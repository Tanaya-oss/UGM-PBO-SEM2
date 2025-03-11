class Shape:
    width = 0
    def __init__(self, width):
        self.width = width

class Square(Shape):
    name = "Square"
    def get_area(self):
        return self.width**2
    
    def tampilkan_luas(self):
       print("Luas Square: ",SquareX.get_area())
    
class Triangle(Shape):
    name = "Triangle"
    height = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return 0.5 * width * height
    
    def tampilkan_luas(self):
        print("Luas Tiangle: ",TriangleX.get_area())
    
SquareX = Square(5)
TriangleX = Triangle(5,3)


    



