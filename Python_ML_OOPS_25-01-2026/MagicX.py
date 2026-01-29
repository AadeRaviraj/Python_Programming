# Dunder method  / Magic method / Special Method

class Demo:
    def __init__(self, A):
        self.No = A
    
    def __add__(self,other):
        return self.No + other.No
    
    def __sub__(self,other):
        return self.No - other.No
    
    def __mul__(self,other):
        return self.No * other.No
    
    def __truediv__(self,other):
        return self.No / other.No
    
obj1 = Demo(11)
obj2 = Demo(12)

print(11 + 21 )

print(obj1 + obj2)  # __add__(Obj1, Obj2)

print(obj1 - obj2) # __sun__(Obj1, Obj2)

print(obj1 * obj2) # __mul__(Obj1, Obj2)

print(obj1 / obj2) # __trvediv__(Obj1, Obj2)

