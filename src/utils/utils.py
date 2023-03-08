
class Vector2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def add(self, vector: 'Vector2') -> None:
        self.x += vector.x
        self.y += vector.y

    def mul(self, vector: 'Vector2') -> None:
        self.x *= vector.x
        self.y *= vector.y

    def sub(self, vector: 'Vector2') -> None:
        self.x -= vector.x
        self.y -= vector.y

    def div(self, vector: 'Vector2') -> None:
        self.x /= vector.x
        self.y /= vector.y

    @property
    def get_cord(self) -> tuple:
        return (self.x, self.y)

    def __repr__(self) -> str:
        return (self.x, self.y)
