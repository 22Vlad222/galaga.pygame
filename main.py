from random import randint,choice
import pygame as pg

class Rocket(pg.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = rocket_img
        self.rect = rocket_img.get_rect()
        self.rect.y = height*0.8
        self.rect.x = weight*0.4

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -=5
        if keys[pg.K_RIGHT]:
            self.rect.x +=5

class Star():
    def __init__(self):
        self.x = randint(0, height)
        self.y = randint(0, weight)
        self.rad = 1
        self.speed = randint(1,3)
    def draw(self):
        pg.draw.circle(win,white, (self.x, self.y), self.rad)

    def move(self):
        self.y += self.speed
        if self.y >= height:
            self.y = 0


class Stone(pg.sprite.Sprite):
    def __init__(self, image, *group):
        super().__init__(*group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, int(weight * 0.8))
        self.rect.y = randint(-height, 0)
        self.speed = randint(2,3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= height:
            self.rect.y = 0
            self.rect.x = randint(0, weight)

def score_and_background():
    win.fill(black)



def move_and_draw_all_sprites():
    player_group.draw(win)
    player_group.update()

    for star in stars:
        star.draw()
        star.move()

    stones.draw(win)
    stones.update()

def collision():
    if pg.sprite.groupcollide(stones, player_group, True, True):
        exit()


height = 500
weight = 500

black = (0, 0, 0)
white = (255, 255, 255)
win = pg.display.set_mode((weight, height))
pg.display.set_caption("Galaga")
clock = pg.time.Clock()

rocket_img = pg.image.load("rocket.png")
rocket_img = pg.transform.scale(rocket_img, (50, 100))
stones_img = [ pg.image.load(f"rock{i}.png") for i in range(0, 3) ]
stones_img = [pg.transform.scale(elem, (40,40)) for elem in stones_img]

stars = [Star() for i in range(50)]


player_group = pg.sprite.Group()
player = Rocket()
player_group.add(player)


stones = pg.sprite.Group()
for i in range(5):
    Stone(choice(stones_img), stones)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    score_and_background()
    move_and_draw_all_sprites()
    collision()
    pg.time.delay(10)
    pg.display.update()
