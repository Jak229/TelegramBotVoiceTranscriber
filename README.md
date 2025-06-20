# Telegram bot Voice Transcriber

This bot is a multifunctional Telegram bot, implemented in Python using the modern asynchronous framework **aiogram v3**. It is designed to work with voice messages, manage users and provide administrative functions through a userfriendly interface.

## Main features of the bot

**Main menu**: The user gets a localized menu using a regular keyboard (ReplyKeyboardMarkup), where he can select a profile, help or information about the bot.
**User profile**: Displays information about the user, supports multilingualism.
**Help and information**: Quick access to reference materials and information about the bot.
**Administrative menu**: A separate menu has been implemented for administrators with the ability to add/remove admins and send messages to all users.
**Multilingualism**: All keyboards and messages support several languages (en, ua, ru, sp, pl, de, it, fr), language selection is implemented through inline buttons.
**Flood control**: Builtin middleware limits the number of requests from a user for a certain period of time.
**Database handling**: SQLAlchemy is used (asynchronous mode) to store and manage users and administrators.
**Modular architecture**: The code is divided into modules for ease of support and expansion (separate files for keyboards, filters, middleware, models, repositories, etc.).

## Dependencies

**aiogram v3** — the main framework for creating a Telegram bot.
**SQLAlchemy** — asynchronous work with the database (SQLite).
**pydantic** — for data validation and working with models.
**asyncio** — for asynchronous launch and operation of the bot.
**logging** — for logging events and errors.

You also need to install **ffmpeg** to convert voice messages to the required format.



## Installation
1. Clone the repo
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Edit **config.py**:
    ```
    BOT_TOKEN=your_bot_token 
    ADMIN=your id
    ```
4. Make sure `ffmpeg` is installed and available in your system path
5. Run the bot:
    ```bash
    python bot.py
    ```

