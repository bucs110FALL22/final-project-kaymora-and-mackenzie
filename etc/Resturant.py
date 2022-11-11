import pygame

class Resturant_1(pygame.sprite.Sprite): 
  ''' this class creates the rectangle and allows us to add an imagine inside of the rectangle and positions it in the center. We created a group to draw the sprites.'''
 def __init__ (self,width,height,pos_x,pos_y,color):
   self.image = pygame.Surface([width,height])
   self.image.fill(color)
   self.rect = self.image.get_rec()
   self.rect.center = [pos_x,pos_y]


#Setup
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

resturant = Resturant_1(30,30,-50,30,"Blue")

resturant_group = pygame.sprite.Group()
resturant_group.add(resturant)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    
  pygame.display.flip()
  resturant_group.draw(screen)