from . import notification_game
import requests
import time

def recheck_game(collection_game, collection_id, bot, OBJECTID_idlist, OBJECTID_game1, OBJECTID_game2):
    time.sleep(10)
    a(collection_game=collection_game, collection_id=collection_id, bot=bot, OBJECTID_idlist=OBJECTID_idlist, OBJECTID_game1=OBJECTID_game1, OBJECTID_game2=OBJECTID_game2)

#Function for send every week the notification
def a(collection_game, collection_id, bot, OBJECTID_idlist, OBJECTID_game1, OBJECTID_game2):
    try:
        #Check for new games
        url = "https://api.plenusbot.xyz/epic_games?country=IT"
        response = requests.get(url).json()

        # Title of current games
        current_games_title1 = response['currentGames'][0]['title']
        current_games_title2 = response['currentGames'][1]['title']

        #Check first game
        search_game1 = collection_game.find_one({"Game 1" : current_games_title1})
        search_game2 = collection_game.find_one({"Game 2" : current_games_title2})
        print(search_game1)
        if search_game1 is None:
            #Send notification if title game is changed
            print("Found a new 1 game!")
            print("Now I'm sending the notification to everyone.")
            notification_game.notification_game1(collection_game, collection_id, bot, OBJECTID_idlist, OBJECTID_game1)
        if search_game2 is None:
            #Send notification if title game is changed
            print("Found a new 2 game!")
            print("Now I'm sending the notification to everyone.")
            notification_game.notification_game2(collection_game, collection_id, bot, OBJECTID_idlist, OBJECTID_game1, OBJECTID_game2)
        else:
            #If new game is changed recheck every 10 second
            print("The game is not changed")
            recheck_game(collection_game, collection_id, bot, OBJECTID_idlist, OBJECTID_game1, OBJECTID_game2)
    except:
        print("An error occurred")
        recheck_game(collection_game, collection_id, bot, OBJECTID_idlist, OBJECTID_game1, OBJECTID_game2)
    else:
        recheck_game(collection_game, collection_id, bot, OBJECTID_idlist, OBJECTID_game1, OBJECTID_game2)