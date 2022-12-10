from bson.objectid import ObjectId
import os
OBJECTID_idlist = os.getenv('OBJECTID_idlist')

def subscribe_command(message, bot, collection_id):
    #Register the user
    chat_id = message.chat.id
    send_message = bot.send_message(chat_id, "✅ You have been successfully subscribed to Epic Games Store Free Games notifications!")
    #Get the ids of all users who write /subscribe
    take_id = message.from_user.id
    collection_id.update_one(
        { "_id": ObjectId(OBJECTID_idlist)},
            {
                "$push": { "username": take_id }
            }
    )