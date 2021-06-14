file = open('csv_data.txt', 'r')
lines = file.readlines()
print(lines)
file.close()

lines = [line.strip() for line in lines[1:]]
#remember to use strip to get rid of whitespace and read lines

for line in lines:
    #split data into a list
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    print(f'{name} is {age}, studying {degree} at {university}.')

sample_csv_value = ' '.join(['Rolf', '25', 'MIT', 'Computer Science'])
#to create a list of data as seen in csv files
print(sample_csv_value)