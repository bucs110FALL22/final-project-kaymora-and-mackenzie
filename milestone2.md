CS110: Milestone II
Final Project Outline
At this point, you should start planning your program structure and interface.
Set Up Project Channel
1. Go to Discord
2. Your Team channel (found here), 
3. Paste a link to your Final Project repo in the chat.
Structure
Each class is a model of some real world object. We often refer to data classes as the models in a GUI program. Your models show the logical structure of your application data, including the relationships and constraints that determine how data can be stored and accessed. Each model is represented by a class that you can instantiate (create new objects). 

In this milestone you will design the data models for your final project. Models only represent the state of the data you will need to represent in your GUI. 

Your Models must not have any GUI components in them other than positioning and image data. 

For example, if you are creating a space invaders type of game:
 You would need a class to represent the ship, which could contain:
the image filename (str), 
location of the ship (x and y coordinates)
methods to update position
method to shoot
To describe the class interface, you could write: 
class Ship
attributes:
x
y
image
methods
move_right()
move_left()
shoot()

1. Copy and paste the milestone 2 template below to a file called 'milestone2.md' . 
2. Place the file in your final project repository folder: /etc
3. Add the requested information to the file 

milestone 2 template
======================================================================

# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

class Resturant_1: 
def __init__ (self,name,color)
    self.name = name 
    self.color = color 
    self.position = position 
    set.match = none 
    
def set_position = position 
  penup()
  self.position = setposition(-50,30)

def __final__(self)
  result_final = f"{self.name}[{self.type}]"
  result_final += f"{self.name}[{self.type}]"
  return result_final

def main()
  greecerest = Resturant_1("Greek restaurant", "blue")
  greecerest.set_match()
  print(greecerest)
main()

## Class Interface 2

class Box_1:

  def __init__(self,name,font)
  self.name = name 
  self.font = font 

  def main()
    interests = Box_1("Interests", "italic")
    
## Class Interface 3

class People:
  def introduce_self(self)
  print("Hi, my name is" + self.name

  p1 = customer()
  p1.name = "Sydney" 
  p1.color = "red"

  p2 = waiter()
  p2.name = "Jesse"
  p2.color = "Green"

  p1.introduce_self()
  p2.introduce_self()
< add your interface >

======================================================================
