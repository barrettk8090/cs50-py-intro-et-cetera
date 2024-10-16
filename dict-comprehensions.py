students = ["Hermione", "Harry", "Ron"]

# gryffindors = []

# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

# Using list & dictionary comprehension - list of dictionaries
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# Even more simplified, just using dictionary comprehensions  - just a single dictionary
gryffindors2 = {student: "Gryffindor" for student in students}

print(gryffindors2)