def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

# Using the yield keyword - one value at a time
# Yield returns an iterator 
def sheep(n):
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()
