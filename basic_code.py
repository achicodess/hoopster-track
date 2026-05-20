print("Players in this draft: LeBron James, Stephen Curry, Luka Dončić and LaMelo")
print("*ATTENTION*: Please enter lowercase letters only!!")

name = input("Enter your favorite NBA player: ").strip().lower()

players = ["lebron james", "lebron", "stephen curry", "curry", "luka dončić", "luka", "lamelo"]

if name in players:   # Start of main "if/else" block.
    print("Player found.")      # Checks and validates player's name in list.
    while True:
        print("Option 1 - Match scores")
        print("Option 2 - Statistics")
        print("Option 3 - Achievements")
        print("Option 4 - Exit")          # 4 options with what they do.

        try:
            opt = int(input("Enter your choice: "))  # Added try/except to tackle any user input errors. 
        except ValueError:                               # ValueError:Occurs when operation recevies arh=guement with correct datatype but wrong value.
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
            print("Invalid input")  # Options selection and description of what the particular section does. 
else:    
    print("Player not found. Please refer to the players list above.")    # End of main "if/else block"  
# Response if name is not present. 
                        
