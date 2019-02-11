from turtle import *

me = Turtle()

me.color("red")
me.pensize(6)
me.speed(7)
me.shape("turtle")

def DrawTri():
	for x in range(3):
		me.forward(100)
		me.left(120)

def DrawWheel():
	for x in range(12):
		DrawTri()
		me.left(30)

DrawWheel()




mainloop()