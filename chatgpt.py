import os
import sys

import constants
from langchain.document_loaders import TextLoader

# from langchain.document_loaders import DirectoryLoader

from langchain.indexes import VectorstoreIndexCreator
#from langchain.llms import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.APIKEY

# if len(sys.argv)< 2:
#     print("Error: No command-line arg provided")
# else:
#  query = sys.argv[1]
query = ""
try:
    query = sys.argv[1]
except IndexError:
    print("Error: No command-line arg provided")


loader = TextLoader('data.txt')
# loader = DirectoryLoader(".", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))
# print(index.query(query, llm=ChatOpenAI))