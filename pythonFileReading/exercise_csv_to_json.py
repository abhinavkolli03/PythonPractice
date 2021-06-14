import json

csv_file = open('csv_file.txt', 'r')
file_content = csv_file.readlines()
lines = [line.strip() for line in file_content]
csv_file.close()

json_list = []

for line in lines:
    club, city, country = line.split(',')
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)

json_file = open('json_file.txt', 'w')
json.dump(json_list, json_file)
json_file.close()