friends = []
for _ in range(0, 3):
    friends.append(input("Enter a friend: "))
nearby_file = open("nearby_friends.txt", "w")
people_file = open("people.txt", 'r')
people = people_file.read()
for friend in friends:
    if friend in people:
        print(f"{friend} is nearby!")
        nearby_file.write(friend + "\n")
people_file.close()
nearby_file.close()