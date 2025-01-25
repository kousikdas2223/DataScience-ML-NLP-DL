print("=============== Example of Class and Inheritance =====================") 
class parent:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def printValues(self):
        print(self.var1, self.var2)

p=parent(4,5)
p.printValues()

class child(parent):
    def __init__(self, var1, var2, var3):
        parent.__init__(self, var1, var2)
        self.var3 = var3

    def printValues(self):
        parent.printValues(self)
        print(self.var3)

c=child(4,5,6)
c.printValues()

class child2(parent):
    def __init__(self, var1, var2, var3):
        parent.__init__(self, var1, var2)
        self.var3 = var3

    def printValues(self):
        parent.printValues(self)
        print(self.var3)

c2=child2(40,50,60)
c2.printValues()

class child3(child,child2):
    def __init__(self, var1, var2, var3, var4):
        child.__init__(self, var1, var2, var3)
        child2.__init__(self, var1, var2, var3)
        self.var4 = var4

    def printValues(self):
        child.printValues(self)
        child2.printValues(self)
        print(self.var4)

c3=child3(4,5,6,7)
c3.printValues()

print("=============== Example of Polymorphism =====================") 

class parent:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def printValues(self):
        print("Parent Class")
        print(self.var1, self.var2)


p=parent(4,5)
p.printValues()

class child(parent):
    def __init__(self, var1, var2, var3):
        parent.__init__(self, var1, var2)
        self.var3 = var3
        super().__init__(var1, var2)

    def printValues(self, var4):
        print("Child Class")
        print(self.var3, var4)

c=child(4,5,6)
c.printValues(7)

print("=============== Example of Abstract Class =====================")


