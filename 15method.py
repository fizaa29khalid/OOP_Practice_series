class A:
    def show(self):
        print("Method in Class A")

class B(A):
    def show(self):
        print("Method in Class B")

class C(A):
    def show(self):
        print("Method in Class C")

class D(B, C):
    pass

# Creating an object of Class D
obj = D()

# Calling show() method on obj
obj.show()

# Observing MRO
print("\nMethod Resolution Order (MRO) of class D:")
print(D.__mro__)
