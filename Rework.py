import pygame
import os
import random 


pygame.init()                                                       # initializing pygame

size = 600                                                          # declaring screen size
screen = pygame.display.set_mode([size,size])                       # initialize the screen

background = pygame.image.load(os.path.join("Resources","road2.png"))   # Initializes the road background
background = pygame.transform.scale(background,(size,size))
background_pos = 0

clock = pygame.time.Clock()         #initialize a clock for FPS cap
FPS = 30                            #Set FPS cap

bottleImage = pygame.image.load(os.path.join("resources", "Bottle.png"))            # creates the bottle images
Bottle = pygame.transform.scale(bottleImage,(40,40))
Bottle.set_colorkey((255,255,255))                                                  # removes the bottle background
Bottle.convert_alpha()

cars = {}                                                           # initialize a list for all the cars
car_cap = 5

car_image_1 = pygame.image.load(os.path.join("Resources", "car_image_1.png"))   # Create car one image
car_1 = pygame.transform.scale(car_image_1,(75,110))
car_1.set_colorkey((255,255,255))                        # removes the bottle background
car_1.convert_alpha()

player = {                                                          # Create the car players car
    "top_speed" : 20 ,
    "acceleration" : .3,
    "drag" : 1,
    "health" : 30,
    "x" : 305,
    "y" : 300,
    "speed" : 0,
    "handling" : .5,
    "image" : car_1,
    "type" : "car",
    "width" : 75,
    "height" : 110
    }

class car :                  # create a car object that has the attribues a car needs
    def __init__ (self,top_speed,acceleration,drag,health,x,y,speed,image) :
        self.direction = -1         # (negitive is up positive is down)                               
        self.top_speed = top_speed                    
        self.acceleration = acceleration           
        self.health = health                                       
        self.drag = drag                                           
        self.x = x                                              
        self.y = y                                                
        self.speed = speed                                                                      
        self.image = image  
        self.width = 75
        self.height = 110

    def update(self) :                                       # update the position of the car and movement speeds

        if  self.y > size or self.y < - size :                                   # deletes thec ar when its off the screen
            self.__init__(random.randrange(5,15),random.uniform(.1,.2),random.uniform(.4,.5),50,random.randrange(10,520),random.randint(-600,-100),0,car_1)
            self.speed = self.top_speed

        elif self.speed < self.top_speed :                            # checks if the car is at top speed
            self.speed += self.acceleration                                  # move the car forward based off the velocity

        elif self.speed > 0 :                                       # checks if the car needs to slow down
            self.speed -= self.drag                                     # slows the car down
        else :
            self.speed = 0                                            # makes sure that the cars dont go backwards based off drag

        self.y += player["speed"] - self.speed                      # sets back the position based off the players movement and car speed        
      
        screen.blit(self.image,(self.x,self.y))                         # place the car on the screen

for x in range(car_cap - len(cars)) : 
    cars["car" + str(x)] = car(random.randrange(5,15),random.uniform(.1,.2),random.uniform(.4,.5),50,random.randrange(10,520),random.randint(-600,-100),0,car_1)
    cars["car" + str(x)].speed = cars["car" + str(x)].top_speed
"""Create a script that spawns cars in the top of the map with random statistics"""
print(len(cars))
running = True                                      # Sets the game as running
debug = False
while running :                             

    for event in pygame.event.get():                # If the player closes the window it ends the script
        if event.type == pygame.QUIT:
            running = False
  
    if background_pos > size:                           # Update the background 
        background_pos = 0
    screen.blit(background,(0,background_pos))                   #Placing the screen background
    screen.blit(background,(0,background_pos - size))

    """Update the items"""
    
    for car in cars :                                               # Place all car objects and updating them
        cars[car].update()
        print(f"updated{car}")

    pressed_keys = pygame.key.get_pressed()                # identify player inputs
    if pressed_keys[pygame.K_w] and player['speed'] < player["top_speed"]:          #increase speed of the player based off inputs
        player["speed"] += player["acceleration"]                                   # also rounds speed
    elif player["speed"] > 0: 
        player["speed"] -= player["drag"]
    else :
        player["speed"] = 0
    player["speed"] = float("{0:.2f}".format(player["speed"]))

    background_pos += player["speed"]                       # Updates background based off player speed

    if pressed_keys[pygame.K_a] and player["x"] > 5 :              # Car x position based of player input and speed of car
        player["x"] -= player["handling"] * player["speed"]
    elif pressed_keys[pygame.K_d] and 520 > player["x"] : 
        player["x"] += player["handling"] * player["speed"]

    screen.blit(player["image"],(player["x"],player["y"]))            # place player



    clock.tick(FPS)                             #sets the FPS Cap

    pygame.display.update()         
pygame.quit()