import pymongo

url='mongodb://localhost:27017'
client = pymongo.MongoClient(url)

db = client['django_api']
# production = client.production
# person_collection = production.person_collection