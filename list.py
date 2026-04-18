colors = ["red" , "blue" , "yellow"]

names = ["raouf" , "cherifa" , "hello" , "world" , "python"]


students = {
    "raouf" : "red",
    "cherifa" : "blue",
    "hello" : "yellow"
        }

for student in students:
    print(student, students[student], sep=", ")



student = [
    {"name":"raouf" , "house":"bejaia" , "age":24},
    {"name":"cherifa", "house":"timerit", "age":22},
    {"name":"Hello", "house":"world" , "age":999},
    {"name": "amine" , "house": "tichy" , "age": None}
]

for s in student:
    print(s["name"], s["house"] , s["age"] , sep=", ")

