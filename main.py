import sys
from bruteforce import bruteforce

# python main.py dummy.zip -b

if __name__ == "__main__":
    arg = sys.argv[1:]
    if arg[1] == "-b":
        print("Processing...")
        if len(arg) > 2:
            length = arg[2].split("=")[1].split(",")
            minRep = int(length[0][1:])
            maxRep = int(length[1][:-1])
        password = bruteforce(arg[0])
    else:
        print("Invalid input")
    if password is False:
        print("password not Found!")
    else:
        print('Password is "%s" without quotes.' % password)
