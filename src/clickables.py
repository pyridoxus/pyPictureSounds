'''
Created on Mar 27, 2011

@author: pyridoxus
'''
import pygame

class ClickableObject(pygame.sprite.Sprite):
    '''
    This is a clickable image with associated sound effect.
    '''
    def __init__(self, imageFile, soundFile, size):
        '''
        Set up the object with the image and the sound.
        '''
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.__image = pygame.image.load(imageFile)
        self.__sound = pygame.mixer.Sound(soundFile)
#        self.__sound.play()
        self.__rect = self.__image.get_rect()
        self.__x = 0
        self.__y = 0
        self.__row = None
        self.__dir = 1
        self.__size = size
        self.__icon = pygame.transform.smoothscale(self.__image,
                                            (self.__size[0],
                                             self.__size[1]))
        
        
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
        self.__icon.get_rect().topleft = x, y
        
        
    def setDir(self, d):
        '''
        Set direction of image movement.
        '''
        self.__dir = d
        
                
    def drawIcon(self, bmp):
        '''
        Draw the iconic version of the image at the object's coordinates.
        '''
        temp = self.__icon.get_rect()
        temp.move_ip(self.__dir, 0)
        bmp.blit(self.__icon, temp)
        
        
    def draw(self, bmp):
        '''
        Draw the image.
        '''
        self.__x += self.__dir * 2
        self.__y += self.__dir * 2
        temp = pygame.transform.smoothscale(self.__image,
                                            (self.__size[0] - self.__y,
                                             self.__size[1] - self.__y))
        self.__rect.move_ip(self.__dir, self.__dir)
        if self.__y >= self.__size[1]:
            self.__dir = -1
        if self.__y <= 0:
            self.__dir = 1
#        print self.__x, self.__y
        bmp.blit(temp, self.__rect)
