'''
Created on Mar 20, 2011

@author: pyridoxus
'''

import sys, pygame
from clickables import ClickableObject

pygame.init()
size = width, height = 640,480
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
ball = pygame.image.load("/home/pyridoxus/workspace/pyPictureSounds/"
                         "images/ball.gif")
ballrect = ball.get_rect()
#while 1:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            sys.exit()
#    ballrect = ballrect.move(speed)
#    if ballrect.left < 0 or ballrect.right > width:
#        speed[0] = -speed[0]
#    if ballrect.top < 0 or ballrect.bottom > height:
#        speed[1] = -speed[1]
#    screen.fill(black)
#    screen.blit(ball, ballrect)
#    pygame.display.flip()

def loop():
    allSprites = pygame.sprite.RenderUpdates()
    ClickableObject.containers = allSprites
    clicker = ClickableObject("/home/pyridoxus/workspace/"
                              "pyPictureSounds/images/frog.bmp",
                              "/home/pyridoxus/workspace/"
                              "pyPictureSounds/sounds/FROG.WAV", size)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(black)
        clicker.draw(screen)
        pygame.display.flip()
        
loop()