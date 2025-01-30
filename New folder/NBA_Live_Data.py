from nba_api.live.nba.endpoints import scoreboard
import json

# Today's Score Board
games = scoreboard.ScoreBoard()

# json
data = games.get_json()

# dictionary
Games_Dic = games.get_dict()

print(Games_Dic)

def format_json(data):
    """
    This function takes a JSON object and returns a formatted string for readability.
    """
    return json.dumps(data, indent=4)


formatted_json = format_json(data)
print(formatted_json)

# I want to get the game scoreboard to get the teams that are playing in a day.
# Next I want to get the players that start for said teams, and then I would have to find there name in the players.py file and get their playerid
# Then I want to put the player id into the ESPN_SCRAPING.py function, Would need to put all player ids into a list and iterate through the list and get each players predecdied stats for the game.
# (((May want to get the team they play OR just have the month that it is. OR HOME and AWAY)))