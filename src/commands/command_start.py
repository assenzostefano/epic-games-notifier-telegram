def start_command(message, bot):
    chat_id = message.chat.id #Get chat id
    #Send message
    messageText = "ā Welcome to <b>Epic Games Notifier</b>\n\nš± You will be notified every week when there are new free games in the Epic Games Store. \n\nšØāš» Created and developed by @Stef58_Official"
    bot.send_message(chat_id, messageText, parse_mode="HTML")