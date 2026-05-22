student = {
    "name": "Rahul",
    "age": 20,
    "city": "Jaipur"
}
student["course"]="CSE"
print(student)
student["age"]=21
student.pop("course")
print(student)
del student["city"]
print(student)
print("name" in student)
print(len(student))    