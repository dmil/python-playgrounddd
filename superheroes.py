# by Dhrumil Mehta and Sultan

# Reads superheroes.json (in this folder)
import json
import csv
from pprint import pprint

# 1. Read superheroes.json
with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)
	
# 2. Write a header to the CSV file

with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(["name", "age", "secretIdentity", "powers", "squadName", "homeTown", "formed", "secretBase", "active"])
		
	# 3. Loop over the members, and for 
	#    each member write a row to the csv file

	members = superheroes['members']
	for hero in members:
		hero_name = hero['name']
		hero_age = hero['age']
		hero_powers = hero['powers']
		hero_secret_id = hero['secretIdentity']

		squad_name = superheroes['squadName']
		squad_hometown = superheroes['homeTown']

		writer.writerow([
			hero_name, 
			hero_age, 
			hero_secret_id,
			hero_powers,
			squad_name,
			squad_hometown])


