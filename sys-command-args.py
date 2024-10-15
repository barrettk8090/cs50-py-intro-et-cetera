import sys

if len(sys.argv) == 1:
    print("meow")
# 3 command line arguments: (python) arg-parse.py -n 3 
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    # save the third command line argument to a variable, e.g 3
    n = int(sys.argv[2])
    # print that many meows
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")

# SeeL arg-parse.py for translation using argparse import