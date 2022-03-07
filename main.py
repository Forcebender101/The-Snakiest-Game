import turtle
import random
import time

#variables
delay = 0.1
segments = []
score = 0
highscore = 0

#movement
def move():
    if head.direction == "up":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y + 20)
 
    elif head.direction == "down":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y - 20)
 
    elif head.direction == "right":
        x = head.xcor() #x coordinate of the turtle
        head.setx(x + 20)
 
    elif head.direction == "left":
        x = head.xcor() #x coordinate of the turtle
        head.setx(x-20)


#define Directions
def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"


#set up the screen
win = turtle.Screen()
win.title("Kalgi's snake game")
win.bgcolor("blue")
win.setup(width=600,height=600)
win.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"

# keyboard bindings
win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color("red")
food.penup()
food.shapesize(0.5,0.5)
food.goto(0,0)

 #set up high score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)




#Main game loop
while True:
  win.update()
  time.sleep(delay)
  if head.distance(food) < 15:
    #move food
    x = random.randint(-290,290)
    y = random.randint(-290,290)
    food.goto(x,y)
    #add a new segment
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape('square')
    new_segment.color('grey')
    new_segment.penup()
    segments.append(new_segment)
    #move the segments in reverse order
    score = score + 1 
  for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x,y)
  #move segment 0 to where the head is
  if len(segments) > 0:
    x=head.xcor()
    y=head.ycor()
    segments[0].goto(x,y)
  move()
  if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
    time.sleep(1)
    head.goto(0,0)
    head.direction = 'stop'
    #hide segments
    for segment in segments:
      segment.goto(1000,1000)

    #clear segment list
    segments = []

    #reset score
    score = 0
  #check for head collisions
  for segment in segments:
    if segment.distance(head) < 20:
      time.sleep(1)
      #reset score
      score = 0
      head.goto(0,0)
      head.direction = 'stop'
      #hide segments
      for segment in segments:
        segment.goto(1000,1000)
  
      #clear segment list
      segments = []
      #reset score
      score = 0
          
  #write score
  if score > highscore:
    highscore = score
  pen.write("Score:" + str(score) + '\n High Score:' + str(highscore))

  