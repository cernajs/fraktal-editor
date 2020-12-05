import turtle

def circle(turtle,n):
	while n < 200:
		turtle.circle(n)
		n += 2

t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")
circle(t,5)
turtle.mainloop()