"""
Ask the user for their roster, display it to them when it's collected
"""
from src.preprocess import player_stats

roster = {}

user_roster = input("Enter player names from your roster (Use first and last name of the player). \nType 'done' when finished:\nPlayer Name: ")

while user_roster.lower() != "done":
    #find the player's row in the big dataset
    player_row = player_stats[player_stats["Player"] == user_roster]

    if not player_row.empty:
        # get the actual position
        position = player_row.iloc[0]["Pos"]

        # update roster
        roster[user_roster] = {"position": position}
    else:
        print(f"'{user_roster}' not found in dataset.")

    user_roster = input("Player Name (or 'done' to finish): ")

print(roster)
