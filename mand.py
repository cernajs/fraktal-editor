iterr = 100
def mandel(c):
	z = 0
	for fin in range(iterr):
		z = z*z + c
		if abs(z) > 2:
			return fin
	return iterr

for i in range(-100,100):
	print([i , mandel(i)])