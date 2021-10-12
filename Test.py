import pygame
import os
pygame.init()                                       #initialize the screen
Size = 600      
screen = pygame.display.set_mode([Size,Size])

backgroundImage = pygame.image.load(os.path.join("Resources","road.png"))   # Initializes the road background
background = pygame.transform.scale(backgroundImage,(Size*2,Size))

carImage = pygame.image.load(os.path.join("resources","car.png"))     #Initialize the Car
Car = pygame.transform.scale(carImage,(75,110))  
Car.set_colorkey((255,255,255))
Car.convert_alpha()

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
    y += 1
    
    
pygame.quit()