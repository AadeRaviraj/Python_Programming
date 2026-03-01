def Addition(*no):
    print(no)
    print(type(no))  #tuple
    print(len(no))

def main():  
    Addition(11,21,51,101,11) # Duplicate allowed 

if __name__ == "__main__":
    main()