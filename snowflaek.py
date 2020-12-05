import turtle
def koch_curve(t, iterations, length, short, angle):
  if iterations == 0:
    t.forward(length)
  else:
    iterations -= 1
    length = length / short
    koch_curve(t, iterations, length, short, angle)
    t.left(angle)
    koch_curve(t, iterations, length, short, angle)
    t.right(angle * 2)
    koch_curve(t, iterations, length, short, angle)
    t.left(angle)
    koch_curve(t, iterations, length, short, angle)

t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")
for i in range(3):
  koch_curve(t, 4, 200, 3, 60)
  t.right(120)
turtle.mainloop()