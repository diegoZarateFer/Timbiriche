import pygame as pg
from settings import *
from Dot import *

class Cell:
    def __init__(self,dots):
        self.dots = dots
        self.lines = [False,False,False,False]
        self.turns = [' ',' ',' ',' ']
        self.completed = False
        self.completed_by = ' '

    def update(self,current_player):
        if not self.lines[0] and self.dots[0].used[1] and self.dots[1].used[3]:
            self.lines[0] = True
            self.turns[0] = current_player
            if sum(self.lines) == len(self.lines):
                self.completed = True
                self.completed_by = current_player
                return True

        elif not self.lines[1] and self.dots[1].used[2] and self.dots[2].used[0]:
            self.lines[1] = True
            self.turns[1] = current_player
            if sum(self.lines) == len(self.lines):
                self.completed = True
                self.completed_by = current_player
                return True
                
        elif not self.lines[2] and self.dots[2].used[3] and self.dots[3].used[1]:
            self.lines[2] = True
            self.turns[2] = current_player
            if sum(self.lines) == len(self.lines):
                self.completed = True
                self.completed_by = current_player
                return True

        elif not self.lines[3] and self.dots[3].used[0] and self.dots[0].used[2]:
            self.lines[3] = True
            self.turns[3] = current_player
            if sum(self.lines) == len(self.lines):
                self.completed = True
                self.completed_by = current_player
                return True
        return False

    def draw_text(self,surf,text,size,x,y,color):
        font = pg.font.Font(font_name,size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        surf.blit(text_surface,text_rect)

    def draw(self,screen):

        # Drawing square.
        if self.completed:
            square = pg.Rect(self.dots[0].x,self.dots[0].y,DISTANCE_BETWEEN_DOTS + 2 * RADIUS,DISTANCE_BETWEEN_DOTS + 2 * RADIUS)
            if self.completed_by == 'A':
                pg.draw.rect(screen,PLAYER_A_COLOR,square)
                self.draw_text(screen,'A',TEXT_SIZE,self.dots[0].x + (DISTANCE_BETWEEN_DOTS + 2 * RADIUS) // 2,self.dots[0].y + (DISTANCE_BETWEEN_DOTS + 2 * RADIUS) // 2 - TEXT_SIZE // 2,BLACK)
            else:
                pg.draw.rect(screen,PLAYER_B_COLOR,square)
                self.draw_text(screen,'B',TEXT_SIZE,self.dots[0].x + (DISTANCE_BETWEEN_DOTS + 2 * RADIUS) // 2,self.dots[0].y + (DISTANCE_BETWEEN_DOTS + 2 * RADIUS) // 2 - TEXT_SIZE // 2,BLACK)

        # Drawing lines
        for i in [0,1,2,3]:
            if self.lines[i]:
                j = (i + 1) % 4
                if self.turns[i] == 'A':
                    pg.draw.line(screen,PLAYER_A_LINE_COLOR,(self.dots[i].x,self.dots[i].y),(self.dots[j].x,self.dots[j].y),WIDTH_LINE)
                else:
                    pg.draw.line(screen,PLAYER_B_LINE_COLOR,(self.dots[i].x,self.dots[i].y),(self.dots[j].x,self.dots[j].y),WIDTH_LINE)
