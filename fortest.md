Понял, добавляю блоки с исходным кодом (`code snippets`) в каждый раздел документации. Это сделает отчет более техническим и наглядным.

Вот обновленная версия документации для `test_shapes.py` с интегрированным кодом.

---

# Unit Tests Documentation

## **Описание тестов для геометрических фигур**

### *Файл test_shapes.py содержит unit-тесты для проверки корректности вычисления площади и периметра, а также валидации входных данных.*

---

## <font color="Cyan"> **Класс CircleTestCase** </font>

**Назначение:** Тестирование функций модуля `circle.py`.

### <font color="LightBlue"> **test_area_positive_radius()** </font>

**Назначение:** Проверяет корректность вычисления площади окружности с положительным радиусом.

**Код теста:**

```python
def test_area_positive_radius(self):
    """Тест площади окружности с положительным радиусом"""
    res = circle.area(5)
    self.assertAlmostEqual(res, math.pi * 25, places=5)

```

**Входные данные:** `r = 5`
**Ожидаемый результат:** `≈ 78.53982`

### <font color="LightBlue"> **test_perimeter_positive_radius()** </font>

**Назначение:** Проверяет корректность вычисления длины окружности.

**Код теста:**

```python
def test_perimeter_positive_radius(self):
    """Тест периметра окружности с положительным радиусом"""
    res = circle.perimeter(3)
    self.assertAlmostEqual(res, 2 * math.pi * 3, places=5)

```

**Входные данные:** `r = 3`
**Ожидаемый результат:** `≈ 18.84956`

### <font color="LightBlue"> **test_area_negative_radius_raises()** </font>

**Назначение:** Проверяет, что отрицательный радиус вызывает исключение.

**Код теста:**

```python
def test_area_negative_radius_raises(self):
    """Проверка, что площадь окружности с отрицательным радиусом вызывает ошибку"""
    with self.assertRaises(ValueError):
        circle.area(-1)

```

**Ожидаемый результат:** `ValueError`

### <font color="LightBlue"> **test_perimeter_negative_radius_raises()** </font>

**Назначение:** Проверяет, что отрицательный радиус при расчете периметра вызывает исключение.

**Код теста:**

```python
def test_perimeter_negative_radius_raises(self):
    """Проверка, что периметр окружности с отрицательным радиусом вызывает ошибку"""
    with self.assertRaises(ValueError):
        circle.perimeter(-5)

```

**Ожидаемый результат:** `ValueError`

---

## <font color="Cyan"> **Класс TriangleTestCase** </font>

**Назначение:** Тестирование функций модуля `triangle.py`.

### <font color="LightBlue"> **test_area_right_triangle()** </font>

**Назначение:** Проверяет формулу Герона на прямоугольном треугольнике.

**Код теста:**

```python
def test_area_right_triangle(self):
    """Тест площади прямоугольного треугольника 3-4-5"""
    res = triangle.area(3, 4, 5)
    self.assertAlmostEqual(res, 6.0, places=5)

```

**Входные данные:** `3, 4, 5`
**Ожидаемый результат:** `6.0`

### <font color="LightBlue"> **test_perimeter_equilateral()** </font>

**Назначение:** Проверяет сумму сторон равностороннего треугольника.

**Код теста:**

```python
def test_perimeter_equilateral(self):
    """Тест периметра равностороннего треугольника"""
    res = triangle.perimeter(5, 5, 5)
    self.assertEqual(res, 15)

```

**Входные данные:** `5, 5, 5`
**Ожидаемый результат:** `15`

### <font color="LightBlue"> **test_area_negative_sides_raises()** </font>

**Назначение:** Проверяет валидацию отрицательных сторон при расчете площади.

**Код теста:**

```python
def test_area_negative_sides_raises(self):
    """Проверка, что площадь треугольника с отрицательными сторонами вызывает ошибку"""
    with self.assertRaises(ValueError):
        triangle.area(-3, 4, 5)

```

**Ожидаемый результат:** `ValueError`

### <font color="LightBlue"> **test_perimeter_negative_sides_raises()** </font>

**Назначение:** Проверяет валидацию отрицательных сторон при расчете периметра.

**Код теста:**

```python
def test_perimeter_negative_sides_raises(self):
    """Проверка, что периметр треугольника с отрицательными сторонами вызывает ошибку"""
    with self.assertRaises(ValueError):
        triangle.perimeter(3, -4, 5)

```

**Ожидаемый результат:** `ValueError`

---

## <font color="Cyan"> **Класс RectangleTestCase** </font>

**Назначение:** Тестирование функций модуля `rectangle.py`.

### <font color="LightBlue"> **test_area_standard()** </font>

**Назначение:** Проверяет вычисление площади прямоугольника.

**Код теста:**

```python
def test_area_standard(self):
    """Тест площади прямоугольника со стандартными размерами"""
    res = rectangle.area(5, 10)
    self.assertEqual(res, 50)

```

**Входные данные:** `5, 10`
**Ожидаемый результат:** `50`

### <font color="LightBlue"> **test_perimeter_standard()** </font>

**Назначение:** Проверяет вычисление периметра прямоугольника.

**Код теста:**

```python
def test_perimeter_standard(self):
    """Тест периметра прямоугольника со стандартными размерами"""
    res = rectangle.perimeter(3, 7)
    self.assertEqual(res, 20)

```

**Входные данные:** `3, 7`
**Ожидаемый результат:** `20`

### <font color="LightBlue"> **test_area_negative_sides_raises()** </font>

**Назначение:** Проверяет ошибку при отрицательных сторонах (площадь).

**Код теста:**

```python
def test_area_negative_sides_raises(self):
    """Проверка, что площадь прямоугольника с отрицательными сторонами вызывает ошибку"""
    with self.assertRaises(ValueError):
        rectangle.area(-5, 10)

```

**Ожидаемый результат:** `ValueError`

### <font color="LightBlue"> **test_perimeter_negative_sides_raises()** </font>

**Назначение:** Проверяет ошибку при отрицательных сторонах (периметр).

**Код теста:**

```python
def test_perimeter_negative_sides_raises(self):
    """Проверка, что периметр прямоугольника с отрицательными сторонами вызывает ошибку"""
    with self.assertRaises(ValueError):
        rectangle.perimeter(3, -7)

```

**Ожидаемый результат:** `ValueError`

---

## <font color="Cyan"> **Класс SquareTestCase** </font>

**Назначение:** Тестирование функций модуля `square.py`.

### <font color="LightBlue"> **test_area_positive_side()** </font>

**Назначение:** Проверяет вычисление площади квадрата.

**Код теста:**

```python
def test_area_positive_side(self):
    """Тест площади квадрата с положительной стороной"""
    res = square.area(4)
    self.assertEqual(res, 16)

```

**Входные данные:** `a = 4`
**Ожидаемый результат:** `16`

### <font color="LightBlue"> **test_perimeter_positive_side()** </font>

**Назначение:** Проверяет вычисление периметра квадрата.

**Код теста:**

```python
def test_perimeter_positive_side(self):
    """Тест периметра квадрата с положительной стороной"""
    res = square.perimeter(5)
    self.assertEqual(res, 20)

```

**Входные данные:** `a = 5`
**Ожидаемый результат:** `20`

### <font color="LightBlue"> **test_area_negative_side_raises()** </font>

**Назначение:** Проверяет ошибку при отрицательной стороне (площадь).

**Код теста:**

```python
def test_area_negative_side_raises(self):
    """Проверка, что площадь квадрата с отрицательной стороной вызывает ошибку"""
    with self.assertRaises(ValueError):
        square.area(-4)

```

**Ожидаемый результат:** `ValueError`

### <font color="LightBlue"> **test_perimeter_negative_side_raises()** </font>

**Назначение:** Проверяет ошибку при отрицательной стороне (периметр).

**Код теста:**

```python
def test_perimeter_negative_side_raises(self):
    """Проверка, что периметр квадрата с отрицательной стороной вызывает ошибку"""
    with self.assertRaises(ValueError):
        square.perimeter(-5)

```

**Ожидаемый результат:** `ValueError`