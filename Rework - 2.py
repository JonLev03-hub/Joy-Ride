import pygame
import random
import os

# personal formatting -- regular variables are all lower case, constant variables are 
# done in all caps, and words are seperated by _
# add constant varaibels
FPS = 30
SCREEN_SIZE = 600
CAR_CAP = 6
IMAGES = {                  # configure all images as their name and dimensions to load
    "background" : (SCREEN_SIZE,SCREEN_SIZE),
    "car1" : (75,110),
    "bottle" : (40,40),
}
debug = False
# add dynamic variables
objects = {}
running = False
# configure the screen instance and clock instance 
pygame.init()
screen = pygame.display.set_mode ([SCREEN_SIZE,SCREEN_SIZE])
clock = pygame.time.Clock()
# configure the background 
# initialize all images
for image in IMAGES.keys() : 
    png = pygame.image.load(os.path.join("Resources", f"{image}.png"))
    IMAGES[image] = pygame.transform.scale(png,IMAGES[image])
    IMAGES[image].set_colorkey((255,255,255))
    IMAGES[image].convert_alpha()

# define classes for all the objects with functions to update the object
class car :                
    def __init__ (self,top_speed,acceleration,drag,health,x,y,speed,image) :
        self.direction = -1                                
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
    #Update the position of the car based on speed and palyer speed    
    def update(self) :                                       
        if running == True : 
            if  self.y > SCREEN_SIZE or self.y < - SCREEN_SIZE and random.randomrange(1,100) > 10 :   
                spawn_location = None
                test_spot = random.randrange(10,520)
                def spawn() : 
                    for hitbox in 
                              
                self.__init__(random.randrange(5,15),random.uniform(.1,.2),random.uniform(.4,.5),50,random.randrange(10,520),-SCREEN_SIZE,0,"car1")
                self.speed = self.top_speed

            elif self.speed < self.top_speed :                          
                self.speed += self.acceleration                                  

            elif self.speed > 0 :                                      
                self.speed -= self.drag                                
            else :
                self.speed = 0                                            

            self.y += objects[player]["speed"] - self.speed                      

# Create the starting objects inside a nested dictionary
objects["player"] = car(20,.3,30,1,305,300,10,"car1")
objects["player"].sobriety = 100

objects["cars"] = {}
for x in range(CAR_CAP-len(objects["cars"])) :
    objects["cars"][x] = car(random.randrange(5,15),random.uniform(.1,.2),random.uniform(.4,.5),50,random.randrange(10,520),random.randint(-600,-100),0,IMAGES["car1"])
# when running for object in dictionary update the object
# when running for object in dictionary write the object on the screen
# update the screen
