import os

COSMOS_CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING") or "mongodb://anjananeighborlycosmos01:3FsCThMsa0ULpSMJbpGHW3oZUmewwNs8mIdWcvkRUTCrufYyQ2X39RcsWBJ8andjLfK6hf0zhW0OACDb0IhFcw==@anjananeighborlycosmos01.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@anjananeighborlycosmos01@"

DATABASE_NAME = "anjananeighborly"

ADVERTISEMENT_COLLECTION = "advertisements"

POST_COLLECTION = "posts"

EVENTHUB_CONNECTION_STRING = os.environ.get("EVENTHUB_CONNECTION_STRING") or "Endpoint=sb://anjananeighborlyeventhub.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=3FsCThMsa0ULpSMJbpGHW3oZUmewwNs8mIdWcvkRUTCrufYyQ2X39RcsWBJ8andjLfK6hf0zhW0OACDb0IhFcw==;EntityPath=neighborlyevents"