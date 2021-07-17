# Task 1

d=[]
e=[]
class MathP:

    def __init__(self, target):
        self.target = target

    def get_numbers(self):
        target = int(self.target)
        num_count = int(input("How many numbers do you want to input?: "))
        for i in range(num_count):
            num = int(input("Enter your number: "))
            d.append(num)
        lenght = len(d)
        for i in range(lenght):
            for j in range(lenght):
                if (d[i] + d[j]) == target and not i==j and i<j:
                    e.append([i, j])
        print(e)

target1 = MathP(50)
print(target1.get_numbers())

# Task 2
    
class ClassNameToPrint:
    
    def __init__(self):
        print(type(self).__name__)
    
a = ClassNameToPrint()


# Task 3
class Point3D:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
    

my_point = Point3D(1,2,3)
print(my_point.__repr__())