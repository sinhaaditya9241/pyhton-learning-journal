# tpyes of inheritance

# 1. single inheritance
# 2. multiple inheritance
# 3. multilevel inheritance

# single level inheritance

class A:

    def state_1(self):
        print("This is class A")
    
    def state_2(self):
        print("This is state 2 of class A")
    
    def state_3(self):
        print("This is state 3 of class A")

class B:

    def state_4(self):
        print("This is class B")

    def state_5(self):
        print("This is state 5 of class B")
'''
a = A()
a.state_1()
a.state_2()


b = B()
b.state_4()
b.state_5()
b.state_3()
'''
# MULTI LEVEL INHERITANCE

class C(A,B):

    def state_6(self):
        print("this is class C")
'''
c = C()
c.state_6()
c.state_5()
c.state_3()
c.state_1()
'''
# MUTIPLE INHERITANCE

a = A()
a.state_3

b = B()
b.state_5

c = C()
c.state_1()