class A:
    def method_A(self):
        print("ini adalah method A")

class B:
    def method_B(self):
        print("ini adalah method B")

class apalah(A,B):
    pass

horw = apalah()
horw.method_A()
horw.method_B()
