import os

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS

DB_FAISS_PATH = r"vectorstore/db_faiss"

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


prompt_template = """
Use the following pieces of context to answer the users question briefly
and preciesly, don't miss any information or qoutes and don't try to make up an answer out of context.

If you don't know the answer, just say that you don't know, don't try to make up an answer.
Clearly state when the chatbot doesn't have information on a particular query.

Allow users to retrieve information about the ingredients of specific Ayurvedic remedies by providing the name of the remedy. 
Respond with a list of ingredients.

If you don't know the answer, just say that you don't know, don't try to make up an answer.
Clearly state when the chatbot doesn't have information on a particular query.

Always include a 'INGREDIENT : ' section in the response, refering to list of ingredients based on ayurvedic remedies

Enable users to share health concerns or symptoms then suggest appropriate Ayurvedic remedies, dos and don'ts as per the  sympotms.

the format should always be like :- 

                    REMEDIES PROCESS DESCRIPTION : 
                    INGREDIENTS : 
                    DOS : 
                    DON'TS :

If users inquire about the chatbot, provide a brief explanation of its identity and function.
Greet users back when they initiate a greeting.

Always provide details of refrenced and relevant books and their authors in the 'SOURCES : ' section.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""


def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    return prompt


def create_retrieval_qa_chain(llm, prompt, db):
    """
    Creates a Retrieval Question-Answering (QA) chain using a given language model, prompt, and database.

    This function initializes a RetrievalQA object with a specific chain type and configurations,
    and returns this QA chain. The retriever is set up to return the top 3 results (k=3).

    Args:
        llm (any): The language model to be used in the RetrievalQA.
        prompt (str): The prompt to be used in the chain type.
        db (any): The database to be used as the retriever.

    Returns:
        RetrievalQA: The initialized QA chain.
    """
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 2}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt},
    )
    return qa_chain


# initialize openai chat model
llm = ChatOpenAI(model="gpt-3.5-turbo")


def create_retrieval_qa_bot(
    model_name="text-embedding-ada-002", persist_dir=DB_FAISS_PATH
):
    """
    This function creates a retrieval-based question-answering bot.

    Parameters:
        model (str): The name of the model to be used for embeddings.
        persist_dir (str): The directory to persist the database.

    Returns:
        RetrievalQA: The retrieval-based question-answering bot.

    """

    if not os.path.exists(persist_dir):
        raise FileNotFoundError(f"No directory found at {persist_dir}")

    try:
        embeddings = OpenAIEmbeddings(model=model_name)  # type: ignore
    except Exception as e:
        raise Exception(
            f"Failed to load embeddings with model name {model_name}: {str(e)}"
        )

    db = FAISS.load_local(folder_path=DB_FAISS_PATH, embeddings=embeddings)

    qa_prompt = (
        set_custom_prompt()
    )  # Assuming this function exists and works as expected

    try:
        qa = create_retrieval_qa_chain(
            llm=llm, prompt=qa_prompt, db=db
        )  # Assuming this function exists and works as expected
    except Exception as e:
        raise Exception(f"Failed to create retrieval QA chain: {str(e)}")

    return qa

conversation_history = []

def retrieve_bot_answer(query):
    """
    Retrieves the answer to a given query using a QA bot.

    This function creates an instance of a QA bot, passes the query to it,
    and returns the bot's response.

    Args:
        query (str): The question to be answered by the QA bot.

    Returns:
        dict: The QA bot's response, typically a dictionary with response details.
    """

    conversation_history.append(query)

    qa_bot_instance = create_retrieval_qa_bot()
    bot_response = qa_bot_instance({"query": query, "context": conversation_history})

    conversation_history.append(bot_response['result'])

    return bot_response['result']


def final_result(query):
    qa_result = retrieve_bot_answer(query)
    response = qa_result
    return response

def main():

    query = ""
    
    while query!="quit":

        query = input("Enter the query ? ->  ")
        answer = final_result(query)

        print(answer)

        file = open("output.txt", "w")
        file.write(answer)

if __name__ == "__main__" :
    main()


