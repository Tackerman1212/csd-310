from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.dvcnh3g.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
students = db.students

find_docs = db.students.find({})

print("--  DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --")

#print(find_docs)
for x in find_docs:
    print(x)

find_one_docs = db.students.find_one({"student_id": "1007"})


print("--  DISPLAYING STUDENT DOCUMENTS FROM find_one() QUERY --")

print(find_one_docs)
#for x in find_one_docs:
    #print(x)