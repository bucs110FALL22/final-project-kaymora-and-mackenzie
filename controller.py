import pygame 

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Button")
main_font = pygame.font.SysFont("arial", 50)

class Button():
  def __init__(self, image, pos, text_input, font, base_color, hovering_color):
      '''Allows the class initializes the object's attributes. '''
      self.image = image
      self.x_pos = pos[0]
      self.y_pos = pos[1]
      self.font = font
      self.base_color, self.hovering_color = base_color, hovering_color
      self.text_input = text_input
      self.text = self.font.render(self.text_input, True, self.base_color)
      if self.image is None:
        self.image = self.text
      self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
      self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

  def on_screen(self,screen):
    '''Puts the button image on the screen. Uses position of rect to place the button.'''
    if self.image is not None:
      screen.blit(self.image, self.rect)
    screen.blit(self.text, self.text_rect)

  def check(self, position):
    '''Checks if the position of the mouse is in the bounds of the coordinates of the button  '''
   
    if position [0] in range (self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
       return True
    else:
     return False

  def hover(self, position): 
    '''Allows the button to change color when the user's mouse hovers above it'''
  
    if position[0] in range(self.rect.left, self.rect.right ) and position[1] in range (self.rect.top, self.rect.bottom):
      self.text = self.font.render(self.text_input, True, self.hovering_color)
    else:
      self.text = self.font.render(self.text_input, True, self.base_color)
      
 
   
pygame.display.update()
                                                                                        
                                                                                        

                                                                                      
                                                                                      
                                                                                      