from pymongo import MongoClient

client = MongoClient("127.0.0.1:27017")

db = client["datasets"]

# Access a collection
collection = db["image_collection"]

# # Insert a document
# document = {"name": ["hossein","ali","mamad"],}
# collection.insert_one(document)

# # Find documents
# result = collection.find()
# for doc in result:
#     print(doc)

# # Update a document
# collection.update_one({"Label": "test"},{"Quantity":4},{"image_url":[
#     'test1',
#     'test2',
#     'test3'
# ]})

# # Delete a document
# collection.delete_one({"name": "John"})


