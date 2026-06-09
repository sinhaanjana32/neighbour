import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from config import ADVERTISEMENT_COLLECTION, COSMOS_CONNECTION_STRING, DATABASE_NAME

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        client = pymongo.MongoClient(COSMOS_CONNECTION_STRING)
        database = client[DATABASE_NAME]
        collection = database[ADVERTISEMENT_COLLECTION]



        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

