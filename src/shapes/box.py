import pygame
from ..utils import Vector2


class Box(pygame.Rect):
    def __init__(self, cord:Vector2, width:int, height:int) -> None:
        super.__init__(self)
        self.cord = cord
        self.width = width
        self.height = height

    def draw(self, display:pygame.display):
        pass

    def move(self, cord:Vector2):
        pass