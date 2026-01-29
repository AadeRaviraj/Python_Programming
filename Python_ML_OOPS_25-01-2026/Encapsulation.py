class Arithematic :
    
    def __init__(self, A,B):
        self .No1 = A
        self.No2 = B
        print("Object gets created successfully...")
    
    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction (self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans
    
Obj1 = Arithematic(11, 10)
    
Obj2 = Arithematic(21,20)

Ret = Obj1.Addition() 
print(Ret)


Ret = Obj2.Substraction() 
print(Ret)
    