import pygame
import random

pygame.init()
SPRITE_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 1
BG_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 2

blue= pygame.Color("blue")
LightBlue = pygame.Color("lightblue")
DarkBlue = pygame.Color("darkblue")
Yellow = pygame.Color("yellow")
Magenta = pygame.Color("magenta")
Orange = pygame.Color("orange")
White = pygame.Color("white")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]), random.choice([-1,1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BG_COLOUR_CHANGE_EVENT))

    def colour_change(self):
        self.image.fill(random.choice([ Yellow, Magenta, Orange, White]))

def colour_change_bg():
    global bg_colour
    bg_colour = random.choice([blue, LightBlue, DarkBlue])

all_sprites_list = pygame.sprite.Group()

sp1= Sprite(White, 20, 25)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 371)
all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Sprite Colour Change on Boundary Hit")
bg_color =  blue
screen.fill(bg_color)

exit=False
clock = pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit=True
        elif event.type == SPRITE_COLOUR_CHANGE_EVENT:
            sp1.colour_change()
        elif event.type == BG_COLOUR_CHANGE_EVENT:
            colour_change_bg()

    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()

    clock.tick(240)
pygame.quit()


