# hoopster-track

This is a project that tracks the live statistics, scores and outputs player acheivements based on the player choosen. Players currently supported are: LeBron James, Stephen Curry, LaMelo and Luka Dončić. This project uses **nba_api** library for functioning. 

## The Structure

**player_data.py** is the data layer of the project. There are three functions that call the NBA Stats API:
* *get_recent_scores(player_id)* → fetches last 5 games with PTS / REB / AST / W-L stats.
* *get_season_stats(player_id)* → fetches PPG, RPG, APG, FG%, 3P%, FT% for the current season of choosen player.
* *get_achievements(player_id)* → fetches full career awards list (MVPs, All-Stars, championships etc)

**The main.py** is rebuilt and it calls all those functions. 
Options 1–3 now actually print real data. Option 4 helps  to switch player mid-session without restarting.


