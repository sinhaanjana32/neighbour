import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from config import COSMOS_CONNECTION_STRING, DATABASE_NAME, POST_COLLECTION, ADVERTISEMENT_COLLECTION


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        client = pymongo.MongoClient(COSMOS_CONNECTION_STRING)
        database = client['DATABASE_NAME']
        collection = database['POST_COLLECTION']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)