# main.py
# ─────────────────────────────────────────────────────────────────
# Hoopster Track — Main CLI Application
# Run:  python main.py
# Requires: pip install nba_api pandas
# ─────────────────────────────────────────────────────────────────

from player_data import (
    PLAYER_ALIASES,
    resolve_player_name,
    get_player_id,
    get_recent_scores,
    get_season_stats,
    get_achievements,
)


# ── Display helpers ───────────────────────────────────────────────

DIVIDER  = "─" * 52
HEADER   = "═" * 52

def banner():
    print(HEADER)
    print("   🏀  HOOPSTER TRACK  —  NBA Player Dashboard")
    print(HEADER)
    unique_names = sorted(set(PLAYER_ALIASES.values()))
    print("  Players: " + ", ".join(unique_names))
    print(DIVIDER)


def display_scores(player_id: int, name: str):
    """Prints the last 5 game results in a readable table."""
    print(f"\n📋  Last 5 Games — {name}")
    print(DIVIDER)
    print(f"  {'DATE':<12} {'MATCHUP':<22} {'PTS':>4} {'REB':>4} {'AST':>4} {'RES':>4}")
    print(DIVIDER)

    games = get_recent_scores(player_id, num_games=5)

    if not games:
        print("  No recent game data available.")
        return

    for g in games:
        outcome = " W ✓" if g["WL"] == "W" else " L ✗"
        print(
            f"  {g['GAME_DATE']:<12} "
            f"{g['MATCHUP']:<22} "
            f"{int(g['PTS']):>4} "
            f"{int(g['REB']):>4} "
            f"{int(g['AST']):>4} "
            f"{outcome:>4}"
        )
    print(DIVIDER)


def display_stats(player_id: int, name: str):
    """Prints current season averages."""
    print(f"\n📊  Season Statistics — {name}")
    print(DIVIDER)

    stats = get_season_stats(player_id)

    if not stats:
        print("  No statistics available.")
        return

    print(f"  Season  : {stats['Season']}  ({stats['Team']})")
    print(f"  Games   : {stats['GP']}")
    print(DIVIDER)
    print(f"  PPG     : {stats['PPG']:>6}  (points per game)")
    print(f"  RPG     : {stats['RPG']:>6}  (rebounds per game)")
    print(f"  APG     : {stats['APG']:>6}  (assists per game)")
    print(f"  SPG     : {stats['SPG']:>6}  (steals per game)")
    print(f"  BPG     : {stats['BPG']:>6}  (blocks per game)")
    print(DIVIDER)
    print(f"  FG%     : {stats['FG%']:>5}%")
    print(f"  3P%     : {stats['3P%']:>5}%")
    print(f"  FT%     : {stats['FT%']:>5}%")
    print(DIVIDER)


def display_achievements(player_id: int, name: str):
    """Prints career awards and honours."""
    print(f"\n🏆  Career Achievements — {name}")
    print(DIVIDER)

    awards = get_achievements(player_id)

    for award in awards:
        print(f"  🥇 {award}")

    print(DIVIDER)


# ── Menu ──────────────────────────────────────────────────────────

def show_menu():
    print(f"\n{DIVIDER}")
    print("  1 — Match Scores      (last 5 games)")
    print("  2 — Season Statistics (current season averages)")
    print("  3 — Achievements      (career awards)")
    print("  4 — Change Player")
    print("  5 — Exit")
    print(DIVIDER)


# ── Main flow ─────────────────────────────────────────────────────

def select_player() -> tuple[str, int] | tuple[None, None]:
    """
    Prompts user for a player name, validates it, and returns
    (canonical_name, player_id). Returns (None, None) on failure.
    """
    user_input = input("\nEnter your favorite NBA player: ").strip().lower()
    canonical_name = resolve_player_name(user_input)

    if not canonical_name:
        print(f"  ❌ '{user_input}' not found. Please use the names listed above.")
        return None, None

    print(f"  ⏳ Fetching data for {canonical_name}...")
    player_id = get_player_id(canonical_name)

    if not player_id:
        print("  ❌ Could not retrieve player ID. Check your internet connection.")
        return None, None

    print(f"  ✅ Loaded: {canonical_name}")
    return canonical_name, player_id


def main():
    banner()

    # Player selection loop
    name, pid = None, None
    while pid is None:
        name, pid = select_player()

    # Main menu loop
    while True:
        show_menu()

        try:
            opt = int(input("  Enter your choice: "))
        except ValueError:
            print("  ⚠️  Please enter a number between 1 and 5.")
            continue

        if opt == 1:
            display_scores(pid, name)
        elif opt == 2:
            display_stats(pid, name)
        elif opt == 3:
            display_achievements(pid, name)
        elif opt == 4:
            banner()
            name, pid = None, None
            while pid is None:
                name, pid = select_player()
        elif opt == 5:
            print("\n  Thanks for using Hoopster Track. See you next game! 🏀\n")
            break
        else:
            print("  ⚠️  Invalid choice. Please enter 1–5.")


if __name__ == "__main__":
    main()
