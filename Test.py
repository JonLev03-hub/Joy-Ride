import pygame
import os

from pygame.constants import K_1, K_SPACE
pygame.init()                                       #initialize the screen
Size = 600      
screen = pygame.display.set_mode([Size,Size])

clock = pygame.time.Clock()         #initialize a clock for FPS cap
FPS = 30                            #Set FPS cap

backgroundImage = pygame.image.load(os.path.join("Resources","road.png"))   # Initializes the road background
background = pygame.transform.scale(backgroundImage,(Size*2,Size))

carImage = pygame.image.load(os.path.join("resources","car.png"))     #Initialize the Car
Car = pygame.transform.scale(carImage,(75,110))  
Car.set_colorkey((255,255,255))
Car.convert_alpha()

debug = False
Velocity = 0
y = 0                                               # initialize the y value for the background            
running = True                                      # Sets the game as running
while running :                             

    for event in pygame.event.get():                # If the player closes the window it ends the script
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0-Size/2,y))                   # Set the background
    screen.blit(background,(0-Size/2,y - Size))
    screen.blit(Car,(305,300))
    pygame.display.update()

    if y > Size:                        #reset the background cordinates
        y = 0

    pressed_keys = pygame.key.get_pressed()     # Detects user input to move forward instead of just move
    if pressed_keys[pygame.K_SPACE] and Velocity < 20:
        Velocity += .5
    elif Velocity > 3:
        Velocity -=.45
    Velocity = float("{0:.2f}".format(Velocity))
    y += Velocity



    clock.tick(FPS) 
    print(Velocity)                           #sets the FPS Cap
             
pygame.quit()