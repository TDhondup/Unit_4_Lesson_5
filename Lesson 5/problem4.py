from turtle import *

me = Turtle()

me.color("red")
me.pensize(6)
me.speed(7)
me.shape("turtle")

def DrawHex(side):
	for x in range(6):
		me.forward(side)
		me.left(60)

DrawHex(50)
DrawHex(75)
DrawHex(100)
DrawHex(125)
DrawHex(150)
DrawHex(175)






mainloop()