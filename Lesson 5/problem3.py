from turtle import *

me = Turtle()

me.color("red")
me.pensize(6)
me.speed(7)
me.shape("turtle")

def DrawHex():
	for x in range(6):
		me.forward(100)
		me.left(60)

DrawHex()

mainloop()