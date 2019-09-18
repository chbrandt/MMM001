import sys

def greet_user(name):
    return "Hello {}!".format(name.upper())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <name>".format(sys.argv[0]))
    else:
        res = greet_user(sys.argv[1])
        print(res)
