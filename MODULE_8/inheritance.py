class name:
    x = 0 
    name = ""

    def __init__(self, z):
        self.name = z
        print("hii", z)

class football_fan(name):
    points = 0 
    
    def pts(self):
        print(self.name,"scores")

n = name ("sam")
f = football_fan("jin")
f.pts()