"""

import turtle

iterations = 3
startLen = 200

turtle.up()
turtle.setpos(-startLen*3/2, startLen*3/2/2)

turtle.speed(0)

koch = "FRFRF"

for _ in range(iterations):
	koch = koch.replace("F", "FLFRFLF")

turtle.down()
"""
#turtle.color("red")
#turtle.begin_fill()
"""
for move in koch:
	if move == "F":
		turtle.forward(startLen/(3 ** (iterations-1)))
	elif move == "R":
		turtle.right(120)
	elif move == "L":
		turtle.left(60)

turtle.hideturtle()
#turtle.end_fill()
turtle.mainloop()

"""

import turtle

import matplotlib.pyplot as plt

from math import pi, cos, sin
radians = pi/180

iterations = 8
startLen = 200
"""
turtle.up()
turtle.setpos(-startLen*3/2, startLen*3/2/2)

turtle.speed(0)
"""
koch = "FRFRF"

for _ in range(iterations):
	koch = koch.replace("F", "FLFRFLF")

#turtle.down()
"""
#turtle.color("red")
#turtle.begin_fill()

for move in koch:
	if move == "F":
		turtle.forward(startLen/(3 ** (iterations-1)))
	elif move == "R":
		turtle.right(120)
	elif move == "L":
		turtle.left(60)
"""

def plot_cor(cords):
	"""
	plt.axis("off")
	plt.axes().set_aspect("equal", "datalim")
	"""
	x,y = zip(*cords)
	plt.plot(x,y)

def coordinates_of_turtle_move(commands, rangle=120, langle=60):
	start = (0.0, 0.0, 60.0)
	yield (0.0, 0.0)

	for com in commands:
		x, y, angle = start

		if com == "F":
			start = (x - cos(angle * radians),
					 y + sin(angle *radians),
					 angle)

			yield(start[0],start[1])

		elif com == "R":
			start = (x,y, angle+rangle)

		elif com == "L":
			start = (x,y, angle-langle)

#seq zančí počáteční string a transform určuje pravidla pro pokrok
def L_system_transform(seq, transform):
	return "".join(transform.get(i, i) for i in seq)


plot_cor(coordinates_of_turtle_move(koch))
plt.show()

#turtle.hideturtle()
#turtle.end_fill()
#turtle.mainloop()
