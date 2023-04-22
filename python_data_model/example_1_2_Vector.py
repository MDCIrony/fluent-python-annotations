import math


class Vector:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x!r}, {self.y!r})"  # -> !r is used for a correct type representation

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar: float):
        return Vector(self.x * scalar, self.y * scalar)
