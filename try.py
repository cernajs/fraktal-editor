import turtle

def rect(t,loop,length,angel):
	for _ in range(3):
		t.forward(length)

		if loop > 1:
			rect(t,loop-1,length/2,-angel)

		t.right(angel)
	t.forward(length)
	t.right(angel)



t = turtle.Turtle()
t.hideturtle()
rect(t,6,150,90)
t.color("black")
turtle.mainloop()

