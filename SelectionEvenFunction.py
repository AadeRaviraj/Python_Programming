def CheckEven(No):
    if No % 2 == 0 :
        print("It is even")
    else:
        print("It is Odd")

def main():
    CheckEven(21)   # Positional  Args
    CheckEven(No = 22)   # Keyword Args

if __name__ == "__main__":
    main()