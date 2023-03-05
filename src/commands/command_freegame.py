import requests

def freegame_command(message, bot):
    chat_id = message.chat.id #Get chat id
    #Connect to API
    try:
        url = "https://minty.apexie.dev/v1/epicfreegames" #URL API
        response = requests.get(url).json() #API in JSON
        #Take data from API (Current Game 1)
        image_currentgames1 = response['games'][0]['mainImage'] # First image current games
        current_games1 = response['games'][0]['title'] # First title current games
        current_games_description1 = response['games'][0]['description'] # First description current games
        #Send notification to user (Current Game 1)
        title_description_1 = current_games1 + "\n\n<b>About:</b>\n" + current_games_description1 # Send title, description, start date and price first current game
        img_1 = bot.send_photo(message.chat.id, image_currentgames1) # Send image first current games
        send_message = bot.send_message(chat_id, title_description_1, parse_mode="HTML") # Send all
    
        try:
            #Take data from API (Current Game 2)
            image_currentgames2 = response['games'][1]['mainImage'] # First image current games
            current_games2 = response['games'][1]['title'] # First title current games
            current_games_description2 = response['games'][1]['description'] # First description current games

            title_description_2 = current_games2 + "\n\n<b>About:</b>\n" + current_games_description2 # Send title, description, start date and price second current game
            img_2 = bot.send_photo(message.chat.id, image_currentgames2) # Send image second current games
            send_message = bot.send_message(chat_id, title_description_2, parse_mode="HTML") # Send all
        except:
            print("Second current game not found")

        #Try search third game
        try:
            #Take data from API (Current Game 3)
            image_currentgames3 = response['games'][2]['mainImage'] # First image current games
            current_games3 = response['games'][2]['title'] # First title current games
            current_games_description3 = response['games'][2]['description'] # First description current games

            #Send notification to user (Current Game 3)
            title_description_3 = current_games3 + "\n\n<b>About:</b>\n" + current_games_description3 # Send title, description, start date and price second current game
            img_3 = bot.send_photo(message.chat.id, image_currentgames3) # Send image second current games
            send_message = bot.send_message(chat_id, title_description_3, parse_mode="HTML") # Send all
        except IndexError:
            print("No third game")
    except:
        bot.send_message(chat_id, "An error occurred")
