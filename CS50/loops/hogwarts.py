#students = ["Hermione", "Harry", "Ron", "Draco"]
#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

#for i in range(len(students)):
#    print(i + 1, students[i])

#dict
students = {"Hermione": "Gryffindor", 
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")