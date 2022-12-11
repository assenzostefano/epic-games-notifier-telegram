import requests
import os
from bson.objectid import ObjectId

def notification_game1(collection_game, collection_id, bot):
    try:
        print("Try to send first game")

        url = "https://api.plenusbot.xyz/epic_games?country=IT"
        response = requests.get(url).json()

        #All information for first game
        current_games_title1 = response['currentGames'][0]['title'] # First title current games
        current_games_description1 = response['currentGames'][0]['description'] # First description current games
        current_games_startdate1 = response['currentGames'][0]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate'] # Public release first game
        current_games_endate1 = response['currentGames'][0]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate'] # End public release first game
        current_games_price1 = response['currentGames'][0]['price']['totalPrice']['fmtPrice']['originalPrice']
        current_games_images1 = response['currentGames'][0]['keyImages'][0]['url'] # First image current games

        collection_find_username = list(collection_id.find({}, {"username": 1,})) #Find all username in collection
        array_username = list(collection_find_username[0]['username']) #Get just the array

        for i in array_username:
            #Send first and second message when the free game title change
            title_description_1 = current_games_title1 + "\n\n<b>About:</b>\n" + current_games_description1 + "\n" + "\n<b>Start Date:</b>\n" + current_games_startdate1 + "\n" + "\n<b>End Date:</b>\n" + current_games_endate1 + "\n" + "\n<b>Price:</b>\n" + current_games_price1 + " → " + "Free" # Send title, description, start date and price first current game
            img_1 = bot.send_photo(i, current_games_images1) # Send image first current games
            send_message = bot.send_message(i, title_description_1, parse_mode="HTML") # Send all
        
        #Update Collection with new game
        send_game1 = {"Game 1": current_games_title1}
        find_document_game1 = list(collection_game.find({}, {"_id": 1}))
        array_game1 = find_document_game1[0]["_id"]
        sendata1 = collection_game.update_one({'_id':ObjectId(array_game1)}, {"$set": send_game1}, upsert=False)
    except:
        print("An error occurred")
        recheck_game(collection_game=collection_game, collection_id=collection_id, bot=bot)

def notification_game2(collection_game, collection_id, bot,):
    try:
        print("Try to send second game")
        #All information for second game
        current_games_title2 = response['currentGames'][1]['title'] # Second title current game
        current_games_images2 = response['currentGames'][1]['keyImages'][0]['url'] # Second image current game
        current_games_description2 = response['currentGames'][1]['description'] # Second description current game
        current_games_startdate2 = response['currentGames'][1]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate'] #Public release second game
        current_games_endate2 = response['currentGames'][1]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate'] # End public release second game
        current_games_price2 = response['currentGames'][1]['price']['totalPrice']['fmtPrice']['originalPrice'] # Original price second game

        collection_find_username = list(collection_id.find({}, {"username": 1,})) #Find all username in collection
        array_username = list(collection_find_username[1]['username']) #Get the array
        for i in array_username:
            title_description_2 = current_games_title2 + "\n\n<b>About:</b>\n" + current_games_description2 + "\n" + "\n<b>Start Date:</b>\n" + current_games_startdate2 + "\n" + "\n<b>End Date:</b>\n" + current_games_endate2 + "\n" + "\n<b>Price:</b>\n" + current_games_price2 + " → " + "Free" # Send title, description, start date and price second current game
            img_2 = bot.send_photo(i, current_games_images2) # Send image second current games
            send_message = bot.send_message(i, title_description_2, parse_mode="HTML") # Send all
            
        #Update Collection with new game
        send_game2 = {"Game 2": current_games_title2}
        find_document_game2 = list(collection_game.find({}, {"_id": 1}))
        array_game2 = find_document_game2[1]["_id"]
        sendata2 = collection_game.update_one({'_id':ObjectId(array_game2)}, {"$set": send_game2}, upsert=False)
    except:
        print("An error occurred")
        recheck_game(collection_game=collection_game, collection_id=collection_id, bot=bot)