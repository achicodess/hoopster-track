print("Players in this draft: LeBron James, Stephen Curry, Luka Dončić and LaMelo")
print("*ATTENTION*: Please enter lowercase letters only!!")

name = input("Enter your favorite NBA player: ").strip().lower()

players = ["lebron james", "lebron", "stephen curry", "curry", "luka dončić", "luka", "lamelo"]

if name in players:
    print("Player found.")
    while True:
        print("Option 1 - Match scores")
        print("Option 2 - Statistics")
        print("Option 3 - Achievements")
        print("Option 4 - Exit")

        try:
            opt = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if opt == 1:
            print("This section gives you the baskets scored by", name, "in recent matches.")
        elif opt == 2:
            print("This section gives you an overall summary of how your chosen player has played across their entire career.")
        elif opt == 3:
            print("This section tells you about the achievements of", name)
        elif opt == 4:
            print("Exiting the application.")
            break
        else:
            print("Invalid input")
else:
    print("Player not found. Please refer to the players list above.")

