"""
 Фабричный метод:
Реализуйте паттерн Фабричный метод на языке Python для создания геометрических фигур.
Создайте класс ShapeFactory, имеющий метод create_shape(),
который возвращает объекты различных геометрических фигур.
"""


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        elif shape_type == "triangle":
            return Triangle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            raise ValueError(f"Не удалось определить фигуру: {shape_type}")


class Circle:
    @staticmethod
    def print_info():
        print("Я - круг")


class Square:
    @staticmethod
    def print_info():
        print("Я - квадрат")


class Triangle:
    @staticmethod
    def print_info():
        print("Я - треугольник")


class Rectangle:
    @staticmethod
    def print_info():
        print("Я - прямоугольник")


if __name__ == '__main__':
    ShapeFactory.create_shape('circle').print_info()
    ShapeFactory.create_shape('square').print_info()
    ShapeFactory.create_shape('triangle').print_info()
    ShapeFactory.create_shape('rectangle').print_info()
    try:
        ShapeFactory.create_shape('rhombus').print_info()
    except ValueError as error:
        print(error)