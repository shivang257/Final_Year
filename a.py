from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
# Get a list of database names
database_names = client.list_database_names()
print("Available databases:", database_names)

# Access a specific database
database = client["aadharDB"]

# Get a list of collection names in the database
collection_names = database.list_collection_names()
print("Collections in the database:", collection_names)

# Access a specific collection
collection = database["aadhar_data"]

# Count documents in a collection
document_count = collection.count_documents({})
print("Total documents in the collection:", document_count)
