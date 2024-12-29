import math


class Vec3:
    """
    a generic class for a 3 dimensional vector
    """

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self._e = [x, y, z]

    @property
    def x(self) -> float:
        return self._e[0]

    @x.setter
    def x(self, value: float) -> None:
        self._e[0] = value

    @property
    def y(self) -> float:
        return self._e[1]

    @y.setter
    def y(self, value: float) -> None:
        self._e[1] = value

    @property
    def z(self) -> float:
        return self._e[2]

    @z.setter
    def z(self, value: float) -> None:
        self._e[2] = value

    def __neg__(self) -> "Vec3":
        return Vec3(-self.x, -self.y, -self.z)

    def __getitem__(self, index: int) -> float:
        if index not in (0, 1, 2):
            raise IndexError("Index out of range")
        return self._e[index]

    def __setitem__(self, index: int, value: float) -> None:
        if index not in (0, 1, 2):
            raise IndexError("Index out of range")
        self._e[index] = value

    def __iter__(self):
        return iter(self._e)

    def __add__(self, other: "Vec3") -> "Vec3":
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other: "Vec3") -> "Vec3":
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other: "Vec3") -> "Vec3":
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __isub__(self, other: "Vec3") -> "Vec3":
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __mul__(self, other) -> "Vec3":
        if isinstance(other, (int, float)):  # scalar multiplication
            return Vec3(self.x * other, self.y * other, self.z * other)
        if isinstance(other, Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        raise NotImplementedError("other operand must be a scalar or Vec3 object")

    def __rmul__(self, other) -> "Vec3":
        return self * other

    def __eq__(self, other: "Vec3") -> bool:
        return (
            math.isclose(self.x, other.x)
            and math.isclose(self.y, other.y)
            and math.isclose(self.z, other.z)
        )

    def __truediv__(self, other) -> "Vec3":
        if isinstance(other, (int, float)):
            # use the __mul__ method since it is already implemented
            return self * (1 / other)
        raise NotImplementedError("other operand must be a scalar")

    def length(self) -> float:
        return math.sqrt(self.length_squared())

    def length_squared(self) -> float:
        return self.x**2 + self.y**2 + self.z**2

    def __repr__(self) -> str:
        return f"Vec3({self.x}, {self.y}, {self.z})"

    def dot(self, other: "Vec3") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: "Vec3") -> "Vec3":
        return Vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def unit_vector(self) -> "Vec3":
        return self / len(self)
