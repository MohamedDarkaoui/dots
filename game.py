import pygame
from pygame.locals import *
from entity import *

NUMBER_OF_DOTS = 4



def drawEntities(entities : list, screen):
    for i in entities:
        pygame.draw.circle(screen, i.color ,(i.position.get_cartesian_coordinates()), 5)


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1500, 800))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    entities = createEntities(NUMBER_OF_DOTS) 

    while 1:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        pygame.time.wait(10)
        screen.fill((0,0,0))
        mouse_press = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        mouse = Entity(Position(0,0), Vector(0))
        mouse.position.set_polar_coordinates(mouse_pos[0],mouse_pos[1])

        if mouse_press[0]:
            entities[0].follows(mouse)
        else:
            entities[0].follows(entities[1])

        drawEntities(entities, screen)

        for entity in entities:
            entity.update()


        pygame.display.update()


if __name__ == '__main__': main()