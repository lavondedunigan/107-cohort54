import pymongo
import certifi

connection_string = "mongodb+srv://testuser:test123@fsdi107.8lfh6.mongodb.net/?retryWrites=true&w=majority&appName=fsdi107"

client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())
db = client.get_database("organika")