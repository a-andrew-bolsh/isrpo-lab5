import math
import unittest
import circle
import triangle
import rectangle
import square


class CircleTestCase(unittest.TestCase):
    def test_area_positive_radius(self):
        """Тест площади окружности с положительным радиусом"""
        res = circle.area(5)
        self.assertAlmostEqual(res, math.pi * 25, places=5)
    
    def test_perimeter_positive_radius(self):
        """Тест периметра окружности с положительным радиусом"""
        res = circle.perimeter(3)
        self.assertAlmostEqual(res, 2 * math.pi * 3, places=5)
    
    def test_area_negative_radius_raises(self):
        """Проверка, что площадь окружности с отрицательным радиусом вызывает ошибку"""
        with self.assertRaises(ValueError):
            circle.area(-1)
    
    def test_perimeter_negative_radius_raises(self):
        """Проверка, что периметр окружности с отрицательным радиусом вызывает ошибку"""
        with self.assertRaises(ValueError):
            circle.perimeter(-5)
    
    def test_area_string_input_raises(self):
        """Проверка, что передача строки вместо числа вызывает ошибку"""
        with self.assertRaises(TypeError):
            circle.area("5")
    
    def test_perimeter_string_input_raises(self):
        """Проверка, что передача строки вместо числа вызывает ошибку"""
        with self.assertRaises(TypeError):
            circle.perimeter("3")
    
    def test_area_none_input_raises(self):
        """Проверка, что передача None вызывает ошибку"""
        with self.assertRaises(TypeError):
            circle.area(None)
    
    def test_perimeter_none_input_raises(self):
        """Проверка, что передача None вызывает ошибку"""
        with self.assertRaises(TypeError):
            circle.perimeter(None)


class TriangleTestCase(unittest.TestCase):
    def test_area_right_triangle(self):
        """Тест площади прямоугольного треугольника 3-4-5"""
        res = triangle.area(3, 4, 5)
        self.assertAlmostEqual(res, 6.0, places=5)
    
    def test_perimeter_equilateral(self):
        """Тест периметра равностороннего треугольника"""
        res = triangle.perimeter(5, 5, 5)
        self.assertEqual(res, 15)
    
    def test_area_negative_sides_raises(self):
        """Проверка, что площадь треугольника с отрицательными сторонами вызывает ошибку"""
        with self.assertRaises(ValueError):
            triangle.area(-3, 4, 5)
    
    def test_perimeter_negative_sides_raises(self):
        """Проверка, что периметр треугольника с отрицательными сторонами вызывает ошибку"""
        with self.assertRaises(ValueError):
            triangle.perimeter(3, -4, 5)
    
    def test_area_string_input_raises(self):
        """Проверка, что передача строки вместо числа вызывает ошибку"""
        with self.assertRaises(TypeError):
            triangle.area("3", 4, 5)
    
    def test_area_string_input_second_arg_raises(self):
        """Проверка, что передача строки во втором аргументе вызывает ошибку"""
        with self.assertRaises(TypeError):
            triangle.area(3, "4", 5)
    
    def test_area_string_input_third_arg_raises(self):
        """Проверка, что передача строки в третьем аргументе вызывает ошибку"""
        with self.assertRaises(TypeError):
            triangle.area(3, 4, "5")
    
    def test_perimeter_string_input_raises(self):
        """Проверка, что передача строки в периметре вызывает ошибку"""
        with self.assertRaises(TypeError):
            triangle.perimeter("3", 4, 5)


class RectangleTestCase(unittest.TestCase):
    def test_area_standard(self):
        """Тест площади прямоугольника со стандартными размерами"""
        res = rectangle.area(5, 10)
        self.assertEqual(res, 50)
    
    def test_perimeter_standard(self):
        """Тест периметра прямоугольника со стандартными размерами"""
        res = rectangle.perimeter(3, 7)
        self.assertEqual(res, 20)
    
    def test_area_negative_sides_raises(self):
        """Проверка, что площадь прямоугольника с отрицательными сторонами вызывает ошибку"""
        with self.assertRaises(ValueError):
            rectangle.area(-5, 10)
    
    def test_perimeter_negative_sides_raises(self):
        """Проверка, что периметр прямоугольника с отрицательными сторонами вызывает ошибку"""
        with self.assertRaises(ValueError):
            rectangle.perimeter(3, -7)
    
    def test_area_string_input_raises(self):
        """Проверка, что передача строки вместо числа вызывает ошибку"""
        with self.assertRaises(TypeError):
            rectangle.area("5", 10)
    
    def test_area_string_input_second_arg_raises(self):
        """Проверка, что передача строки во втором аргументе вызывает ошибку"""
        with self.assertRaises(TypeError):
            rectangle.area(5, "10")
    
    def test_perimeter_string_input_raises(self):
        """Проверка, что передача строки в периметре вызывает ошибку"""
        with self.assertRaises(TypeError):
            rectangle.perimeter("3", 7)


class SquareTestCase(unittest.TestCase):
    def test_area_positive_side(self):
        """Тест площади квадрата с положительной стороной"""
        res = square.area(4)
        self.assertEqual(res, 16)
    
    def test_perimeter_positive_side(self):
        """Тест периметра квадрата с положительной стороной"""
        res = square.perimeter(5)
        self.assertEqual(res, 20)
    
    def test_area_negative_side_raises(self):
        """Проверка, что площадь квадрата с отрицательной стороной вызывает ошибку"""
        with self.assertRaises(ValueError):
            square.area(-4)
    
    def test_perimeter_negative_side_raises(self):
        """Проверка, что периметр квадрата с отрицательной стороной вызывает ошибку"""
        with self.assertRaises(ValueError):
            square.perimeter(-5)
    
    def test_area_string_input_raises(self):
        """Проверка, что передача строки вместо числа вызывает ошибку"""
        with self.assertRaises(TypeError):
            square.area("4")
    
    def test_perimeter_string_input_raises(self):
        """Проверка, что передача строки вместо числа вызывает ошибку"""
        with self.assertRaises(TypeError):
            square.perimeter("5")
    
    def test_area_list_input_raises(self):
        """Проверка, что передача списка вызывает ошибку"""
        with self.assertRaises(TypeError):
            square.area([4])
    
    def test_perimeter_dict_input_raises(self):
        """Проверка, что передача словаря вызывает ошибку"""
        with self.assertRaises(TypeError):
            square.perimeter({"side": 5})


if __name__ == '__main__':
    unittest.main()