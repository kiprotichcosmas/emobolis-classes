class Circle:

    def __init__(self, radius):  # constructor
        self.circle_radius = radius

    def calc_area(self):
        a = 22 / 7 * self.circle_radius ** 2
        print(f"Area is {a}")

    def calc_perimeter(self):
        p = 22 / 7 * self.circle_radius * 2
        print(f"Circumference is {p}")


circle1 = Circle(10)
circle2 = Circle(14)
circle3 = Circle(22.7)
circle4 = Circle(700.90)

circle1.calc_area()
circle1.calc_perimeter()

circle2.calc_area()
circle2.calc_perimeter()

circle3.calc_area()
circle3.calc_perimeter()

circle4.calc_area()
circle4.calc_perimeter()
