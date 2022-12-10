from bson.objectid import ObjectId

def subscribe_command(message, bot, collection_id):
    chat_id = message.chat.id #Get chat id
    send_message = bot.send_message(chat_id, "✅ You have been successfully subscribed to Epic Games Store Free Games notifications!") #Send message
    #Get the ids of all users who write /subscribe
    take_id = message.from_user.id #Get user id
    collection_find_username = list(collection_id.find({}, {"username": 1,})) #Find all username in collection
    print(collection_find_username)
    array_username = list(collection_find_username[0]["username"]) #Get just the array
    print(array_username)
    #Insert the id of the user who writes /subscribe in the database
    collection_id.update_one(
        { "_id": ObjectId(array_username)},
            {
                "$push": { "username": take_id }
            }
    )