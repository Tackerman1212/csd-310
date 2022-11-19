from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.dvcnh3g.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
students = db.students


print("-- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --")


find_docs = db.students.find({})
for x in find_docs:
    print(x)


#update_one = {{"student_id" : "1007"}, {"$set": {"last_name" : "Ackerman"}}}
result = db.students.update_one({'_id': 1007}, {'$set': {'last_name':'Ackerman'}})


print("-- DISPLAYING STUDENT DOCUMENT 1007 --")


find_one = db.students.find_one({"_id" : 1007})
print(find_one)