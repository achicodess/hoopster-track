# hoopster-track

This is a project where the application tracks the live scores, statistics and displays the achievements of your favorite basketball player in the NBA.
The players of whom you can view the data currently are : Stephen Curry, LeBron James, LaMelo and Luka Dončić. 

## The Procedure

I have used the concepts I have learnt through Dr Charles Sevrance's Python For Everybody course. The basic code has been written entirely in Python using simple concepts learnt through the timeline of the course. For live data fetching and it's display, I will be using nba_api library. 


## nba_api library
nba_api is a free library that solves the database and API confusion in the project. This library keeps track of the live scores of the player and is updated in real-time.

# The Structure: 

player_data.py is the data layer of the project. There are three functions that call the NBA Stats API:
* get_recent_scores(player_id) → fetches last 5 games with PTS / REB / AST / W-L stats.
* get_season_stats(player_id) → fetches PPG, RPG, APG, FG%, 3P%, FT% for the current season of choosen player.
* get_achievements(player_id) → fetches full career awards list (MVPs, All-Stars, championships etc)
The main.py — is rebuilt and it calls all those functions. Options 1–3 now actually print real data.
Added Option 4 to switch player mid-session without restarting.

## What has been done

* 2 print statements about players list and input caution 
* list of players and their nicknames
* .strip() and .lower() added
* if, else statement to verify player's presence in the list
  
Next, i have to figure out a way to get the choosen NBA player's database that syncs with real-time and present status of the palyer. I have to also construct a kind of database. For this, 
* I will use a local file
* Make Python to read the file
* Extract relavent information
* Display the information
* OR I will construct an SQL Database that the program can read, extract and display information from.

Or perhaps I can use an API that does this task for me.

## I still have three thing pending:
* Figuring out the overall structure + mechanism 
* Organising the code 
                                    
                                    
                                    



