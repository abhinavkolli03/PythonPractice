friend = "Rolf"
user_name = input("Enter your name: ")

if user_name == friend:
  print("Hello, friend!")
  print("This runs too.")
else:
  print("Hello stranger!")

if user_name != friend:
  print("Hello stranger!")

print("This runs anyway.")

friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your new name: ")

if user_name in friends:
  print("Hello friend!")
elif user_name in family:
  print("Hello, family!")
else:
  print("I don't know you!")

#while loops
is_learning = True

while is_learning:
  print("You're learning!")
  user_input = input("Are you still learning? ")
  is_learning = user_input == "yes"

print("We stopped running.")

#for loops
friends = ["Rolf", "Jen", "Anne"]
for friend in friends:
  print(friend)

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8]

for index in elements:
  print("Hello, world!")

for index in range(5, 10):
  print("Hello world!")

for index in range(2, 20, 3):
  print(index)

students = [
  {"name": "Rolf", "grade": 90},
  {"name": "Bob", "grade": 78},
  {"name": "Jen", "grade": 100},
  {"name": "Anne", "grade": 80},
]

for student in students:
  name = student["name"]
  grade = student["grade"]

  print(f"{name} has a grade of {grade}.")

friends = [("Rolf", 25, 2000), ("Anne", 27, 2003), ("Jane", 33, 4023)]

for name, age, birthday in friends:
  print(f"{name} is {age} years old. Bday {birthday}")

friend_ages = {"Rolf": 35, "Anne": 37, "Charlie": 31}

for name, age in friend_ages.items():
  print(f"{name} is {age} years old.")

cars = ["ok", "ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
  if status == "faulty":
    print("Found faulty car, skipping!")
    continue
  print(f"This car is {status}.")
  print("Shipping new car to customer!")
else:
  print("All cars built successfully. No faulty cars.")

for n in range(2, 10):
  for x in range (2, n):
    if n % x == 0:
      print(f"{n} equals {x} * {n//x}")
      break
  else:
    print(f"{n} is a prime number.")

friends = ["Rolf", "Charlie", "Anna", "Bob"]
print(friends[-2:-1])

#List comprehension in python
doubled_numbers = [_ * 2 for _ in range(5)]

print(doubled_numbers)

friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} years old." for age in friend_ages]

names = ["Rolf", "Bob", "Jen"]
lowercase = [name.lower() for name in names]
print(lowercase)


ages = [22, 35, 27, 21, 20]
odds = []
for age in ages:
  if age % 2 == 1:
    odds.append(age)

print(odds)

#dictionary combination
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = list(zip(friends, time_since_seen))


long_timers = {
  friends[i] : time_since_seen[i]
  for i in range(len(friends))
  if time_since_seen[i] > 5
}

print(long_timers)

friends = ["Rolf", "John", "Anna"]

index = 0

for friend in friends:
  print(index)
  print(friend)
  index = index + 1

for index, friend in enumerate(friends):
  print(index)
  print(friend)

print(list(enumerate(friends)))
print(dict(enumerate(friends)))

def greet():
  name = input("Enter your name: ")
  print(f"Hello, {name}!")

greet()


