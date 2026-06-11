# hoopster-track

This is a project that tracks the live statistics, scores and outputs player acheivements based on the player choosen. Players currently supported are: LeBron James, Stephen Curry, LaMelo and Luka Dončić. This project uses **nba_api** library for functioning. 

## The Structure

**player_data.py** is the data layer of the project. There are three functions that call the NBA Stats API:
* *get_recent_scores(player_id)* → fetches last 5 games with PTS / REB / AST / W-L stats.
* *get_season_stats(player_id)* → fetches PPG, RPG, APG, FG%, 3P%, FT% for the current season of choosen player.
* *get_achievements(player_id)* → fetches full career awards list (MVPs, All-Stars, championships etc)

**The main.py** is rebuilt and it calls all those functions. 
Options 1–3 now actually print real data. Option 4 helps  to switch player mid-session without restarting. It contains all the basic functionality files and is the foundation of the whole program. 

The other files can be ignored as they are just prototypes of my idea and initiation process. The main, final and new program can be found in *Master Branch*.

## The Process
When you enter your favourite player's name, the particular champions' database is fetched from nba_api and is loaded into the program. Next, when an option is selcted, that vlaue triggers the data from nba_api and outputs it on the screen.

## About **nba_api**
 nba_api is an open-source, unofficial Python client package that provides direct access to the extensive performance statistics and data endpoints of NBA.com. 
 It is widely used by sports analysts, data scientists, and developers to scrape historical and real-time basketball metrics. 
 * Extensive Endpoint Mapping: Bridges your code directly to dozens of official NBA stats endpoints including play-by-play logs, box scores, shot charts, and player career histories.
 * Built-in Static Data: Includes built-in dictionaries for looking up unique player and team IDs without sending repetitive HTTP requests.
 * Pandas Integration: Converts the raw JSON data returned by NBA.com seamlessly into structured Pandas DataFrames using the .get_data_frames() method.
 * Flexible Configurations: Offers native configurations for custom HTTP headers, proxy tracking, and connection timeouts to handle requests safely.

## How to integrate

#Install the package and its requirements via your terminal
pip install nba_api pandas

from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

#1. Search for LeBron James' player dictionary
player_dict = players.get_players()
lebron = [p for p in player_dict if p['full_name'] == 'LeBron James'][0]
lebron_id = lebron['id']
print(f"LeBron James Player ID: {lebron_id}")

#2. Call the career stats endpoint using his ID
career = playercareerstats.PlayerCareerStats(player_id=lebron_id)

#3. Convert the response into a Pandas DataFrame
df = career.get_data_frames()[0]

#Display the first few rows of the career statistics table
print(df.head())






