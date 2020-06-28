#fox and rabbits

import turtle
import random

#initalizes the food
#you could combine this with foxes and rabbits
def seed_plants(num_plants):
    plants = []

    for i in range(num_plants):
        plants.append(turtle.Turtle())

    for plant in plants:
        x = random.randint(-460,460)
        y = random.randint(-400,400)

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
    screen = turtle.Screen()
    screen.bgcolor('black')
    screen.tracer(0)

    num_plants = 20
    #num_rabbits
    #num_foxes

    seed_plants(num_plants)

    rabbit = turtle.Turtle()
    rabbit.penup()
    rabbit.color('blue')
    x = random.randint(-460,460)
    y = random.randint(-400,400)
    rabbit.goto(x,y)

    while True: #this needs to get turned into a function
        screen.tracer(0)
        rabbit.dx = random.randint(-5,5)
        rabbit.dy = random.randint(-5,5)
        rabbit.da = random.randint(-10,10)

        rabbit.rt(rabbit.da)
        rabbit.setx(rabbit.xcor() + rabbit.dx)
        rabbit.sety(rabbit.ycor() + rabbit.dy)

        if rabbit.ycor() < -400:
            rabbit.sety(-400) #prevents it from going out of bounds
            rabbit.dy *= -1
            rabbit.da = random.randint(-10,10)
            rabbit.rt(rabbit.da)
        elif rabbit.ycor() > 400:
            rabbit.sety(400)
            rabbit.dy *= -1
            rabbit.da = random.randint(-10,10)
            rabbit.rt(rabbit.da)
        if rabbit.xcor() > 460:
            rabbit.setx(460)
            rabbit.dx *= -1
            rabbit.da = random.randint(-15,15)
            rabbit.rt(rabbit.da)
        elif rabbit.xcor() < -460:
            rabbit.setx(-460)
            rabbit.dx *= -1
            rabbit.da = random.randint(-15,15)
            rabbit.rt(rabbit.da)
        screen.update()

    turtle.done()

if __name__ == "__main__":
    fox_and_rabbits()
