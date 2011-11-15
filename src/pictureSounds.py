'''
Created on Mar 20, 2011

@author: pyridoxus
'''

import sys, pygame
from clickables import (ClickableObject, Interface)
from objectList import (objectList, BLACK)
from time import sleep

class Game(object):
    '''
    Main game object.
    '''
    def __init__(self):
        '''
        Setup the game.
        '''
        pygame.init()
        self.__size = 1280, 1024
#        self.__size = 1920, 1080
        self.__screen = pygame.display.set_mode(self.__size)
#        self.__screen = pygame.display.set_mode(self.__size,
#                    pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
        #print pygame.display.list_modes()
        self.__objects = []
        self.__interface = Interface(0, 0, [128, 128], 16)
        self.__initObjects()
        self.__yBase = 0
        self.initPositions()
        
        
    def __initObjects(self):
        '''
        Init the object list.
        '''
        allSprites = pygame.sprite.RenderUpdates()
        ClickableObject.containers = allSprites
        imageDirectory = "../images/"
        soundDirectory = "../sounds/"

        n = 0
        for image, sound in objectList:
            clicker = ClickableObject("%s%s" % (imageDirectory, image),
                                      "%s%s" % (soundDirectory, sound),
                                      self.__interface, n)
            n += 1
            self.__objects.append(clicker)
        print len(self.__objects)
        
        
    def initPositions(self):
        '''
        Setup the object's positions
        '''
        index = 0
        spacing = self.__interface.getSpacing()
        objectSize = self.__interface.getSize()
        rows = int(self.__size[1] / (objectSize[1] + spacing))
        columns = len(self.__objects) / rows + 1
        print rows, columns
        xBase = self.__size[0] / 2 - (((objectSize[0] + spacing) * columns) - \
                                        spacing + objectSize[0]) / 2
        self.__yBase = self.__size[1] / 2 - (((objectSize[1] + spacing) * \
                                              rows) - spacing) / 2
        xEnd = xBase
        for b in range(rows):
            y = self.__yBase + (objectSize[1] + spacing) * b
            for a in range(columns):
                self.__objects[index].setRow(b)
                d = [-1, 1][b % 2]
                self.__objects[index].setDir(d)
                x = xBase + a * (objectSize[0] + \
                                        spacing)
                self.__objects[index].setXY(x, y)
                print "(%d, %d)" % (x, y), xEnd
                index += 1
                if x > xEnd:
                    xEnd = x
                if index == len(self.__objects):
                    b = rows
                    break
            
        self.__interface.setLeft(xBase)
        self.__interface.setRight(xEnd)
            

    def loop(self):
        while(True):
            mouseLocation = (-1000, -1000)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouseLocation = pygame.mouse.get_pos()
                elif event.type == pygame.KEYDOWN:
                    sys.exit()
            pygame.event.clear()
            self.__screen.fill(BLACK)
            for ob in self.__objects:
                if ob.isClicked(mouseLocation):
                    ob.expandAndPlaySound(self.__screen, self.__size)
                ob.drawIcon(self.__screen)
            pygame.display.flip()
            sleep(0.05)
        
game = Game()
game.loop()