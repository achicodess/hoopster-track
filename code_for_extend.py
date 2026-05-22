opt=int(input("Enter option: "))
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


            