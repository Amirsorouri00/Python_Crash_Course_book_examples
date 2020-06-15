players = ['charles', 'martina', 'michael', 'florance', 'eli']
print(players[0:3])
print(players[0:4])
print(players[1:4])
print(players[:4])
print(players[2:])

# looping through a slice
print("here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

# Copying the list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)
