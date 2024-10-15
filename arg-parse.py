import argparse

# Run -h or --help for documentation on usage

parser = argparse.ArgumentParser(description="meow like a cat")
# add an argument to the command line, -n, and provide a default run value, helper, and require int type
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")