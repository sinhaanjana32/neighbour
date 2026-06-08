import json
import pymongo

CONNECTION_STRING = "mongodb://anjananeighborlycosmos01:sB4EyS12ev5Zr9sduHXrVDj58l6Z8xxpPPM49qVNEbzjvGdD22dcXYFRW5TrjfdAqyX6OiMGEANEACDbYQ8RmA==@anjananeighborlycosmos01.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@anjananeighborlycosmos01@"

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