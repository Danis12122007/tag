import pygame
import random


class Board:
    # defining a basic values
    def __init__(self):
        self.cell_x = None
        self.cell_y = None
        self.width = 4
        self.height = 4
        self.board = [[-1] * self.width for _ in range(self.height)]
        numbers_list = [str(i + 1) for i in range(15)]
        numbers_list.append(' ')
        random.shuffle(numbers_list)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(i * 4 + j)
                self.board[i][j] = str(numbers_list[i * 4 + j])
        self.left = 10
        self.top = 10
        self.cell_size = 70

    # redefining a value of top and left side and cell size set during init method
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # showing board to screen
    def render(self):
        screen.fill((0, 0, 0))
        for y in range(self.height):
            for x in range(self.width):
                print('draw')
                pygame.draw.rect(screen,
                                 'white',
                                 (x * self.cell_size + self.left,
                                  y * self.cell_size + self.top,
                                  self.cell_size,
                                  self.cell_size),
                                 3)
                font = pygame.font.SysFont('Arial', 50)
                text = font.render(str(self.board[y][x]), True, 'white')
                screen.blit(text, (x * self.cell_size + self.left + 3, y * self.cell_size + self.top + 3))

    # showing the modified cell
    def on_click(self):
        change = None
        try:
            if self.board[self.cell_y][self.cell_x - 1] == ' ':
                change = (self.cell_y, self.cell_x - 1)
        except IndexError:
            pass
        try:
            if self.board[self.cell_y][self.cell_x + 1] == ' ':
                change = (self.cell_y, self.cell_x + 1)
        except IndexError:
            pass
        try:
            if self.board[self.cell_y - 1][self.cell_x] == ' ':
                change = (self.cell_y - 1, self.cell_x)
        except IndexError:
            pass
        try:
            if self.board[self.cell_y + 1][self.cell_x] == ' ':
                change = (self.cell_y + 1, self.cell_x)
        except IndexError:
            pass

        if change:
            self.board[change[0]][change[1]], self.board[self.cell_y][self.cell_x] = \
                self.board[self.cell_y][self.cell_x], self.board[change[0]][change[1]]

        self.render()

    # receiving cell where user clicked
    def get_click(self, mouse_pos):
        self.get_cell(mouse_pos)
        if 0 <= self.cell_x < self.width and 0 <= self.cell_y < self.height:
            self.on_click()

    # receiving cell where user clicked
    def get_cell(self, mouse_pos):
        self.cell_x = (mouse_pos[0] - self.left) // self.cell_size
        self.cell_y = (mouse_pos[1] - self.top) // self.cell_size
        print([self.cell_x, self.cell_y])


class Main(Board):
    pass


if __name__ == '__main__':
    pygame.init()
    size = w, h = (400, 300)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Пятнашки')
    icon = pygame.image.load('pic/game_icon.jpg')
    pygame.display.set_icon(icon)
    app = Main()
    app.render()
    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                app.get_click(pygame.mouse.get_pos())
                pygame.display.update()
