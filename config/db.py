from pymongo import MongoClient

MONGO_URI = 'mongodb+srv://<username>:<password>@samit.accuvxz.mongodb.net/<dbname>?retryWrites=true&w=majority'

conn = MongoClient(MONGO_URI)
db = conn.notes
collectionName = db['notes']