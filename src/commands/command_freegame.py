import requests

def freegame_command(message, bot):
    chat_id = message.chat.id
    url = "https://api.plenusbot.xyz/epic_games?country=IT"
    response = requests.get(url).json()
    image_currentgames1 = response['currentGames'][0]['keyImages'][0]['url'] # First image current games
    current_games1 = response['currentGames'][0]['title'] # First title current games
    current_games_description1 = response['currentGames'][0]['description'] # First description current games
    current_games_startdate1 = response['currentGames'][0]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate']
    current_games_endate1 = response['currentGames'][0]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate']
    current_games_price1 = response['currentGames'][0]['price']['totalPrice']['fmtPrice']['originalPrice']
    
    image_currentgames2 = response['currentGames'][1]['keyImages'][0]['url'] # First image current games
    current_games2 = response['currentGames'][1]['title'] # First title current games
    current_games_description2 = response['currentGames'][1]['description'] # First description current games
    current_games_startdate2 = response['currentGames'][1]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate']
    current_games_endate2 = response['currentGames'][1]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate']
    current_games_price2 = response['currentGames'][1]['price']['totalPrice']['fmtPrice']['originalPrice']

    #Send notification to user
    title_description_1 = current_games1 + "\n\n<b>About:</b>\n" + current_games_description1 + "\n" + "\n<b>Start Date:</b>\n" + current_games_startdate1 + "\n" + "\n<b>End Date:</b>\n" + current_games_endate1 + "\n" + "\n<b>Price:</b>\n" + current_games_price1 + " → " + "Free" # Send title, description, start date and price first current game
    img_1 = bot.send_photo(message.chat.id, image_currentgames1) # Send image first current games
    send_message = bot.send_message(chat_id, title_description_1, parse_mode="HTML") # Send all

    title_description_2 = current_games2 + "\n\n<b>About:</b>\n" + current_games_description2 + "\n" + "\n<b>Start Date:</b>\n" + current_games_startdate2 + "\n" + "\n<b>End Date:</b>\n" + current_games_endate2 + "\n" + "\n<b>Price:</b>\n" + current_games_price2 + " → " + "Free" # Send title, description, start date and price second current game
    img_2 = bot.send_photo(message.chat.id, image_currentgames2) # Send image second current games
    send_message = bot.send_message(chat_id, title_description_2, parse_mode="HTML") # Send all    

    try:
        image_currentgames3 = response['currentGames'][2]['keyImages'][0]['url'] # First image current games
        current_games3 = response['currentGames'][2]['title'] # First title current games
        current_games_description3 = response['currentGames'][2]['description'] # First description current games
        current_games_startdate3 = response['currentGames'][2]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate']
        current_games_endate3 = response['currentGames'][2]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate']
        current_games_price3 = response['currentGames'][2]['price']['totalPrice']['fmtPrice']['originalPrice']
        title_description_3 = current_games3 + "\n\n<b>About:</b>\n" + current_games_description3 + "\n" + "\n<b>Start Date:</b>\n" + current_games_startdate3 + "\n" + "\n<b>End Date:</b>\n" + current_games_endate3 + "\n" + "\n<b>Price:</b>\n" + current_games_price3 + " → " + "Free" # Send title, description, start date and price second current game
        img_3 = bot.send_photo(message.chat.id, image_currentgames3) # Send image second current games
        send_message = bot.send_message(chat_id, title_description_3, parse_mode="HTML") # Send all    
    except IndexError:
        print("No third game")