import pygame as pg
import sys
import random
# from main import Setup

pg.init()

SW, SH = 800, 800

# gridblock size
BLOCK_SIZE = 50

screen = pg.display.set_mode((SW, SH))
pg.display.set_caption("Snake!")
clock = pg.time.Clock()


class Snake:
    def __init__(self):
        # self.x = BLOCK_SIZE
        # self.y = BLOCK_SIZE
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.x_direction = 1
        self.y_direction = 0
        self.head = pg.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pg.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False
        # self.color = "green"

    def update(self):
        global apple

        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x = self.body[i+1].x
            self.body[i].y = self.body[i+1].y

        self.head.x += self.x_direction * BLOCK_SIZE
        self.head.y += self.y_direction * BLOCK_SIZE
        self.body.remove(self.head)

class Apple:
    def __init__(self):
        self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pg.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE )

    def update(self):
        pg.draw.rect(screen, "red", self.rect)



def draw_grid():
    for x in range(0,SW,BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pg.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pg.draw.rect(screen, "gray70", rect, 1)


draw_grid()

snake = Snake()
apple = Apple()

while True:
    keys = pg.key.get_pressed()
    # pg.fill("black")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    if keys[pg.K_ESCAPE]:
        break
    if keys[pg.K_s]:
        snake.x_direction = 0
        snake.y_direction = 1
    if keys[pg.K_w]:
        snake.x_direction = 0
        snake.y_direction = - 1

    if keys[pg.K_a]:
        snake.x_direction = - 1
        snake.y_direction = 0
    if keys[pg.K_d]:
        snake.x_direction = 1
        snake.y_direction = 0
    if keys[pg.K_SPACE]:
        snake.x_direction = 0
        snake.y_direction = 0

    snake.update()

    screen.fill("black")
    draw_grid()
    apple.update()

    pg.draw.rect(screen, "green", snake.head)

    for square in snake.body:
        pg.draw.rect(screen, "green", square)

    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pg.Rect(snake.head.x, snake.head.y, BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()



    pg.display.update()
    clock.tick(10)

