from settings import *
from Dot import *
from Cell import *

class Board:
    def __init__(self):
        self.dot_is_clicked = False
        self.selected_dot = None
        self.dots = self.create_dots()
        self.cells = self.create_cells()
        self.mouse_listener = True

    def create_dots(self):
        dots = []
        y = BOARD_Y + RADIUS
        for i in range(ROWS):
            dots_row = []
            x = BOARD_X + RADIUS
            for j in range(DOTS_PER_ROW):
                dots_row.append(Dot(x,y))
                x += DISTANCE_BETWEEN_DOTS + 2 * RADIUS
            
            dots.append(dots_row)
            y += DISTANCE_BETWEEN_DOTS + 2 * RADIUS
        
        for row in range(ROWS):
            for col in range(DOTS_PER_ROW):
                for d in range(len(DIRECTIONS)):
                    (dr,dc) = DIRECTIONS[d]
                    new_row = row + dr
                    new_col = col + dc
                    if new_row >= 0 and new_row < ROWS and new_col >= 0 and new_col < DOTS_PER_ROW:
                        dots[row][col].adjacent_dots[d] = dots[new_row][new_col]
        return dots
    
    def create_cells(self):
        cells = []
        for row in range(ROWS - 1):
            cell_row = []
            for col in range(DOTS_PER_ROW - 1):
                list_of_dots = [self.dots[row][col],self.dots[row][col + 1],self.dots[row + 1][col + 1],self.dots[row + 1][col]]
                cell_row.append(Cell(list_of_dots))
            cells.append(cell_row)
        return cells

    def make_options(self):
        for i in range(len(self.selected_dot.adjacent_dots)):
            dot = self.selected_dot.adjacent_dots[i]
            if dot != None and not self.selected_dot.used[i]:
                dot.make_option()
            
    def unmake_options(self):
        for dot in self.selected_dot.adjacent_dots:
            if dot != None:
                dot.make_normal()

    def select_dot(self):
        for i in range(ROWS):
            for j in range(DOTS_PER_ROW):
                (x,y) = pg.mouse.get_pos()
                if self.dots[i][j].handle_left_click(x,y):
                    self.dot_is_clicked = True
                    self.selected_dot = self.dots[i][j]
                    self.make_options()

    def check_hover(self):
        # Checking hover of each dot
        for dots_row in self.dots:
            for dot in dots_row:
                [x,y] = pg.mouse.get_pos()
                dot.hover(x,y)
    
    def check_adjacent(self,x,y):
        opposite = {0:2,1:3,2:0,3:1}
        for i in range(len(self.selected_dot.adjacent_dots)):
            dot = self.selected_dot.adjacent_dots[i]
            if dot != None and dot.handle_left_click(x,y):
                dot.used[opposite[i]] = True
                self.selected_dot.used[i] = True
                self.dot_is_clicked = False
                self.selected_dot.make_normal()
                self.unmake_options()
                self.selected_dot = None
                return

    def update(self):
        self.check_hover()
        for cell_row in self.cells:
            for cell in cell_row:
                cell.update()
    
    def handle_events(self):
        if self.mouse_listener:
            mouse_clicked = pg.mouse.get_pressed()
            [x,y] = pg.mouse.get_pos()
            if mouse_clicked[0]:
                if self.dot_is_clicked:
                    self.check_adjacent(x,y)
                else:
                    self.select_dot()
                self.mouse_listener = False
            elif mouse_clicked[2]:
                if self.dot_is_clicked and self.selected_dot.handle_right_click(x,y):
                    self.unmake_options()
                    self.dot_is_clicked = False
                    self.selected_dot = None
                self.mouse_listener = False

    def draw(self,screen):
        for dots_row in self.dots:
            for dot in dots_row:
                dot.draw(screen)

        for cell_row in self.cells:
            for cell in cell_row:
                cell.draw(screen)