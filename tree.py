import turtle

def tree(a,length,short,angel):
	if length > 5:

		a.forward(length)
		new_len = length - short

		a.left(angel)
		tree(a,new_len,short,angel)

		a.right(angel*2)
		tree(a,new_len,short,angel)

		a.left(angel)
		a.backward(length)

t = turtle.Turtle()
t.color("blue")
t.hideturtle()
t.speed(99999)
t.setheading(90)

tree(t, 50, 5, 20)
turtle.mainloop()