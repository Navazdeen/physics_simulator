import pygame
from ..utils import Vector2

class Cirle(pygame.Circle):
    def __init__(self, cord: Vector2, radius: int) -> None:
        self.cord = cord
        self.radius = radius

    def draw(self, display:pygame.display) -> None:
        pass

    def move(self, cord:Vector2) -> None:
        pass
    
        