class Demo :
    No = 10
    
    def __init__(self, A , B ):
        self.Value1 = A
        self. Value2 = B
        
    def fun(self):
        
        print("Inside Instance method Fun :", self.Value1, self.Value2)
    
    @classmethod
    def sun(cls):
        print("Inside Class method sun : ", cls.No)


Demo.sun()  # class method 
print("Class variable No : ", Demo.No)

obj = Demo(11,21)

obj.fun()  # instance function
print("Instance variable : ", obj.Value1, obj.Value2)