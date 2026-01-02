import math
from typing import Union, Any
from functools import total_ordering


@total_ordering
class Rectangle:
    __slots__ = ('_width', '_height')

    def __init__(self, width: float, height: float):
        self._validate_dimension(width)
        self._validate_dimension(height)
        self._width = float(width)
        self._height = float(height)

    @staticmethod
    def _validate_dimension(value: float) -> None:
        if value <= 0:
            raise ValueError("Dimensions must be greater than 0.")

    @property
    def width(self) -> float:
        return self._width

    @property
    def height(self) -> float:
        return self._height

    @property
    def area(self) -> float:
        return self._width * self._height

    @classmethod
    def from_area(cls, area: float) -> 'Rectangle':
        if area <= 0:
            raise ValueError("Area must be positive.")
        side = math.sqrt(area)
        return cls(side, side)

    def __add__(self, other: 'Rectangle') -> 'Rectangle':
        if not isinstance(other, Rectangle):
            return NotImplemented

        total_area = self.area + other.area
        return Rectangle.from_area(total_area)

    def __mul__(self, n: Union[int, float]) -> 'Rectangle':
        if not isinstance(n, (int, float)):
            return NotImplemented
        if n <= 0:
            raise ValueError("Multiplier must be greater than 0.")

        new_area = self.area * n
        return Rectangle.from_area(new_area)

    def __rmul__(self, n: Union[int, float]) -> 'Rectangle':
        return self.__mul__(n)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return math.isclose(self.area, other.area)

    def __lt__(self, other: 'Rectangle') -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area < other.area

    def __str__(self) -> str:
        return f"Rectangle(w={self.width:.2f}, h={self.height:.2f}, area={self.area:.2f})"

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"


if __name__ == "__main__":
    try:
        rect1 = Rectangle(2, 4)
        rect2 = Rectangle(3, 6)

        print(rect1)
        print(rect2)

        rect_sum = rect1 + rect2
        print(rect_sum)

        n = 3
        rect_mul = rect1 * n
        print(rect_mul)

        rect_rmul = 2 * rect1
        print(rect_rmul)

        print(rect1 < rect2)
        print(rect1 == rect2)

        rect3 = Rectangle(1, 8)
        print(rect1 == rect3)

    except ValueError as e:
        print(e)