def start_command(message, bot):
    chat_id = message.chat.id #Get chat id
    #Send message
    messageText = "✋ Welcome to <b>Epic Games Notifier</b>\n\n📱 You will be notified every week when there are new free games in the Epic Games Store. \n\n👨‍💻 Created and developed by @Stef58_Official"
    bot.send_message(chat_id, messageText, parse_mode="HTML")