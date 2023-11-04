from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings #HuggingFaceInstructEmbeddings
#database is saved locally
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

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


def get_conversation_chain(vectorstore,prompt):
   llm = ChatOpenAI()
   conversation_chain = ConversationChain(
      llm=llm,
     verbose=True,
      memory=ConversationBufferMemory()  
  )
   return conversation_chain.predict(input=prompt)
 



def main(prompt):
    load_dotenv()
    raw_text = get_pdf_text()
    text_chunks = get_text_chunks(raw_text)
    vectorstore = get_vectorstore(text_chunks) 
    # response = st.session_state.conversation({'question': prompt})
    # st.session_state.chat_history = response['chat_history']

    # for i, message in enumerate(st.session_state.chat_history):
    #     print(message)
    answer = get_conversation_chain(vectorstore,prompt)
    return answer


if __name__ == '__main__':
    main()