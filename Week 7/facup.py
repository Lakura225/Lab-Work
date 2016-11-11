import csv

def test():
	with open('Week 7 \ facup.csv') as csvfile:
		rdr = csv.reader(csvfile)
		for row in rdr:
			print(row[0] + " last won indented " + row[1])