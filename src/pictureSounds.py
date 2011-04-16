'''
Created on Mar 20, 2011

@author: pyridoxus
'''

import sys, pygame
from clickables import (ClickableObject, Interface)
from objectList import objectList
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
        self.__size = 640,480
        self.__speed = [2, 2]
        self.__black = 0, 0, 0
        self.__screen = pygame.display.set_mode(self.__size)
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
        imageDirectory = "/home/pyridoxus/workspace/pyPictureSounds/images/"
        soundDirectory = "/home/pyridoxus/workspace/pyPictureSounds/sounds/"

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
#    int rows, columns, index, x, y;
        index = 0
        spacing = self.__interface.getSpacing()
        objectSize = self.__interface.getSize()
        rows = self.__size[1] / (objectSize[1] + spacing)
        columns = len(self.__objects) / rows + 1
        xBase = self.__size[0] / 2 - \
            (((objectSize[0] + spacing) * columns) - \
             spacing) / 2
        self.__yBase = self.__size[1] / 2 - \
                (((objectSize[1] + spacing) * rows) - \
                 spacing) / 2
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
                print "(%d, %d)" % (x, y)
                index += 1
                if index == len(self.__objects):
                    b = rows
                    break
        if x > xEnd:
            xEnd = x + objectSize[0] + spacing
            
        self.__interface.setLeft(xBase)
        self.__interface.setRight(xEnd)
            
#    }
#    return;
        
    def loop(self):
        while(True):
            mouseLocation = (-1000, -1000)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouseLocation = pygame.mouse.get_pos()
            pygame.event.clear()
            self.__screen.fill(self.__black)
            for ob in self.__objects:
                if ob.isClicked(mouseLocation):
                    ob.playSound()
                ob.drawIcon(self.__screen)
            pygame.display.flip()
        
game = Game()
game.loop()