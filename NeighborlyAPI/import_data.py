import json
import pymongo
from config import COSMOS_CONNECTION_STRING

CONNECTION_STRING = COSMOS_CONNECTION_STRING
client = pymongo.MongoClient(CONNECTION_STRING)

db = client["anjananeighborly"]

# Import advertisements
with open("sample_data/advertisements.json") as f:
    advertisements = json.load(f)

db["advertisements"].insert_many(advertisements)

# Import posts
with open("sample_data/posts.json") as f:
    posts = json.load(f)

db["posts"].insert_many(posts)

print("Data imported successfully")