import requests

def soon_command(message, bot):
    chat_id = message.chat.id
    try:
        url = "https://api.plenusbot.xyz/epic_games?country=IT"
        response = requests.get(url).json()
        # Title of future games
        image_futuregames1 = response['nextGames'][0]['keyImages'][0]['url'] # First image future games
        future_games1 = response['nextGames'][0]['title'] # First title future games
        future_games_description1 = response['nextGames'][0]['description'] # First description future games
        future_games_startdate1 = response['nextGames'][0]['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['startDate']
        future_games_price1 = response['nextGames'][0]['price']['totalPrice']['fmtPrice']['originalPrice']

        image_futuregames2 = response['nextGames'][1]['keyImages'][1]['url'] # Second image future games
        future_games2 = response['nextGames'][1]['title'] # Second title future games
        future_games_description2 = response['nextGames'][1]['description'] # Second description future games
        future_games_startdate2 = response['nextGames'][1]['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['startDate']
        future_games_price2 = response['nextGames'][1]['price']['totalPrice']['fmtPrice']['originalPrice']

        title_description_1 = future_games1 + "\n\n<b>About:</b>\n" + future_games_description1 + "\n" + "\n<b>Start Date:</b>\n" + future_games_startdate1 + "\n" + "\n<b>Price:</b>\n" + future_games_price1 + " → " + "Free" # Send title, description, start date and price first future game
        img_1 = bot.send_photo(message.chat.id, image_futuregames1) # Send image first future games
        send_message = bot.send_message(chat_id, title_description_1, parse_mode="HTML") # Send all

        title_description_2 = future_games2 + "\n\n<b>About:</b>\n" + future_games_description2 + "\n" + "\n<b>Start Date:</b>\n" + future_games_startdate2 + "\n" + "\n<b>Price:</b>\n" + future_games_price2 + " → " + "Free" # Send title, description, start date and price second future game
        img_2 = bot.send_photo(message.chat.id, image_futuregames2) # Send image second future games
        send_message = bot.send_message(chat_id, title_description_2, parse_mode="HTML") # Send all
    except:
        bot.send_message(chat_id, "An error has occurred, probably new games have not been revealed or there are problems with the API. \nWe apologize for the inconvenience")

    try:
        image_futuregames3 = response['nextGames'][0]['keyImages'][2]['url'] # Third image future games
        future_games3 = response['nextGames'][2]['title'] # Third title future games
        future_games_description3 = response['nextGames'][2]['description'] # Third description future games
        future_games_startdate3 = response['nextGames'][1]['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['startDate']
        future_games_price3 = response['nextGames'][1]['price']['totalPrice']['fmtPrice']['originalPrice']
        title_description_3 = future_games3 + "\n\n<b>About:</b>\n" + future_games_description3 + "\n" + "\n<b>Start Date:</b>\n" + future_games_startdate3 + "\n" + "\n<b>Price:</b>\n" + future_games_price3 + " → " + "Free" # Send title, description, start date and price second future game
        
        img_3 = bot.send_photo(message.chat.id, image_futuregames3) # Send image third future games
        send_message = bot.send_message(chat_id, title_description_3, parse_mode="HTML") # Send all
    except IndexError:
        print("No third game")