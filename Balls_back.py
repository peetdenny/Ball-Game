import pygame
import random
import math

myimage = pygame.image.load("Booloon.png")
imagerect = myimage.get_rect()

def initialise():
    pygame.init()
    size=(400,400)
    screen=pygame.display.set_mode(size)
    pygame.font.init()
    myimage.convert_alpha()
    return screen

def get_colour():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return pygame.Color (red, green, blue)



def render(screen, x, y, colour):
    screen.fill((226,226,226))
    pygame.draw.ellipse(screen, colour, [x, y, 50, 50], 0)
    screen.blit(myimage, (x, y))
    pygame.display.flip()


def run_game():
    screen = initialise()
    clock = pygame.time.Clock()
    carry_on = True
    x = 20
    y = 20
    y_direction = random.randint(1, 5)
    x_direction = random.randint(1, 6)
    c = get_colour()

    while carry_on:

        y = y + y_direction
        if(y > 350 or y < 0):
            y_direction = - y_direction
            c = get_colour()
        x = x + x_direction
        if(x > 350 or x < 0):
            x_direction = - x_direction
            c = get_colour()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                carry_on = False
                print("bye bye")
                break
        render(screen, x, y, c)
        clock.tick(60)

run_game()
