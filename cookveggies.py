# by Dhrumil And Sultan

# 1. Read vegetables.csv (see previous section) 
#    into a variable called vegetables.
import csv
import json

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    vegetables = [dict(row) for row in rows] # Convert OrderedDict to regular dict

# 2. Print the variable vegetables.
print(vegetables)

# 3. Write vegetables as a JSON file 
#    called vegetables.json. 
#    It should look like this:
with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f, indent=2)

# [
#   { "name": "eggplant", "color": "purple" },
#   { "name": "tomato", "color": "red" },
#   { "name": "corn", "color": "yellow" },
#   { "name": "okra", "color": "green" },
#   { "name": "arugula", "color": "green" },
#   { "name": "broccoli", "color": "green" }
# ]
