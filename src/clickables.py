'''
Created on Mar 27, 2011

@author: pyridoxus
'''
import pygame

class Interface(object):
    '''
    Interface between the ClickableObjects and the game loop.
    '''
    def __init__(self, left, right, size, spacing):
        '''
        Setup internals.
        '''
        self.__left = left
        self.__right = right
        self.__size = size
        self.__spacing = spacing
        
        
    def setLeft(self, x):
        '''
        Set the left-most coordinate.
        '''
        self.__left = x
        
        
    def getLeft(self):
        '''
        Return the left-most coordinate.
        '''
        return self.__left
    
    
    def setRight(self, x):
        '''
        Set the right-most coordinate.
        '''
        self.__right = x
        
        
    def getRight(self):
        '''
        Return the right-most coordinate.
        '''
        return self.__right
    
    
    def getSize(self):
        '''
        Return the size of the icons.
        '''
        return self.__size
    
    
    def getSpacing(self):
        '''
        Return the spacing size between icons.
        '''
        return self.__spacing
    
    

class ClickableObject(pygame.sprite.Sprite):
    '''
    This is a clickable image with associated sound effect.
    '''
    def __init__(self, imageFile, soundFile, interface, n):
        '''
        Set up the object with the image and the sound.
        '''
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.__image = pygame.image.load(imageFile)
        self.__sound = pygame.mixer.Sound(soundFile)
#        self.__sound.play()
        self.__x = 0
        self.__y = 0
        self.__row = None
        self.__dir = 1
        self.__interface = interface
        self.__icon = pygame.transform.smoothscale(self.__image,
                                            (self.__interface.getSize()[0],
                                             self.__interface.getSize()[1]))
        self.__rect = self.__icon.get_rect()
        self.n = n
        
        
    def setRow(self, row):
        '''
        Set the row position for this object.
        '''
        self.__row = row
        
        
    def setXY(self, x, y):
        '''
        Set the x,y coordinates for this object.
        '''
        self.__x = x
        self.__y = y
        self.__rect = self.__rect.move(x, y)
        
        
    def setDir(self, d):
        '''
        Set direction of image movement.
        '''
        self.__dir = d


    def isClicked(self, mouseLocation):
        '''
        Return true if the mouse is inside this icon.
        '''
        return self.__rect.collidepoint(mouseLocation)
    
                
    def drawIcon(self, bmp):
        '''
        Draw the iconic version of the image at the object's coordinates.
        '''
        self.__x += self.__dir
        if self.__x < self.__interface.getLeft() and self.__dir == -1:
            self.__x = self.__interface.getRight() + \
                        self.__interface.getSize()[0] + \
                        self.__interface.getSpacing() 
            self.__rect = self.__icon.get_rect()
            self.__rect = self.__rect.move(self.__x, self.__y)
        elif self.__x > self.__interface.getRight() and self.__dir == 1:
            self.__rect = self.__icon.get_rect()
            self.__x = self.__interface.getLeft()
            self.__rect = self.__rect.move(self.__x, self.__y)
        else:
            self.__rect = self.__rect.move(self.__dir, 0)
        bmp.blit(self.__icon, self.__rect)
        
        
    def draw(self, bmp):
        '''
        Draw the image.
        '''
        self.__x += self.__dir * 2
        self.__y += self.__dir * 2
        temp = pygame.transform.smoothscale(self.__image,
                                            (self.__interface.getSize()[0] -\
                                             self.__y,
                                             self.__interface.getSize()[1] -\
                                             self.__y))
        self.__rect.move_ip(self.__dir, self.__dir)
        if self.__y >= self.__interface.getSize()[1]:
            self.__dir = -1
        if self.__y <= 0:
            self.__dir = 1
#        print self.__x, self.__y
        bmp.blit(temp, self.__rect)
