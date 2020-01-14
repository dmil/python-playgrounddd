# by Dhrumil Mehta and Sultan
import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

# 1. Loops through each vegetable

# 2. In the loop, write the name of each 
# vegetable and the color into a CSV 
# called vegetables.csv
with open('vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color'])

	for veg in vegetables:
		writer.writerow([veg["name"], veg["color"]])


# hint!:Don't forget to first write 
# a header row to the CSV BEFORE
# looping through the vegetables