#fox and rabbits

import turtle
import random
import math

maxX=240
maxY=240
plants = []
free_turtles = []
free_rabbits = []

#Calculates Distance between two points
#Expects a tuple like turtle.pos()
def calculateDistance(pt1, pt2):
     x1 = pt1[0]
     y1 = pt1[1]
     x2 = pt2[0]
     y2 = pt2[1]

     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist

#initalizes the food
#you could combine this with foxes and rabbits
def place_plant(obj_turtle):
    x = random.randint(-maxX,maxX)
    y = random.randint(-maxY,maxY)

    obj_turtle.penup()
    obj_turtle.color('green')
    obj_turtle.shape('circle')
    #make the food smaller
    obj_turtle.shapesize(0.5,0.5,0.5) #default is 1,1,1
    obj_turtle.goto(x,y)

def seed_plants(num_plants):
    global maxX
    global maxY
    global plants

    for i in range(num_plants):
        plants.append(turtle.Turtle())

    for plant in plants:
        place_plant(plant)

def init_rabbit(r):
    r.reset()
    r.health = 100
    r.age = 0
    #After rabbits mate they can't mate again until cooldown < 0
    r.cooldown = 10
    r.dead = False
    r.sex = random.choice(['M','F'])
    if(r.sex == 'F'):
        r.color('pink')
    else:
        r.color('blue')
    r.penup()
    return r

def create_rabbit():
    r= turtle.Turtle()
    return init_rabbit(r)

def draw_square(obj_turtle, x=0, y=0, size=10,  bg_color='red'):
    obj_turtle.penup()
    c = obj_turtle.color()
    obj_turtle.goto(x,y)
    obj_turtle.setheading(180)
    obj_turtle.pendown()
    obj_turtle.color(bg_color)
    for ii in range(0,4):
        obj_turtle.fd(size*2)
        obj_turtle.lt(90)
    obj_turtle.penup()
    obj_turtle.color(c[0],c[1])

def main():
    global maxX
    global maxY

    fd_speed = 5
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.tracer(0)

    num_plants =  50
    num_rabbits = 4
    max_rabbits = 24
    #num_foxes

    seed_plants(num_plants)

    #Create Rabbits
    rabbits = []
    for ii in range(0,num_rabbits):
        rabbit = create_rabbit()
        rabbit.penup()
        x = random.randint(-1*maxX,maxX)
        y = random.randint(-1*maxY,maxY)
        rabbit.goto(x,y)
        rabbits.append(rabbit)

    #Draw a border around active area
    #rabbit.color() returns a tuple (c1, c2)
    #I only want one color so I choose c1
    draw_square(rabbits[0], maxX, maxY, maxX,'red' )

    #Move the rabbits
    rabbits_alive = True
    while rabbits_alive ==  True: #this needs to get turned into a function
        screen.tracer(0)
        rabbits_alive = False
        for rabbit in rabbits:
            if(rabbit.dead == False):
                #rabbit.dx = random.randint(-5,5)
                #rabbit.dy = random.randint(-5,5)
                rabbit.da = random.randint(-15,15)
                rabbit.rt(rabbit.da)

                #Look for food
                for plant in plants:
                    distance_to_plant = calculateDistance(rabbit.pos(),plant.pos())
                    plant.color('green')
                    if(abs(rabbit.towards(plant) - rabbit.heading() ) < 45 \
                       and distance_to_plant < 25*fd_speed):
                        #rabbit sees a plant
                        rabbit.setheading(rabbit.towards(plant.xcor(), plant.ycor()))
                        #rabbit.color('green')
                        plant.color('red')

                        #Eat Food
                        if(distance_to_plant <= fd_speed):
                            plants.remove(plant)
                            free_turtles.append(plant)
                            rabbit.health += 50
                            #rabbit.color('red')
                            plant.reset()
                            #print('Plants left' + str(len(plants))+ ':' + str(len(screen.turtles())))

                        break
                    else:
                        #rabbit.color('blue')
                        pass

                rabbit.fd(fd_speed)

                #Check Boundry conditions.
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

                rabbit.health -= 1
                rabbit.age += 1
                rabbit.cooldown -=1

                if rabbit.health > 0:
                    rabbits_alive = True
                    if(rabbit.age < 50):
                        #Have rabbits grow until they are age 100
                        rabbit_size = rabbit.age/40
                        rabbit.shapesize(rabbit_size,rabbit_size,rabbit_size) #default is 1,1,1
                else:
                    #Rabbit died
                    if rabbit.dead == False:
                        rabbit.color('gray')
                        rabbit.write('   ' + rabbit.sex + ': Rabbit starved to death at age:' + str(rabbit.age))
                        rabbit.dead=True
                        free_rabbits.append(rabbit)
                        rabbits.remove(rabbit)

                #Check if rabbits have babies
                for r in rabbits:
                    if(calculateDistance(rabbit.pos(), r.pos()) <= 15 \
                       and r.sex != rabbit.sex \
                       and r.cooldown < 0 \
                       and rabbit.cooldown < 0):
                        rabbit.cooldown = 15
                        r.cooldown = 15
                        if(len(rabbits) <= max_rabbits):
                            baby_rabbit = create_rabbit()
                        else:
                            try:
                                baby_rabbit = free_rabbits.pop(1)
                                baby_rabbit = init_rabbit(baby_rabbit)

                            except:
                                pass

                        baby_rabbit.goto(r.xcor(),r.ycor())
                        print(str(len(rabbits)) + '           --->'+ 'Baby Rabbit' + \
                              str(r.age) + ':' +  str(rabbit.age))
                        rabbits.append(baby_rabbit)

            #Grow Food
            if random.randint(0,500) > 499:
                try:
                    new_plant = free_turtles.pop(1)
                    place_plant(new_plant)
                    plants.append(new_plant)
                except:
                    pass


        screen.update()


    screen.update()
    turtle.done()

if __name__ == "__main__":
   main()
