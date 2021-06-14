import json

with open('friends_json.txt', 'r') as file:
    file_contents = json.load(file)
#remember this process fluently

#file = open('friends_json.txt', 'r')
#file_contents = json.load(file) #makes a dictionary


cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

with open('cars_json.txt', 'w') as file:
    json.dump(cars, file)

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])