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
        self.__sound.play()
        self.__rect = self.__image.get_rect()
        self.__x = 0
        self.__y = 0
        self.__dir = 1
        self.__size = size
        self.__image = pygame.transform.smoothscale(self.__image, self.__size)
        
        
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
