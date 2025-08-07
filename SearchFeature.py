#Author: Annie Luse
#Date: August 2nd, 2025
#Program description: CS361 Microservice A - Search Feature

import requests #You might need to install the requests library with "pip install requests" 
#also btw it gives me the squiggly error lines (under the word requests) but it works fine anyways so don't worry about that if it happens
import sys

def search_function(user_input):

    url = f"https://api.rawg.io/api/games?key=fe946676201443efb4a0cfcde7c04cbb&search={user_input}&page_size=1"

    #Make a GET request to the API
    response = requests.get(url)
    data = response.json()

    if data["results"]:
        #Grab the first result
        game = data["results"][0]
        print("Game found!")
        print("Name:", game["name"])
        print("Released:", game.get("released", "Unknown"))
        print("Rating:",	game.get("rating"))
        #Only include tags where all characters are ASCII (AKA English)
        tags = [tag["name"] for tag in game.get("tags", []) if tag["name"].isascii()]
        print("Top 5 Genre Tags:", tags[:5])

    else:
        print("Game not found, try again Hero/Heroine!")

#Check if the user provided a command line argument
if len(sys.argv) > 1:
    user_input = sys.argv[1]
    search_function(user_input)
else:
    print("No game name provided.")
