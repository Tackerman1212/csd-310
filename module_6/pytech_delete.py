from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.dvcnh3g.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
students = db.students


print("-- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --")


find_docs = db.students.find({})
for x in find_docs:
    print(x)


print("-- INSERT STATEMENTS --")


john = {
    "_id" : 1010,
    "first_name" : "John",
    "last_name" : "Doe"
}
john_document_id = students.insert_one(john).inserted_id


print("Inserted student record", {john["first_name"]}, {john["last_name"]}, "into the students collection with document_id", john_document_id) 


print("-- DISPLAYING STUDENT TEST DOC --")


find_one_docs = db.students.find_one({"_id": 1010})


print(find_one_docs)


students.delete_one({"_id": 1010})


print("-- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --")


find_docs = db.students.find({})
for x in find_docs:
    print(x)