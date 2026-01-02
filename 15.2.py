import math
from typing import Union, Any
from functools import total_ordering


@total_ordering
class ProperFraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Zero division error.")

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers.")

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        common = math.gcd(numerator, denominator)

        self.numerator: int = numerator // common
        self.denominator: int = denominator // common

    def __str__(self) -> str:
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self) -> str:
        return f"ProperFraction({self.numerator}, {self.denominator})"

    def __add__(self, other: Union['ProperFraction', int]) -> 'ProperFraction':
        if isinstance(other, int):
            other = ProperFraction(other, 1)

        if not isinstance(other, ProperFraction):
            return NotImplemented

        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __sub__(self, other: Union['ProperFraction', int]) -> 'ProperFraction':
        if isinstance(other, int):
            other = ProperFraction(other, 1)

        if not isinstance(other, ProperFraction):
            return NotImplemented

        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __mul__(self, other: Union['ProperFraction', int]) -> 'ProperFraction':
        if isinstance(other, int):
            other = ProperFraction(other, 1)

        if not isinstance(other, ProperFraction):
            return NotImplemented

        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, int):
            other = ProperFraction(other, 1)

        if isinstance(other, ProperFraction):
            return self.numerator == other.numerator and self.denominator == other.denominator

        return False

    def __lt__(self, other: Union['ProperFraction', int]) -> bool:
        if isinstance(other, int):
            other = ProperFraction(other, 1)

        if not isinstance(other, ProperFraction):
            return NotImplemented

        return (self.numerator * other.denominator) < (other.numerator * self.denominator)


if __name__ == "__main__":
    try:
        f1 = ProperFraction(1, 2)
        f2 = ProperFraction(3, 4)
        f3 = ProperFraction(2, 4)

        print(f1)
        print(f2)
        print(f3)

        print(f1 + f2)
        print(f2 - f1)
        print(f1 * f2)

        print(f1 == f3)
        print(f1 < f2)

        print(f1 * 2)

    except ValueError as e:
        print(e)