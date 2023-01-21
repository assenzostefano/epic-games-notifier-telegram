import requests
import os
from bson.objectid import ObjectId

def notification_game1(collection_game, collection_id, bot):
    try:
        print("Try to send first game")

        url = "https://minty.apexie.eu/v1/epicfreegames"
        response = requests.get(url).json()

        #All information for first game
        current_games_title1 = response['games'][0]['title'] # First title current games
        current_games_description1 = response['games'][0]['description'] # First description current games
        current_games_images1 = response['games'][0]['mainImage'] # First image current games

        collection_find_username = list(collection_id.find({}, {"username": 1,})) #Find all username in collection
        array_username = list(collection_find_username[0]['username']) #Get just the array

        for i in array_username:
            #Send first and second message when the free game title change
            title_description_1 = current_games_title1 + "\n\n<b>About:</b>\n" + current_games_description1 # Send title, description, start date and price first current game
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
        current_games_title2 = response['games'][1]['title'] # Second title current game
        current_games_images2 = response['games'][1]['mainImage'] # Second image current game
        current_games_description2 = response['games'][1]['description'] # Second description current game

        collection_find_username = list(collection_id.find({}, {"username": 1,})) #Find all username in collection
        array_username = list(collection_find_username[1]['username']) #Get the array
        for i in array_username:
            title_description_2 = current_games_title2 + "\n\n<b>About:</b>\n" + current_games_description2 # Send title, description, start date and price second current game
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

def notification_game3(collection_game, collection_id, bot,):
    try:
        print("Try to send third game")
        #All information for second game
        current_games_title3 = response['games'][1]['title'] # Third title current game
        current_games_images3 = response['games'][1]['mainImage'] # Third image current game
        current_games_description3 = response['games'][1]['description'] # Third description current game

        collection_find_username = list(collection_id.find({}, {"username": 1,})) #Find all username in collection
        array_username = list(collection_find_username[1]['username']) #Get the array
        for i in array_username:
            title_description_3 = current_games_title3 + "\n\n<b>About:</b>\n" + current_games_description3 # Send title, description, start date and price Third current game
            img_3 = bot.send_photo(i, current_games_images3) # Send image Third current games
            send_message = bot.send_message(i, title_description_3, parse_mode="HTML") # Send all
            
        #Update Collection with new game
        send_game3 = {"Game 3": current_games_title3}
        find_document_game3 = list(collection_game.find({}, {"_id": 1}))
        array_game3 = find_document_game3[2]["_id"]
        sendata2 = collection_game.update_one({'_id':ObjectId(array_game3)}, {"$set": send_game3}, upsert=False)
    except:
        print("An error occurred")
        recheck_game(collection_game=collection_game, collection_id=collection_id, bot=bot)