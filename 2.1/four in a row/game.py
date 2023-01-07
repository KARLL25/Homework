import pygame, sys, pygame_menu 1
from tkinter import *
from tkinter import messagebox
 
pygame.init()
 
 
class Chip(): # Класс для рисования фишек на поле
    
    def __init__(self, x, y):
        self.color = WHITE
        self.rect = (x, y, 65, 65)
 
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
 
class Button(): # Создаем кнопки для меню

    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
 
    def draw(self, screen, text, rect_color, border_color):
        border = 2
        pygame.draw.rect(screen, rect_color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, border_color, (self.x + border, self.y + border, self.width - border*2, self.height - border*2))
        screen.blit(text, (self.x + self.width / 6, self.y + self.height / 7))
 
def vertical_win(column):
        cubes = 0
        for i in range(len(column) - 1):
                        if column[i].color == RED and column[i+1].color == RED or column[i].color == YELLOW and column[i+1].color == YELLOW:
                            cubes += 1
                        if cubes == 3:
                            winner = column[i].color
                            Tk().wm_withdraw()
                            messagebox.showinfo('Result', f"{column[i].color} is a winner")
                            return False
     
def horisontal_win(chips):
    cubes = 0
    for i in range(len(chips) - 1):
        for j in range(len(chips[i])):
            if chips[i][j].color == RED and chips[i + 1][j].color == RED or chips[i][j].color == YELLOW and chips[i+1][j].color == YELLOW:
                cubes +=1
            if cubes == 6:
                winner = chips[i + 1][j].color
                Tk().wm_withdraw()
                messagebox.showinfo('Result', f"{chips[i + 1][j].color} is a winner")
                return False
 
                
            
 
size = (650, 425)
screen = pygame.display.set_mode(size)
    
YELLOW = 'yellow'
WHITE = 'white'
BLACK = 'black'
RED = 'red'
 
my_font = pygame.font.SysFont('monospace', 42)
my_font_2 = pygame.font.SysFont('monospace', 24)
 
pygame.display.set_caption("4 в ряд")
clock = pygame.time.Clock()
 
rows = [5, 75, 145, 215, 285, 355]
columns = [5, 75, 145, 215, 285, 355]
 
chips = [[Chip(x, y) for y in columns] for x in rows]
 
def run_game():
    turn = 0
    run = True
    rows_of_objects = [[],[],[],[],[],[]]
    while run:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                (posx,posy) = pygame.mouse.get_pos()
                rows.append(posx)
                rows.sort()
                column_num = rows.index(posx) - 1
                rows.remove(posx)
 
                if menu_button.x < posx < menu_button.x + menu_button.width and menu_button.y < posy < menu_button.y + menu_button.height:
                    run = False
 
                if column_num >= 0 and posx < rows[column_num] + 70:
                    column = chips[column_num]
                    row = column[column_num]
                    
                    for chip in column[::-1]:
                        if chip.color == WHITE:
                            if turn == 0:
                                chip.color = RED
                            else:
                                chip.color = YELLOW
                            turn = 1 - turn
                            break
                    vertical_win(column)
                    horisontal_win(chips)
                
                   
                    
        screen.fill(BLACK)
 
        for i in chips:
            for chip in i:
                chip.draw(screen)
        
        menu_button = Button(150, 65, 495, 355)
        quit_text = my_font.render('Menu', True, WHITE)
        menu_button.draw(screen, quit_text, WHITE, BLACK)
        
        pygame.display.flip()
 
 
def finish_game():
    pygame.quit()
    sys.exit()
 
 
menu = pygame_menu.Menu('4 в ряд', 650, 425, theme = pygame_menu.themes.THEME_DARK)
menu.add.button('Play', run_game)
menu.add.button('Quit', finish_game)
menu.mainloop(screen)
