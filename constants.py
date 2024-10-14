#  No constants in Python - instead use CAPITALIZATION to demonstrate that MEOWS should be constrant/unchanged.

# MEOWS = 3

# for _ in range(MEOWS):
#     print("meow")

# Can use "constants" within the constraints of a class

class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()