
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.x6urf.mongodb.net/pytech?";

client = MongoClient(url)

client = MongoClient "mongodb+srv://admin:admin@cluster0.x6urf.mongodb.net/pytech?";

db = client.pytech

print(db.list_collection_names)
