print()
print("Welcome to the dungeon!")
print("Do you go through door 1 or door 2?")

door = input(">")

if door == "1":
	print("There is a nice vampire asking you if you enjoy life.")
	print("What do you do?")
	print("1. Smile and nod")
	print("2. Scream and run")

	answer = input(">")

	if answer == "1":
		print("Congratulations, you found a new friend!")
	elif answer == "2":
		print("Sorry, the vampire is faster. You become a dinner.")
	else:
		print("You are not so good with numbers, are you?")

elif door == "2":
	print("You enter a dark room with a big box and another, smaller door.")
	print("What do you?")
	print("1. Open the box.")
	print("2. Open the next door.")

	answer = input (">")

	if answer == "1":
		print("You discover that the box is filled with gold and jewels. Congratulations, you are now rich.")
	elif answer == "2":
		print("There is a skeleton behind the door. You scream and run away.")
	else:
		print("You are not very good with numbers, are you?")
else:
	print("You are not so good with numbers, are you?")
