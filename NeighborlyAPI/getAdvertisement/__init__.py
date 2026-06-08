import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging
from config import COSMOS_CONNECTION_STRING, DATABASE_NAME, POST_COLLECTION, ADVERTISEMENT_COLLECTION

def main(req: func.HttpRequest) -> func.HttpResponse:

    # example call http://localhost:7071/api/getAdvertisement/?id=5eb6cb8884f10e06dc6a2084

    id = req.params.get('id')
    print("--------------->", id)
    
    if id:
        try:
            client = pymongo.MongoClient(COSMOS_CONNECTION_STRING)
            database = client['DATABASE_NAME']
            collection = database['ADVERTISEMENTS_COLLECTION']
           
            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            print("----------result--------")

            result = dumps(result)
            print(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)