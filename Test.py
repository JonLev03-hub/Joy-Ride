import pygame
import os

from pygame.constants import K_1, K_SPACE
pygame.init()                                       #initialize the screen
Size = 600      
screen = pygame.display.set_mode([Size,Size])

backgroundImage = pygame.image.load(os.path.join("Resources","road.png"))   # Initializes the road background
background = pygame.transform.scale(backgroundImage,(Size*2,Size))

carImage = pygame.image.load(os.path.join("resources","car.png"))     #Initialize the Car
Car = pygame.transform.scale(carImage,(75,110))  
Car.set_colorkey((255,255,255))
Car.convert_alpha()

debug = False
y = 0                                               # initialize the y value for the background             # Tracks keys pressed
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
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_SPACE] :
        y += 2
             
pygame.quit()