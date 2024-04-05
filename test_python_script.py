import sys

if __name__ == "__main__":
    for param in sys.argv:
       print(param)
       print(type(param))
    print("Path GIT")
    print(sys.argv[0])
    print("Username:")
    print(sys.argv[1])
    print("Password:")
    print(sys.argv[2])
    print("Ip address:")
    print(sys.argv[3])
    x = 1/0
    raise Exception('spam', 'eggs')
    print("test_python_script")
