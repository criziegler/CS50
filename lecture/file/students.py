import csv

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name}, {house}")
#         # row = line.rstrip().split(",")
        # print(f"{row[0]} is in {row[1]}")

students = []


with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is from {student["home"]}")




# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         # student ["name"] = name
#         # student ["house"] = house
#         students.append(student)
# #         students.appen(f"{name} is in {house}")

# # for student in sorted(students):
# #     print(student)

# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]

# # for student in sorted(students, key=get_name, reverse=True):
# #     print(f"{student["name"]} is in {student["house"]}")
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student["name"]} is in {student["house"]}")