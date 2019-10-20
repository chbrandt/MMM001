# Because no programming course really exist without a "Hello World!"
import sys

def greet_user(name):
    return "Hello {}!".format(name.upper())

if __name__ == "__main__":
    try:
        res = greet_user(sys.argv[1])
        print(res)
    except:
        print("Usage: {} <name>".format(sys.argv[0]))
        
