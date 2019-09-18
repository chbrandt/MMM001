import sys

def make_upper(word):
    return word.upper()

def greet_user(name):
    return "Hello {}!".format(make_upper(name))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <name>".format(sys.argv[0]))
    else:
        res = greet_user(sys.argv[1])
        print(res)

