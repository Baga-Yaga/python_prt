import turtle

def clk():
    import page2

z = turtle.Turtle()
z.shapesize(2,2)
z.color('cyan')
z.pensize(10)
z.shape('turtle')
turtle.bgcolor('black')
turtle.setup(700,500,startx=400,starty=150)
turtle.onclick(clk,btn=1,add=None)

z.penup()
z.backward(190)
z.left(90)
z.forward(190)
z.pendown()
z.speed(0)

def e ():
    z.forward(30)
    z.backward(30)
    z.right(90)
    z.forward(30)
    z.left(90)
    z.forward(20)
    z.backward(20)
    z.right(90)
    z.forward(30)
    z.left(90)
    z.forward(30)

def o ():
    for i in range(2):
        z.forward(30)
        z.left(90)
        z.forward(60)
        z.left(90)

# W
z.right(180)
z.forward(60)
z.left(135)
z.forward(30)
z.right(90)
z.forward(30)
z.left(135)
z.forward(60)

# E
z.penup()
z.right(90)
z.forward(20)
z.pendown()

e()

#L
z.penup()
z.forward(20)
z.pendown()
z.forward(30)
z.backward(30)
z.left(90)
z.forward(60)

#C
z.penup()
z.right(90)
z.forward(50)
z.pendown()
z.forward(30)
z.backward(30)
z.right(90)
z.forward(60)
z.left(90)
z.forward(30)

#O
z.penup()
z.forward(20)
z.pendown()
o()

#M
z.penup()
z.forward(50)
z.pendown()
z.left(90)
z.forward(60)
z.right(135)
z.forward(30)
z.left(90)
z.forward(30)
z.right(135)
z.forward(60)

#E
z.penup()
z.left(90)
z.forward(20)
z.left(90)
z.forward(60)
z.right(90)
z.pendown()
e()

#T
z.penup()
z.right(90)
z.forward(60)
z.right(90)
z.forward(220)
z.pendown()
z.backward(40)
z.forward(20)
z.left(90)
z.forward(60)

#O
z.penup()
z.left(90)
z.forward(40)
z.pendown()
o()

#A
z.penup()
z.right(90)
z.forward(60)
z.right(90)
z.forward(220)
z.pendown()
z.left(70)
z.forward(70)
z.backward(70)
z.left(40)
z.forward(70)
z.backward(30)
z.right(110)
z.forward(25)

#U
z.penup()
z.right(125)
z.forward(40)
z.right(55)
z.forward(35)
z.pendown()
z.right(90)
z.forward(60)
z.left(90)
z.forward(40)
z.left(90)
z.forward(60)

#D
z.speed(0)
z.penup()
z.right(90)
z.forward(20)
z.pendown()
z.right(90)
z.forward(60)
z.left(90)
z.forward(10)
for a in range(95):
    z.left(1.9)
    z.fd(1)
z.forward(10)
# z.speed(7)

#I
z.penup()
z.right(0.5)
z.backward(50)
z.pendown()
z.backward(40)
z.forward(20)
z.left(90)
z.forward(60)
z.right(90)
z.forward(20)
z.backward(40)

#O
z.penup()
z.backward(20)
z.right(180)
z.pendown()
o()

#B
z.penup()
z.forward(50)
z.pendown()
# o()
# z.left(90)
# z.forward(30)
# z.right(90)
# z.forward(30)
# z.right(90)
# z.forward(30)
# z.left(90)
z.left(90)
z.forward(60)
z.right(90)
z.forward(15)
for a in range(45):
    z.right(4)
    z.fd(1)
z.forward(13)
z.right(180)
z.forward(17)
for a in range(45):
    z.right(4)
    z.fd(1)
z.forward(15)
z.left(180)
z.forward(22)

#oo
for a in range(2):
    z.penup()
    z.forward(20)
    z.pendown()
    o()
    z.forward(30)

#k
z.penup()
z.forward(20)
z.pendown()
z.left(90)
z.forward(60)
z.backward(30)
z.right(45)
z.forward(40)
z.backward(40)
z.right(90)
z.forward(40)
z.left(45)
z.forward(15)

a=0
turtle.bgcolor('black')
while a<4:
    z.left(90)
    z.speed(1)
    a = a + 1

# turtle.mainloop()
# turtle.hideturtle()
# turtle.clear()
import page2



