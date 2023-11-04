from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings #HuggingFaceInstructEmbeddings
#database is saved locally
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


vectorstore = None
conversation_chain = None

def get_pdf_text():
   text = ""
   pdf_docs = ["docs/cough.pdf"]
   for pdf in pdf_docs:
      pdf_reader = PdfReader(pdf)
      for page in pdf_reader.pages:
          text += page.extract_text()
   return text
 

def get_text_chunks(text):
   text_splitter = CharacterTextSplitter(
      separator="\n",
      chunk_size=1000,
      chunk_overlap=200,
      length_function=len 
   )
   chunks = text_splitter.split_text(text)
   return chunks


def get_vectorstore(text_chunks):                                                                                                                        
   embeddings = OpenAIEmbeddings()
   # index = faiss.IndexFlatL2(embeddings.shape[1])
   # index.add(embeddings)
   #embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
   vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
   return vectorstore


def get_conversation_chain(vectorstore):
   llm = ChatOpenAI()
   memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
   conversation_chain = ConversationalRetrievalChain.from_llm(
      llm=llm,
      retriever=vectorstore.as_retriever(), 
      memory=memory  
  )
   return conversation_chain
 



def main():
    global conversation_chain
    load_dotenv()
    raw_text = get_pdf_text()
    text_chunks = get_text_chunks(raw_text)
    vectorstore = get_vectorstore(text_chunks) 
    conversation_chain = get_conversation_chain(vectorstore)

def ask(prompt):
   global conversation_chain
   res = conversation_chain(prompt)
   chat_history = [message.content for message in res['chat_history']]
   return chat_history

if __name__ == '__main__':
    main()