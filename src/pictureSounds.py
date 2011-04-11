'''
Created on Mar 20, 2011

@author: pyridoxus
'''

import sys, pygame
from clickables import ClickableObject
from objectList import objectList

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
        self.__objectSize = 128, 128
        self.__objectSpacing = 16
        self.__initObjects()
        self.__xBase = 0
        self.__yBase = 0
        self.__xEnd = 0
        self.initPositions()
        
        
    def __initObjects(self):
        '''
        Init the object list.
        '''
        allSprites = pygame.sprite.RenderUpdates()
        ClickableObject.containers = allSprites
        imageDirectory = "/home/pyridoxus/workspace/pyPictureSounds/images/"
        soundDirectory = "/home/pyridoxus/workspace/pyPictureSounds/sounds/"

        for image, sound in objectList:
            clicker = ClickableObject("%s%s" % (imageDirectory, image),
                                      "%s%s" % (soundDirectory, sound),
                                      self.__objectSize)
            self.__objects.append(clicker)
        
        
    def initPositions(self):
        '''
        Setup the object's positions
        '''
#    int rows, columns, index, x, y;
        index = 0
        rows = self.__size[1] / (self.__objectSize[1] + self.__objectSpacing)
        columns = len(self.__objects) / rows + 1
        self.__xBase = self.__size[0] / 2 - \
            (((self.__objectSize[0] + self.__objectSpacing) * columns) - \
             self.__objectSpacing) / 2
        self.__yBase = self.__size[1] / 2 - \
                (((self.__objectSize[1] + self.__objectSpacing) * rows) - \
                 self.__objectSpacing) / 2
        self.__xEnd = self.__xBase
        for b in range(rows):
            y = self.__yBase + (self.__objectSize[1] + self.__objectSpacing) * b
            for a in range(columns):
                self.__objects[index].setRow(b)
                self.__objects[index].setDir(b % 2)
                x = self.__xBase + a * (self.__objectSize[0] + \
                                        self.__objectSpacing)
                self.__objects[index].setXY(x, y)
                index += 1
                if index == len(self.__objects):
                    b = rows
                    break
        if x > self.__xEnd:
            self.__xEnd = x + self.__objectSize[0] + self.__objectSpacing
#    }
#    return;
        
    def loop(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.__screen.fill(self.__black)
            for ob in self.__objects:
                ob.drawIcon(self.__screen)
            pygame.display.flip()
        
game = Game()
game.loop()