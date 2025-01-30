import requests
import json

# URL of the API
url = "https://sports.core.api.espn.com/v3/sports/basketball/nba/athletes?limit=18000"

# Send a GET request to the API
response = requests.get(url)

count = 0

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract player names and IDs
    players = []
    for player in data['items']:
        player_id = player['id']
        player_name = player['fullName']
        players.append({'id': player_id, 'name': player_name})
    
    # Print the extracted player names and IDs
    for player in players:
        print(f"Player ID: {player['id']}, Player Name: {player['name']}")
        count += 1
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
    
print("Player Count: " + count)