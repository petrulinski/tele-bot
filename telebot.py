import telebot
import json
import random
from datetime import datetime, timedelta

TOKEN = " " #Put your token
bot = telebot.TeleBot(TOKEN)

RATINGS_FILE = 'ratings.json'

#Load ratings from a file, if it exists
try:
    with open(RATINGS_FILE, 'r') as file:
        ratings = json.load(file)
except FileNotFoundError:
    ratings = {}

#Storing ratings in a file
def save_ratings():
      with open(RATINGS_FILE, 'w') as file:
        json.dump(ratings, file)

############################# RATING_SYSTEM ##########################

def get_username(user_id):
    user = bot.get_chat_member(chat_id=user_id, user_id=user_id).user
    return f"@{user.username}" if user.username else user.first_name

def get_rating_message(user_name, new_rating):
    return f"You have a change of ePoints! Balance {user_name}: {new_rating}"

def get_stats_message():
    sorted_ratings = sorted(ratings.items(), key=lambda x: x[1], reverse=True)
    stats_message = "User stats:\n"
    for user_id, rating in sorted_ratings:
        user_name = get_username(user_id)
        stats_message += f"{user_name}: {rating} ePoint \n"
    return stats_message

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Greetings! My name is ePointmeter. I am a bot specially designed for your group. Please, use this command to answer on message '+', '-', '👍', '👎' or '😂'. to change the rating.")

@bot.message_handler(commands=['deletewebhook'])
def delete_webhook(message):
    bot.delete_webhook()
    bot.reply_to(message, "Webhook is deleted. Now you can use getUpdates.")

@bot.message_handler(commands=['stats'])
def show_stats(message):
    stats_message = get_stats_message()
    bot.reply_to(message, stats_message)

@bot.message_handler(commands=['+', '👍', '😂'])
def add_rating(message):
    try:
        user_to_rate = message.reply_to_message.from_user.id if message.reply_to_message else None
        if user_to_rate == bot.get_me().id or user_to_rate == message.from_user.id:
            bot.reply_to(message, "You cannot give/take point to me.")
            return
        user_name = get_username(user_to_rate)

        rating_change = 1  # default for '+', '👍', '😂'
        if message.text.startswith('/+'):
            rating_change = int(message.text.split()[1]) if len(message.text.split()) > 1 else 1

        current_rating = ratings.get(user_to_rate, 0)
        new_rating = current_rating + 1
        ratings[user_to_rate] = new_rating
        bot.reply_to(message, get_rating_message(user_name, new_rating))
    except AttributeError:
        bot.reply_to(message, "Please, use this command to answer on message '+'.")

@bot.message_handler(commands=['-', '👎'])
def subtract_rating(message):
    try:
        user_to_rate = message.reply_to_message.from_user.id if message.reply_to_message else None
        if user_to_rate == bot.get_me().id or user_to_rate == message.from_user.id:
            bot.reply_to(message, "You cannot give/take point to me.")
            return
        user_name = get_username(user_to_rate)

        current_rating = ratings.get(user_to_rate, 0)
        new_rating = current_rating - 1  # Reduce the rating by -1

        ratings[user_to_rate] = new_rating
        bot.reply_to(message, get_rating_message(user_name, new_rating))
    except AttributeError:
        bot.reply_to(message, "Please, use this command to answer on message '-'.")

@bot.message_handler(func=lambda message: message.text in {"+", "-", "👍", "👎", "😂"})
def handle_plus_minus(message):
    try:
        user_to_rate = message.reply_to_message.from_user.id if message.reply_to_message else None
        if user_to_rate == bot.get_me().id or user_to_rate == message.from_user.id:
            bot.reply_to(message, "You cannot give/take point to me.")
            return
        user_name = get_username(user_to_rate)
        current_rating = ratings.get(user_to_rate, 0)
        
        if message.text in {"+", "👍", "😂"}:
            new_rating = current_rating + 1
        else:
            new_rating = max(-99, current_rating - 1)
            
        ratings[user_to_rate] = new_rating
        save_ratings()  # Saving ratings in a file
        bot.reply_to(message, get_rating_message(user_name, new_rating))
    except AttributeError:
        bot.reply_to(message, "Please, use this command to answer on message '+', '-', '👍', '👎' or '😂'.")


if __name__ == "__main__":
    bot.delete_webhook()
    bot.polling(none_stop=True)
