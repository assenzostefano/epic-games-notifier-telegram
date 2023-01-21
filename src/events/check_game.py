from . import notification_game
import requests
import time

#Function that waits 10 seconds before trying again
def recheck_game(collection_game, collection_id, bot):
    time.sleep(10)
    a(collection_game=collection_game, collection_id=collection_id, bot=bot)

#Function for check new games, if there are a new game, send notification
def a(collection_game, collection_id, bot):
    try:
        #Connect to API
        url = "https://minty.apexie.eu/v1/epicfreegames" #URL API
        response = requests.get(url).json() #API in JSON

        # Title of current games
        try:
            current_games_title1 = response['games'][0]['title'] #Title of first game
            search_game1 = collection_game.find_one({"Game 1": current_games_title1}) #Search game1 in MongoDB

            if search_game1 is None: #If game1 is not in MongoDB send notification
                #Send notification if title game is changed
                print("Found a new 1 game!")
                print("Now I'm sending the notification to everyone.")
                notification_game.notification_game1(collection_game, collection_id, bot)
            else:
                print("Current Game 1 not found")
        except:
            print("Current Game 1 not found")
            #recheck_game(collection_game, collection_id, bot)

        try:
            current_games_title2 = response['games'][1]['title'] #Title of second game
            search_game2 = collection_game.find_one({"Game 2" : current_games_title2}) #Search game2 in MongoDB
            if search_game2 is None: #If game2 is not in MongoDB send notification
                #Send notification if title game is changed
                print("Found a new 2 game!")
                print("Now I'm sending the notification to everyone.")
                notification_game.notification_game2(collection_game, collection_id, bot)
        except:
            print("Current Game 2 not found")
            #recheck_game(collection_game, collection_id, bot)
        
        try:
            current_games_title3 = response['games'][2]['title']
            search_game3 = collection_game.find_one({"Game 3" : current_games_title3})
            if search_game3 is None: #If game2 is not in MongoDB send notification
                #Send notification if title game is changed
                print("Found a new 2 game!")
                print("Now I'm sending the notification to everyone.")
                notification_game.notification_game3(collection_game, collection_id, bot)
        except:
            print("Current Game 3 not found")
            recheck_game(collection_game, collection_id, bot)
    except:
        print("An error occurred")
        recheck_game(collection_game, collection_id, bot)