def lightss():
	lights = [0] * 50
	i=0
	n=0
	while i <= 50:
		for times in range(1,50):
			n=n*times
			for n,l in enumerate(lights):
				if l == 0:
					lights[l] == 1
				elif l == 1:
					lights[l] == 0
	print(lights)