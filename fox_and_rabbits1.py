#fox and rabbits

import turtle
import random
import math

maxX=240
maxY=240
plants = []

def calculateDistance(pt1, pt2):
     x1 = pt1[0]
     y1 = pt1[1]
     x2 = pt2[0]
     y2 = pt2[1]
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist

#initalizes the food
#you could combine this with foxes and rabbits
def seed_plants(num_plants):
    global maxX
    global maxY
    global plants

    for i in range(num_plants):
        plants.append(turtle.Turtle())

    for plant in plants:
        x = random.randint(-maxX,maxX)
        y = random.randint(-maxY,maxY)

        plant.penup()
        plant.color('green')
        plant.shape('circle')
        #make the food smaller
        plant.shapesize(0.5,0.5,0.5) #default is 1,1,1
        plant.goto(x,y)

#plants grow over time
#def grow():

#seeking behavior towards rabbits
#def foxes():

#seeks plants, runs from foxes
#def rabbits():
#I'm still fuzzy on how to get functions to interact
#rabbit.health() = 100
#if it eats a plant
#rabbit.health() += 25 or whatever
#if rabbit.health() == 0:
#    death


#def run():


def fox_and_rabbits():
    global maxX
    global maxY

    fd_speed = 5
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.tracer(0)

    num_plants =  50
    #num_rabbits
    #num_foxes

    seed_plants(num_plants)

    #Create Rabbit
    rabbit = turtle.Turtle()
    rabbit.penup()
    rabbit.health = 100

    #Draw a border around active area
    rabbit.goto(maxX,maxY)
    rabbit.setheading(180)
    rabbit.pendown()
    rabbit.color('red')
    for ii in range(0,4):
        rabbit.fd(maxX*2)
        rabbit.lt(90)

    rabbit.color('blue')

    rabbit.penup()
    x = random.randint(-1*maxX,maxX)
    y = random.randint(-1*maxY,maxY)
    rabbit.goto(x,y)
    while rabbit.health >= 0: #this needs to get turned into a function
        screen.tracer(0)
        rabbit.dx = random.randint(-5,5)
        rabbit.dy = random.randint(-5,5)
        rabbit.da = random.randint(-10,10)
        rabbit.rt(rabbit.da)

        #Look for food
        for plant in plants:
            distance_to_plant = calculateDistance(rabbit.pos(),plant.pos())
            plant.color('green')
            if(abs(rabbit.towards(plant) - rabbit.heading() ) < 45 \
               and distance_to_plant < 25*fd_speed):
                #rabbit sees a plant
                rabbit.setheading(rabbit.towards(plant.xcor(), plant.ycor()))
                rabbit.color('green')
                plant.color('red')

                if(distance_to_plant <= fd_speed):
                    plants.remove(plant)
                    rabbit.health += 50
                    rabbit.color('red')
                    plant.reset()
                    print('Plants left' + str(len(plants))+ ':' + str(len(screen.turtles())))

                break
            else:
                rabbit.color('blue')

        rabbit.fd(fd_speed)

        #rabbit.setx(rabbit.xcor() + rabbit.dx)
        #rabbit.sety(rabbit.ycor() + rabbit.dy)

        if rabbit.ycor() < -maxX:
            rabbit.sety(-maxX) #prevents it from going out of bounds
            rabbit.da = 180 - rabbit.heading()
            rabbit.rt(rabbit.da)
        elif rabbit.ycor() > maxY:
            rabbit.sety(maxY)
            rabbit.da = 90 - rabbit.heading()
            rabbit.rt(rabbit.da)
        if rabbit.xcor() > maxX:
            rabbit.setx(maxX)
            rabbit.da = 270 + rabbit.heading()
            rabbit.rt(rabbit.da)
        elif rabbit.xcor() < -maxY:
            rabbit.setx(-maxY)
            rabbit.da = 90 + rabbit.heading()
            rabbit.rt(rabbit.da)
        screen.update()

        rabbit.health -= 1
        print('Rabbit Health=' + str(rabbit.health))

    #Rabbit died
    rabbit.color('gray')
    rabbit.write('Rabbit starved to death')
    screen.update()
    turtle.done()

if __name__ == "__main__":
    fox_and_rabbits()
