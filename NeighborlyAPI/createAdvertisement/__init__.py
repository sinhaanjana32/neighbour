import azure.functions as func
import pymongo
from config import COSMOS_CONNECTION_STRING, DATABASE_NAME, POST_COLLECTION, ADVERTISEMENT_COLLECTION

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            client = pymongo.MongoClient(COSMOS_CONNECTION_STRING)
            database = client['DATABASE_NAME']
            collection = database['ADVERTISEMENTS_COLLECTION']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )