class Foo:
    def __init__(self) -> None:
        self._x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, a):
        if a > 0:
            self._x = int(str(a)[-2:])
        elif a < 0:
            self._x = (-1)
        else:
            self._x = 0
