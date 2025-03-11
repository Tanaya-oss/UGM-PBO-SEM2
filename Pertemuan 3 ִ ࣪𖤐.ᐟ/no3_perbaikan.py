class Shape:
    def __init__(self, width):
        self.width = width

class Square(Shape):
    name = "Square"
    
    def get_area(self):
        return self.width ** 2
    
    def tampilkan_luas(self):
        print("Luas Square: ", self.get_area())
    
class Triangle(Shape):
    name = "Triangle"
    
    def __init__(self, width, height):
        super().__init__(width)  
        self.height = height

    def get_area(self):
        return 0.5 * self.width * self.height
    
    def tampilkan_luas(self):
        print("Luas Triangle: ", self.get_area())
    

SquareX = Square(5)
TriangleX = Triangle(5, 3)

SquareX.tampilkan_luas()
TriangleX.tampilkan_luas()