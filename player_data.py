# player_data.py
# ─────────────────────────────────────────────────────────────────
# Hoopster Track — Data Layer
# Uses the `nba_api` library (pip install nba_api) to fetch real,
# up-to-date NBA player data. No API key needed.
# ─────────────────────────────────────────────────────────────────

import time
from nba_api.stats.static import players
from nba_api.stats.endpoints import (
    playercareerstats,
    playergamelog,
    playerawards,
)


# ── 1. ALIAS TABLE ────────────────────────────────────────────────
# Maps every nickname / spelling the user might type → canonical NBA name.
# Add more aliases here as you expand the player list.

PLAYER_ALIASES: dict[str, str] = {
    # LeBron James
    "lebron james":  "LeBron James",
    "lebron":        "LeBron James",
    "lbj":           "LeBron James",
    "king james":    "LeBron James",
    # Stephen Curry
    "stephen curry": "Stephen Curry",
    "steph curry":   "Stephen Curry",
    "curry":         "Stephen Curry",
    "steph":         "Stephen Curry",
    # Luka Dončić  (support both accented + plain ASCII)
    "luka dončić":  "Luka Doncic",
    "luka doncic":  "Luka Doncic",
    "luka":          "Luka Doncic",
    "doncic":        "Luka Doncic",
    # LaMelo Ball
    "lamelo ball":  "LaMelo Ball",
    "lamelo":       "LaMelo Ball",
    "melo":         "LaMelo Ball",
}

# ── 2. HELPER FUNCTIONS ───────────────────────────────────────────

def resolve_player_name(user_input: str) -> str | None:
    """
    Converts the user's raw input to the canonical player name.
    Returns None if not found.
    """
    return PLAYER_ALIASES.get(user_input.strip().lower())


def get_player_id(canonical_name: str) -> int | None:
    """
    Returns the NBA Stats API player ID for a canonical name.
    Returns None if the player is not found in the static registry.
    """
    result = players.find_players_by_full_name(canonical_name)
    if result:
        return result[0]["id"]
    return None


# ── 3. DATA FETCH FUNCTIONS ───────────────────────────────────────
# Each function includes a short sleep() to respect NBA API rate limits.
# The API doesn't need a key but throttles aggressive requests.

def get_recent_scores(player_id: int, num_games: int = 5) -> list[dict]:
    """
    Fetches the last `num_games` game scores for the player.

    Returns a list of dicts with keys:
        GAME_DATE, MATCHUP, PTS, REB, AST, STL, BLK, WL
    """
    time.sleep(0.8)  # polite pause — NBA API rate limit
    gamelog = playergamelog.PlayerGameLog(
        player_id=player_id,
        season="2024-25",      # ← update season string each year
        timeout=10
    )
    df = gamelog.get_data_frames()[0]

    if df.empty:
        return []

    cols = ["GAME_DATE", "MATCHUP", "PTS", "REB", "AST", "STL", "BLK", "WL"]
    return df[cols].head(num_games).to_dict(orient="records")


def get_season_stats(player_id: int) -> dict | None:
    """
    Fetches the player's most recent season averages.

    Returns a dict with:
        Season, Team, GP, PPG, RPG, APG, SPG, BPG, FG%, 3P%, FT%
    """
    time.sleep(0.8)
    career = playercareerstats.PlayerCareerStats(
        player_id=player_id,
        timeout=10
    )
    df = career.get_data_frames()[0]  # regular season totals per season

    if df.empty:
        return None

    latest = df.iloc[-1]            # last row = most recent season
    gp = latest["GP"]

    if gp == 0:
        return None

    return {
        "Season":  latest["SEASON_ID"],
        "Team":    latest["TEAM_ABBREVIATION"],
        "GP":      int(gp),
        "PPG":     round(latest["PTS"]     / gp, 1),
        "RPG":     round(latest["REB"]     / gp, 1),
        "APG":     round(latest["AST"]     / gp, 1),
        "SPG":     round(latest["STL"]     / gp, 1),
        "BPG":     round(latest["BLK"]     / gp, 1),
        "FG%":     round(latest["FG_PCT"]  * 100, 1),
        "3P%":     round(latest["FG3_PCT"] * 100, 1),
        "FT%":     round(latest["FT_PCT"]  * 100, 1),
    }


def get_achievements(player_id: int) -> list[str]:
    """
    Fetches career awards and honours for the player from the NBA API.

    Returns a list of formatted strings: "SEASON — AWARD_NAME"
    """
    time.sleep(0.8)
    awards = playerawards.PlayerAwards(
        player_id=player_id,
        timeout=10
    )
    df = awards.get_data_frames()[0]

    if df.empty:
        return ["No awards data available from the API."]

    result = []
    for _, row in df.iterrows():
        # PlayerAwards columns: PLAYER_ID, PLAYER_NAME, TEAM, DESCRIPTION,
        #                       ALL_NBA_TEAM_NUMBER, SEASON, MONTH, WEEK,
        #                       CONFERENCE, TYPE
        line = f"{row.get('SEASON', '----')}  —  {row.get('DESCRIPTION', 'Award')}"
        result.append(line)

    return result
