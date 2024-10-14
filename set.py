students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

#  WITHOUT USING SETS 
# houses = []
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])

# for house in sorted(houses):
#     print(house)

# SET - REMOVE DUPLICATES

houses = set()
for student in students:
    # sets use .add instead of .append for arrays
    houses.add(student["house"])

for house in sorted(houses):
    print(house)