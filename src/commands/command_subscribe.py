from bson.objectid import ObjectId
import os

def subscribe_command(message, bot, collection_id):
    chat_id = message.chat.id #Get chat id
    send_message = bot.send_message(chat_id, "✅ You have been successfully subscribed to Epic Games Store Free Games notifications!") #Send message
    #Get the ids of all users who write /subscribe
    take_id = message.from_user.id #Get user id
    #Insert the id of the user who writes /subscribe in the database
    find_document_username = list(collection_id.find({}, {"_id": 1}))
    array_username = find_document_username[0]["_id"]
    collection_id.update_one(
        { "_id": ObjectId(array_username)},
            {
                "$push": { "username": take_id }
            }
    )