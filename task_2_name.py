print()
print("Welcome to the dungeon!")
print("What is your name?")

name = input("> ")

print("Hello, %s." % (name))
print("Let's play a game.")
print("There are two doors. Do you go through door 1 or door 2?")

def wrong_input():
	print("You are not so good with numbers, %s, are you?" % (name))

door = input("> ")

if door == "1":
	print("There is a nice vampire asking you if you enjoy life.")
	print("What do you do, %s?" % (name))
	print("1. Smile and nod")
	print("2. Scream and run")

	answer = input("> ")

	if answer == "1":
		print("Congratulations, %s, you found a new friend!" % (name))
	elif answer == "2":
		print("Sorry, %s, the vampire is faster. You become a dinner." % (name))
	else:
		wrong_input()

elif door == "2":
	print("You enter a dark room with a big box and another, smaller door.")
	print("What do you, %s?" % (name))
	print("1. Open the box.")
	print("2. Open the next door.")

	answer = input ("> ")

	if answer == "1":
		print("You discover that the box is filled with gold and jewels. Congratulations, %s you are now rich." % (name))
	elif answer == "2":
		print("There is a skeleton behind the door. You scream and run away.")
	else:
		wrong_input()
else:
	wrong_input()
