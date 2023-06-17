class Rectangle:  

    def __init__(self, x, y, width, height): # придаю __init__ аргументы для х,у
        self.x = x
        self.y = y
        self.width = width 
        self.height = height

    def move(self, deltaX, deltaY): 
        self.x += deltaX
        self.y += deltaY

    def resize(self, deltaWidth, deltaHeight): 
        self.width += deltaWidth
        self.height += deltaHeight

    def contains(self, other): 
        return (self.x <= other.x and self.y <= other.y and 
                self.x + self.width >= other.x + other.width and
                self.y + self.height >= other.y + other.height)

    def intersection(self, other):
        if not self.contains(other) and not other.contains(self):
            return None

        x = max(self.x, other.x)
        y = max(self.y, other.y)
        bottom_right_x = min(self.x + self.width, other.x + other.width)
        bottom_right_y = min(self.y + self.height, other.y + other.height)

        return Rectangle(x, y, bottom_right_x - x, bottom_right_y - y)

    def union(self, other): 
        x = min(self.x, other.x)
        y = min(self.y, other.y)
        bottom_right_x = max(self.x + self.width, other.x + other.width)
        bottom_right_y = max(self.y + self.height, other.y + other.height)

        return Rectangle(x, y, bottom_right_x - x, bottom_right_y - y)

    def __str__(self): 
        return f'Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})'

# Пример использования класса
rect1 = Rectangle(0, 0, 10, 5)
print(rect1)  # Rectangle(x=0, y=0, width=10, height=5) 

rect1.move(3, 2)
print(rect1)  # Rectangle(x=3, y=2, width=10, height=5)

rect1.resize(2, 1)
print(rect1)  # Rectangle(x=3, y=2, width=12, height=6)

rect2 = Rectangle(5, 3, 8, 6)
union_rect = rect1.union(rect2)
print(union_rect)  # Rectangle(x=3, y=2, width=10, height=7)
#(объединение rect1 и rect2 и его вывод на экран).

intersection_rect = rect1.intersection(rect2)
print(intersection_rect)  # Rectangle(x=5, y=3, width=8, height=4)
#(пересечение rect1 и rect2 и его вывод на экран).
