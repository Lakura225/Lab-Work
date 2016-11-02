
lights = [0] * 50
i=0
while i <= 50:
	for count,light in enumerate(lights):
		i += 1
		if light == 0:
			lights[count] = 1
		elif light == 1:
			lights[count] = 0
