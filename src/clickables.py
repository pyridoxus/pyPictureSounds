'''
Created on Mar 27, 2011

@author: pyridoxus
'''
import pygame
from objectList import (BLACK, ANIMATIONFRAMES)
from time import sleep

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
        self.__xa = 0
        self.__ya = 0
        self.__wa = 0
        self.__ha = 0
        self.__xao = 0
        self.__yao = 0
        self.__wao = 0
        self.__hao = 0
        
        
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
    
                
    def playSound(self):
        '''
        Play the sound in this object.
        '''
        self.__sound.play()
        sleep(self.__sound.get_length())

        
    def drawIcon(self, bmp):
        '''
        Draw the iconic version of the image at the object's coordinates.
        '''
        self.__x += self.__dir
        right = self.__interface.getRight() + self.__interface.getSize()[0] + \
                    self.__interface.getSpacing()
        if self.__x < self.__interface.getLeft() and self.__dir == -1:
            self.__x = self.__interface.getRight() + \
                        self.__interface.getSize()[0] + \
                        self.__interface.getSpacing() 
            self.__rect = self.__icon.get_rect()
            self.__rect = self.__rect.move(self.__x, self.__y)
        elif self.__x > right and self.__dir == 1:
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


    def expandAndPlaySound(self, bmp, size):
        '''
        Expand the image to full screen and play the sound.
        Shrink the image back to icon size when sound is over.
        '''
        xs, ys = self.__rect.topleft    # Starting dimensions of image
        imageRect = self.__image.get_rect()
        w = imageRect.w
        h = imageRect.h
        r = float(w) / float(h)     # image ratio width to height
        xe = (size[0] - w) / 2      # initialize the final position
        ye = (size[1] - h) / 2      # initialize the final position
    
        if xe < 0:
            xe = 0
            w = size[0]
            h = int((float(w) / r))
            ye = (size[1] - h) / 2
        if ye < 0:
            ye = 0
            h = size[1]
            w = int(r * float(h))
            xe = (size[0] - w) / 2
    
#        //set up frame variables at beginning of position and size
        self.__xa = float(xs)
        self.__ya = float(ys)
        self.__wa = float(self.__rect.w)
        self.__ha = float(self.__rect.h)
    
#        //set up frame offsets
        self.__xao = float(xe - xs) / float(ANIMATIONFRAMES)
        self.__yao = float(ye - ys) / float(ANIMATIONFRAMES)
        self.__wao = float(w - self.__rect.w) / float(ANIMATIONFRAMES)
        self.__hao = float(h - self.__rect.h) / float(ANIMATIONFRAMES)
        self.__animate(bmp)
#    //    while(!keypressed());
#        return;
        
        
    def __grow(self, bmp, d):
        '''
        Grow (or shrink) the image. d=1 to grow, d=-1 to shrink.
        Must grow first, then call this function again to shrink.
        '''
        for a in range(ANIMATIONFRAMES):
            temp = pygame.transform.smoothscale(self.__image,
                                                (int(self.__wa),
                                                 int(self.__ha)))
            tempRect = temp.get_rect()
            tempRect = tempRect.move(self.__xa, self.__ya)
            bmp.fill(BLACK)
            bmp.blit(temp, tempRect)
            pygame.display.flip()
            self.__xa += self.__xao * d
            self.__ya += self.__yao * d
            self.__wa += self.__wao * d
            self.__ha += self.__hao * d

    
    def __animate(self, bmp):
        '''
        Animate the growth of the object.
        '''
        self.__grow(bmp, 1)
        sleep(0.5)
        self.playSound()
        sleep(0.5)
        self.__grow(bmp, -1)
