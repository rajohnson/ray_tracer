import vec3


class Color(vec3.Vec3):
    def __init__(self, r: float, g: float, b: float) -> None:
        super().__init__(r, g, b)

    @property
    def r(self) -> float:
        return self.x

    @r.setter
    def r(self, value: float) -> None:
        self.x = value

    @property
    def g(self) -> float:
        return self.y

    @g.setter
    def g(self, value: float) -> None:
        self.y = value

    @property
    def b(self) -> float:
        return self.z

    @b.setter
    def b(self, value: float) -> None:
        self.z = value

    def __str__(self):
        return f"{int(round(255 * self.r))} {int(round(255 * self.g))} {int(round(255 * self.b))}"
