"""
Load in the three separate files and combine them to create the merged file
"""
import pandas as pd

passing = pd.read_csv("../data/raw/passing_stats.csv")
passing = passing.drop(columns=["Player-additional"])



rushing = pd.read_csv("../data/raw/rushing_stats.csv")
rushing= rushing.drop(columns=["-9999"])

receiving = pd.read_csv("../data/raw/receiving_stats.csv")
receiving = receiving.drop(columns=["-9999"])



passing = passing[['Player','Pos', 'Yds', 'TD', 'Int']].rename(
    columns={'Yds': 'PassYds', 'TD': 'PassTDs'})

rushing = rushing[['Player','Pos', 'Yds', 'TD']].rename(
    columns={'Yds':'RushYds', 'TD':'RushTDs'})

receiving = receiving[['Player','Pos','Rec','Yds','TD']].rename(
    columns={'Yds': 'RecYds', 'TD':'RecTDs'})

#use merge instead of concat to have one row for each player showing all stats
player_stats = (
    passing
    .merge(rushing, on=["Player","Pos"], how="outer")
    .merge(receiving, on=["Player","Pos"], how="outer")
)

#replace NaN with 0 for looks
player_stats.fillna(0, inplace=True)

pd.set_option("display.max_columns", None)   # show all columns
pd.set_option("display.width", None)         # don't wrap columns
pd.set_option("display.max_colwidth", None)  # show full column
pd.set_option("display.max_rows", None)  #show all rows

print(player_stats)

player_stats.to_csv("../data/processed/player_stats.csv")





