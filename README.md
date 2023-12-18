## Overview

This document provides a breakdown of the main components and functionalities of the code.

### Token and Initialization:

- In order to run the Telegram bot successfully, you need to obtain a Telegram Bot Token.
- An instance of the `TeleBot` class from the `telebot` library is created with the specified token.

### Ratings Storage:

- Ratings are stored in a JSON file named 'ratings.json'.
- The script attempts to load existing ratings from the file. If the file doesn't exist, it initializes an empty ratings dictionary.

### Rating System Functions:

1. **get_username(user_id):**
   - Retrieves the username or first name of a user given their Telegram user ID.

2. **get_rating_message(user_name, new_rating):**
   - Generates a message indicating the change in ePoints for a user.

3. **get_stats_message():**
   - Creates a message displaying the user statistics and ratings in descending order.

### Command Handlers:

- **/start and /help:**
  - Displays a welcome message introducing the bot and its purpose.

- **/deletewebhook:**
  - Deletes the webhook to enable the use of `getUpdates`.

- **/stats:**
  - Displays the user statistics and ratings in the group.

- **Commands like +, -, '👍', '👎', '😂':**
  - Allow users to give or take points from other users.

### Main Execution:

- The script starts by deleting the webhook.
- Initiates continuous polling (`bot.polling(none_stop=True)`) to listen for incoming messages and commands.

### Rating Changes:

- Users can change ratings by replying to a message with commands like '+', '-', '👍', '👎', or '😂'.
- The script tracks the ratings and updates the 'ratings.json' file accordingly.

### How to work with telebot

In order to run the Telegram bot successfully, you need to obtain a Telegram Bot Token. Follow these steps to create and obtain the token:

1. **Create a Telegram Bot:**
   - Start a chat with [@BotFather](https://t.me/BotFather) on Telegram.
   - Use the `/newbot` command to create a new bot.
   - Follow the instructions to choose a name and username for your bot.

2. **Get the Token:**
   - Once your bot is created, BotFather will provide you with a unique API token.
   - Copy the token provided by BotFather.

3. **Replace the Token in the Code:**
   - Open your script in the code editor.
   - Locate the line `TOKEN = " " #Put your token`.
   - Replace the empty string (`" "`) with the token you obtained from BotFather.

Here's an example of how the `TOKEN` line should look after replacing:
   ```python
   TOKEN = "your-telegram-bot-token"

**Bots FAQ - https://core.telegram.org/bots/faq#how-do-i-create-a-bot**

### Note:

- The script uses the `telebot` library, assumed to be installed (`pip install pyTelegramBotAPI`).
- The Telegram bot token needs to be obtained from the BotFather on Telegram and replaced in the `TOKEN` variable for the script to work.
- Proper error handling is implemented to ensure the robustness of the bot.
- Keep your Telegram Bot Token confidential. Do not share it publicly or expose it in your code repositories.
- If you suspect your token has been compromised, you can generate a new one by talking to BotFather and updating it in your code.
