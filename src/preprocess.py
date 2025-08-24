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



passing = passing[['Player', 'Pos', 'Yds', 'TD', 'Int']]
rushing = rushing[['Player','Pos','Yds','TD']]
receiving = receiving[['Player','Pos','Rec','Yds','TD']]




