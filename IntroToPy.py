float_division = 12 / 3
print(float_division)

#double slash indicates integer division
integer_division = 12 // 3
print(integer_division)

integer_division = 13 // 5
print(integer_division)

#modulus for remainder
remainder = 13 % 5
print(remainder)

x = 37
remainder = x % 2
print(remainder)

#String Operations
my_string = "Hello, world!"
print(my_string)

string_qith_quotes = "Hello, it's me."
another_with_quotes = "He said \"You are amazing\" today!"

name = "Abhi"
name_two = "nav"
print(name + name_two)

age = 34
print("you are " + str(age))
#concatenates the num into a string with str()

#string formatting
name = "Abhinav"
greeting = f"How are you, {name}?"
print(greeting)
"""
"""
#boolean operations
age = 20
is_over_age = age >= 18
is_under_age = age < 18
is_twenty = age == 20

my_number = 5
user_number = int(input("Enter a number: "))
matches = my_number == user_number
print(f"You got it right: {matches}.")

age = int(input("Enter your age: "))
usually_working = age >= 18 or age <= 65

print(f"At {age}, you are usually not working: {usually_working}.")

print(bool(35))
print(bool("Roff"))

print(bool(0))
print(bool(0.0))
print(bool(""))

x = 35 and 0
print(x)

x = True
cmp = x and 18
print(cmp)

#list
friends = ["Rolf", "Bob", "Anne"]
print(friends[0])
print(friends[1])

print(len(friends))
friends_age = [
  ["Rolf", 24], 
  ["Bob", 20], 
  ["Anne", 27]
]

friends.append(["Ale", 54])
friends.remove(["Ale", 54])

#tuple
short_tuple = ("Rolf", "Bob", "Anne")
friends = friends + ("Jen",)
print(friends)

#set operations
art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}

art_friends.add("Jen")

print(art_friends)

art_friends.remove("Jen")

print(art_friends)
# does not print out repeats unlike tuples

art_but_not_science = art_friends.difference(science_friends)
#removes all the elements that are similar between sets

science_but_not_art = science_friends.difference(art_friends)

print(art_but_not_science)
print(science_but_not_art)

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

art_and_science = art_friends.intersection(science_friends)
print(art_and_science)


#dictionaries
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Rolf"])

friend_ages["Bob"] = 20
friend_ages["Rolf"] = 25

print(friend_ages)
friends = (
  {"name": "Rolf Smith", "age": 24},
  {"name": "Adam Wool", "age": 30},
  {"name": "Anne Pun", "age": 27},
)


grades = [80, 75, 90, 100]

total = sum(grades)
length = len(grades)
print(str(total) + " " + str(length))

lottery_numbers = {13, 21, 22, 5, 8}

players = [{'name': 'vaibhav', 'numbers': {59, 30, 32, 4, 53}}, {'name': 'abheebo', 'numbers': {1, 2, 3, 4, 5}}]
    
x = len(players[0]["numbers"].intersection(lottery_numbers)) 
y = len(players[1]["numbers"].intersection(lottery_numbers))

print(f"Player {players[0]['name']} got {x} numbers right.")
print(f"Player {players[1]['name']} got {y} numbers right.") 
