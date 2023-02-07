import pygame as pg
from Dot import *

class Cell:
    def __init__(self,dots):
        self.dots = dots
        self.lines = [False,False,False,False]
    
    def update(self):
        if self.dots[0].used[1] and self.dots[1].used[3]:
            self.lines[0] = True
        if self.dots[1].used[2] and self.dots[2].used[0]:
            self.lines[1] = True
        if self.dots[2].used[3] and self.dots[3].used[1]:
            self.lines[2] = True
        if self.dots[3].used[0] and self.dots[0].used[2]:
            self.lines[3] = True

    def draw(self,screen):
        for i in [0,1,2,3]:
            if self.lines[i]:
                j = (i + 1) % 4
                pg.draw.line(screen,BLACK,(self.dots[i].x,self.dots[i].y),(self.dots[j].x,self.dots[j].y))
