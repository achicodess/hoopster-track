print("Players in this draft: LeBron James, Stephen Curry, Luka Dončić and LaMelo")
name=input("Enter your favorite NBA player: ").strip() .lower()
players=["lebron james", "lebron", "stephen curry", "curry", "luka dončić", "luka", "lamelo"] 
#Only lowercase letters allowed. 
if name in players:
	print("Player found.")
else:
	print("Please refer the players list above.")