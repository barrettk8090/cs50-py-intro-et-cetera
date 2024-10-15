# def main():
#     yell("This", "is", "CS50")


# def yell(*words):
#     uppercased = [word.upper() for word in words]
#     print(*uppercased)

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# gryffindors = []
# for student in students:
#     if student["house"] == "Gryffindor":
#         gryffindors.append(student["name"])


# The gryffindors list should be names of students - loop through students if a students house is Gryffindor 
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)