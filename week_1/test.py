from pymongo import MongoClient



client = MongoClient("mongodb+srv://<PROJECT>:<PROJECT-PWD>@mflix-d8wrg.mongodb.net/mflix?authSource=admin")
db = client.test
print client.mflix
