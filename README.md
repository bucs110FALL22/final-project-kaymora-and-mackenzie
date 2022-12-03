:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
#  Dine Before You Try 
## CS 110 Final Project
### << Fall, 2022 >>
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

 [repl](https://replit.com/join/lcptmiceqz-mackenziegoodl3) 

<< [link to demo presentation slides](#) >>

### Team:  Mackenzie and Kaymora
####  Team Members: Mackenzie Goodluck and Kaymora Roberts

***

## Project Description


Our website, "Dine Before You Try", will allow users to get a feel of the restaurant before they go. Users can fill out their interests, where they can then get recommendations on different restaurants and cafes. They can also search by location, so no matter if the user is in Paris, Greece, or Jamaica they will be able to dine to their preferences. Users can also create an avatar that can visit the restaurants for them before they decide to go. 

***    

## User Interface Design

- **Initial Concept**
  - A program that allows users to get recommendations for popular and new restaurants in their home city. 
- 
    
    
- **Final GUI**
  -The Final GUI Screen Shots are FINALGUI SCREENSHOTS folder
  

***        

## Program Design

* Non-Standard libraries
    * N/A
      
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
    * class Controller - Allows for the start and quit buttons to operate in the main menu. Once the user clicks on start, it takes them to the dropdown page where they can choose a city to search for restaurants. 
    * class Button - Allows creating the image, position, hovering color, base color, text font, and text input to
    * class DropDown - Allowed for the dropdown to change colors when hovered over
    * 
Reponse:
The only library used is pygame.
## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * << n/a >>
* assets
    * aatl1.png
    * asea1.png
    * atli1.png
    * CLASSDIAGRAM.pdf
    * font.ttf
    * italy1.png
    * italysea1.png
    * jamatl1.png
    * jerk1.png
    * jsea1.png
    * kine1.png
    
* etc
    * milestone2.md
    * milestone3.md
    * README.md

***

## Tasks and Responsibilities 

   * We sat together and did the whole program. Mackenzie and Kaymorah though of ways on how the program then worked together on cfreating and fixing the bugs in program.
   * 

## Testing

* We wrote a large amount of code, ran it, located the bugs, fixed them, and made them more specific to our program.  

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run the Program      |GUI window appears with the start page. 
                                                Displays a start button and a back button
|
|  2                   |click the start button| program displays a dropdown of available 
                                                cities.  allows the user to click back.
                                                
   3                   | click a desired city | program displays three restaurants in the 
                                                city of choice along with the 
                                                restaurant's address, phone number, and 
                                                featured meals with prices. Users have the                                                                   ability to use the back button to go back                                                                    to the previous page. 