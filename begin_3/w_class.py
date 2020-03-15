class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def vol(self):
        print(self.x * self.y * self.z)

cube_1 = Cube (11.5,23,5)
num1 = int(input('Enter NUmber: '))
num2 = int(input('Enter NUmber: '))
num3 = int(input('Enter NUmber: '))
cube_2 = Cube (num1, num2, num3)
cube_2.vol()        