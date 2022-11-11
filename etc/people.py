import pygame
  
class People(pygame.sprite.Sprite):
  
    ''' this class creates the rectangle and allows us to add an imagine inside of the rectangle and positions it in the center. We created a group to draw the sprites. Differnt images will be applied for each file'''

  def __init__ (self,width,height,pos_x,pos_y,color):
   self.image = pygame.Surface([width,height])
   self.image.fill(color)
   self.rect = self.image.get_rec()
   self.rect.center = [pos_x,pos_y]
  
  def introduce_self(self)
  print("Hi, my name is" + self.name)
