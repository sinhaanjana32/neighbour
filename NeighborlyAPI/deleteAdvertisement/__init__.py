import azure.functions as func
import pymongo
from bson.objectid import ObjectId
from config import COSMOS_CONNECTION_STRING, DATABASE_NAME, POST_COLLECTION, ADVERTISEMENT_COLLECTION


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            client = pymongo.MongoClient(COSMOS_CONNECTION_STRING)
            database = client[DATABASE_NAME]
            collection = database[ADVERTISEMENT_COLLECTION]
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
