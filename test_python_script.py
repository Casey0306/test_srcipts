import sys

if __name__ == "__main__":
    for param in sys.argv:
       print(param)
       print(type(param))
    print("Username:")
    print(sys.argv[0])
    print("Password:")
    print(sys.argv[1])
    print("Ip address:")
    print(sys.argv[2])

print("test_python_script")
