import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://badoy4:Vocaloid3@cluster-cs4800scheduler.oamlzkk.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["UIDs"]

post = {"_id": 1, "name": "Bob", "pass":"Something"}
post2 = {"_id": 2, "name": "Bob", "pass":"Something"}

# collection.insert_one(post) - Adds 1 post
# collection.insert_many([post, post2]) - Adds all posts

#results = collection.find({"name":"Bob"}) - Finds all entries with name of Bob

# Prints _id Item of entry with Bob---------------------
#for result in results:
#    #print(result) - Gets String of Code
#    print(result["_id"]) 

# Finds the one entry with ID of _1
#result2 = collection.find_one({"_id":1})
#print(result2)

#collection.delete("_id":0) - Deletes item from DB
#collection.delete_many({"_id":0}) - Deletes items (multiple) from DB

# Prints all entries------------------
#results = collection.find({})
#for x in results:
#    print(x)

#collection.update_one({"_id": 1},{"$set":{"name":"tim"}}) - Updates an item in an entry
#collection.update_one({"_id": 1},{"$set":{"hello":"tim"}}) - Adds new query
# $inc - Increases value by number

post_count = collection.count_documents({}) # Shows count of items in collection
print(post_count)