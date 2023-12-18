# Bot "ePointmeter" for Telegram chat groups.

This Python script implements a Telegram bot named "ePointmeter" designed for group interactions. The bot allows users to give and take points to/from each other using commands like '+', '-', '👍', '👎', or '😂'. The points are tracked and displayed as ratings for each user in the group.

Here's a breakdown of the main components and functionalities of the code:

Token and Initialization:

The Telegram bot token is defined as TOKEN.
An instance of the TeleBot class from the telebot library is created with the specified token.
Ratings Storage:

Ratings are stored in a JSON file named 'ratings.json'.
The script attempts to load existing ratings from the file, and if the file doesn't exist, it initializes an empty ratings dictionary.
Rating System Functions:

get_username(user_id): Retrieves the username or first name of a user given their Telegram user ID.
get_rating_message(user_name, new_rating): Generates a message indicating the change in ePoints for a user.
get_stats_message(): Creates a message displaying the user statistics and ratings in descending order.
Command Handlers:

/start and /help: Displays a welcome message introducing the bot and its purpose.
/deletewebhook: Deletes the webhook to enable the use of getUpdates.
/stats: Displays the user statistics and ratings in the group.
Commands like +, '-', '👍', '👎', '😂': Allow users to give or take points from other users.
Main Execution:

The script starts by deleting the webhook and then initiates continuous polling (bot.polling(none_stop=True)) to listen for incoming messages and commands.
Rating Changes:

Users can change ratings by replying to a message with commands like '+', '-', '👍', '👎', or '😂'.
The script tracks the ratings and updates the 'ratings.json' file accordingly.
Note: The script uses the telebot library, which is assumed to be installed (pip install pyTelegramBotAPI). The Telegram bot token needs to be obtained from the BotFather on Telegram and replaced in the TOKEN variable for the script to work. Additionally, proper error handling is implemented to ensure the robustness of the bot.
