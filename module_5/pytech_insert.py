from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.dvcnh3g.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
students = db.students


thorin = {
    "student_id" : "1007",
    "first_name" : "Thorin",
    "last_name" : "Oakenshield"
}

thorin_student_id = students.insert_one(thorin).inserted_id


bilbo = {
    "student_id" : "1008",
    "first_name" : "Bilbo",
    "last_name" : "Baggins"
}

bilbo_student_id = students.insert_one(bilbo).inserted_id


frodo = {
        "student_id" : "1009",
    "first_name" : "Frodo",
    "last_name" : "Baggins"
}

frodo_student_id = students.insert_one(frodo).inserted_id


print("--  INSERT STATEMENTS --")
print("Inserted student record", {thorin["first_name"]}, {thorin["last_name"]}, "into the students collection with document_id", thorin_student_id) 
print("Inserted student record", {bilbo["first_name"]}, {bilbo["last_name"]}, "into the students collection with document_id", bilbo_student_id) 
print("Inserted student record", {frodo["first_name"]}, {frodo["last_name"]},"into the students collection with document_id", frodo_student_id) 
