class vegetables:

    def __init__(self,carrrot,beans):
        self.carrrot = carrrot
        self.beans = beans
    
    def __add__(self,other):
        carrot = self.carrrot + other.carrrot
        beans = self.beans + other.beans
        return vegetables(carrot,beans)

v1 = vegetables(1,2)
v2 = vegetables(3,4)
v3 = vegetables(5,6)

v4= v1 + v2 + v3

print(v4)