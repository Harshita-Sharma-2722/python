student={
    "name":"harshita",
    "class":12,
    "age":20
}
print("Dictionary= ",student)
#access value
print("access= ",student["class"])
#length
print("length= ",len(student))
#adding new
student["marks"]=85
#key:value
print(student)
for key,value in student.items():
    print(key,":",value)
