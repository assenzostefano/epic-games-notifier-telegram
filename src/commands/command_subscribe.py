from bson.objectid import ObjectId
import os

def subscribe_command(message, bot, collection_id, OBJECTID_idlist):
    chat_id = message.chat.id #Get chat id
    send_message = bot.send_message(chat_id, "✅ You have been successfully subscribed to Epic Games Store Free Games notifications!") #Send message
    #Get the ids of all users who write /subscribe
    take_id = message.from_user.id #Get user id
    #Insert the id of the user who writes /subscribe in the database
    collection_id.update_one(
        { "_id": ObjectId(OBJECTID_idlist)},
            {
                "$push": { "username": take_id }
            }
    )