# def f(*args, *kwargs):
#     print("Positional:", args)

# f(1000, 50, 25)

def f(*args, **kwargs):
    print("Named: ", kwargs)

# kwargs is a dictionary 
f(galleons=100, sickles=50, knuts=25)