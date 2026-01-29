import os

def main():
    print("Pid of running process is : ", os.getpid())
    print("Pid of parent process is ", os.getppid())


if __name__ == "__main__":
    main( )