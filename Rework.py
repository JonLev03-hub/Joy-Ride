import pygame

import os


# pygame.init()                                                       # initializing pygame

size = 600                                                          # declaring screen size
screen = pygame.display.set_mode([size,size])                       # initialize the screen
cars = {}                                                           # initialize a list for all the cars
car_image_1 = pygame.image.load(os.path.join("Resources", "car.png"))   # Create car one image
car_1 = pygame.transform.scale(car_image_1,(75,110))

car_1.set_colorkey((255,255,255))                        # sets the color key and removes the white background for car one
car_1.convert_alpha()

Player = {                                                          # Create the car players car
    "top_speed" : 20,
    "acceleration" : .3,
    "drag" : .5,
    "health" : 30,
    "x" : 305,
    "y" : 300,
    "speed" : 0,
    "handling" : .5,
    "image" : "car_1"
}

class car :
    def __init__ (self,top_speed,acceleration,drag,health,x,y,speed,handling,car) : # create a car object that has the attribues a car needs
        self.direction = -1         # (negitive is up positive is down)                               
        self.top_speed = top_speed*self.direction                    
        self.acceleration = acceleration*self.direction           
        self.health = health                                       
        self.drag = drag                                           
        self.x = x                                              
        self.y = y                                                
        self.speed = speed*self.direction                                                                        
        self.car = car                                             

    def update(self) :                                       # update the position of the car and movement speeds

        if  self.y > size :                                   # deletes thec ar when its off the screen
            cars.remove(self)
            """ initialize a new car here"""

        elif self.speed < self.top_speed :                            # checks if the car is at top speed
            self.speed += self.acceleration                                  # move the car forward based off the velocity

        elif self.speed >= 0 :                                       # checks if the car needs to slow down
            self.speed -= self.drag                                     # slows the car down
        else :
            self.speed = 0                                            # makes sure that the cars dont go backwards based off drag

        self.y -= Player["speed"] - self.speed                      # sets back the position based off the players movement and car speed        
      
        screen.blit(self.car,self.x,self.y)                         # place the car on the screen


for x in range(10-len(cars)):
    cars[x] = car(20,.3,.5,20,305,300,0,0.5,car_1)

    print(cars[x].speed)

# # ###########################################################################################################################################
# # user = car(20,.3,.5,20,305,300,"car.png")


# from pygame.constants import K_1, K_SPACE
# pygame.init()                                       #initialize the screen
# size = 600      
# screen = pygame.display.set_mode([size,size])

# clock = pygame.time.Clock()         #initialize a clock for FPS cap
# FPS = 30                            #Set FPS cap
# carx = 305
# cary = 300
# backgroundImage = pygame.image.load(os.path.join("Resources","road2.png"))   # Initializes the road background
# background = pygame.transform.scale(backgroundImage,(size,size))

# carImage = pygame.image.load(os.path.join("resources","car.png"))     #Initialize the Car
# Car = pygame.transform.scale(carImage,(75,110))  
# Car.set_colorkey((255,255,255))
# Car.convert_alpha()

# bottleImage = pygame.image.load(os.path.join("resources", "Bottle.png"))
# Bottle = pygame.transform.scale(bottleImage,(40,40))
# Bottle.set_colorkey((255,255,255))
# Bottle.convert_alpha()

# debug = False
# Velocity = 0                                    # Allows the code to have a velocity and acceleration 
# y = 0                                               # initialize the y value for the background            
# running = True                                      # Sets the game as running



# ##################################################################################################################################
# while running :                             

#     for event in pygame.event.get():                # If the player closes the window it ends the script
#         if event.type == pygame.QUIT:
#             running = False

#     screen.blit(background,(0,y))                   # Set the background 
#     screen.blit(background,(0,y - size))  
#     screen.blit(Car,(carx,cary))
#     screen.blit(Bottle,(210,0+y))
#     pygame.display.update()

#     if y > size:                        #Replaces the intersection once your twice the distance of the road
#         y = 0




#     pressed_keys = pygame.key.get_pressed()                # Detects user input to move forward instead of just move
#     if pressed_keys[pygame.K_w] and Velocity < 20:      #this block also moves the map according to the velocity and has a drag and acceleration aspect
#         Velocity += .3
#     elif Velocity > 0: 
#         Velocity -=.5
#     else :
#         Velocity = 0
#     Velocity = float("{0:.2f}".format(Velocity))
#     y += Velocity


#     if pressed_keys[pygame.K_a] and carx > 5 :              # Car x position based of player input and speed of car
#         carx -= .75*Velocity
#     elif pressed_keys[pygame.K_d] and 520 > carx : 
#         carx += .75*Velocity



#     clock.tick(FPS) 
#     print(Velocity)                           #sets the FPS Cap
             
# pygame.quit()