#input block
opt=int(input("Enter option: "))
print("Database only refers to Stephen Curry currently.")

#if loop
if opt == 1:
    print("This section gives you the baskets scored by"),#(name, "in recent matches.")
    obj=open("database_file_curry.py","r")
    obj.read()
    print("Curry's Awesome Score: ")
    print(obj)
elif opt==2:
     print("This section gives you an overall summary of how your chosen player has played across their entire career.")
     obj2=open("database_file_curry_stats.py", "r")
     obj2.read()
     print("Curry's Jawdropping Stats: ")
     print(obj2)
elif opt==3:
    print("This section tells you about the achievements of") #(, name)
    obj3=open("database_file_curry_achiev.py","r")
    obj3.read()
    print("Curry's Glorious Achievements: ")
    print(obj3)
elif opt==4:
    print("Exiting the application")
    quit()

# for loop
# Repeating the player's list and input prompting
# This is a trail code implementing an additional for loop. 
players=["lebron james", "lebron", "stephen curry", "curry", "luka dončić", "luka", "lamelo"]
name=input("Enter player's name: ")
for name in players:
    if name=="stephen curry":
        print("Player choosen is",name)
    elif name=="lebron james":
        print("Player choosen is",name)
    elif name=="luka dončić":
        print("Player choosen is",name)
    elif name=="lamelo":
        print("Player choosen is", name)
    else:
        print("Invalid player name")
else:
    print("Player not found")




            
