import pygame
import os
import random
from pygame.constants import K_1, K_SPACE
pygame.init()                                       #initialize the screen
Size = 600      
screen = pygame.display.set_mode([Size,Size])

clock = pygame.time.Clock()         #initialize a clock for FPS cap
FPS = 30                            #Set FPS cap
carx = 305
cary = 300
backgroundImage = pygame.image.load(os.path.join("Resources","road2.png"))   # Initializes the road background
background = pygame.transform.scale(backgroundImage,(Size,Size))

carImage = pygame.image.load(os.path.join("resources","car.png"))     #Initialize the Car
Car = pygame.transform.scale(carImage,(75,110))  
Car.set_colorkey((255,255,255))
Car.convert_alpha()

bottleImage = pygame.image.load(os.path.join("resources", "Bottle.png"))
Bottle = pygame.transform.scale(bottleImage,(40,40))
Bottle.set_colorkey((255,255,255))
Bottle.convert_alpha()

debug = False
Velocity = 0                                    # Allows the code to have a velocity and acceleration 
y = 0                                               # initialize the y value for the background            
running = True                                      # Sets the game as running



##################################################################################################################################
while running :                             

    for event in pygame.event.get():                # If the player closes the window it ends the script
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,y))                   # Set the background 
    screen.blit(background,(0,y - Size))  
    screen.blit(Car,(carx,cary))
    screen.blit(Bottle,(210,0+y))
    pygame.display.update()

    if y > Size:                        #Replaces the intersection once your twice the distance of the road
        y = 0




    pressed_keys = pygame.key.get_pressed()                # Detects user input to move forward instead of just move
    if pressed_keys[pygame.K_w] and Velocity < 20:      #this block also moves the map according to the velocity and has a drag and acceleration aspect
        Velocity += .3
    elif Velocity > 0: 
        Velocity -=.5
    else :
        Velocity = 0
    Velocity = float("{0:.2f}".format(Velocity))
    y += Velocity


    if pressed_keys[pygame.K_a] and carx > 5 :              # Car x position based of player input and speed of car
        carx -= .75*Velocity
    elif pressed_keys[pygame.K_d] and 520 > carx : 
        carx += .75*Velocity



    clock.tick(FPS) 
    print(Velocity)                           #sets the FPS Cap
             
pygame.quit()