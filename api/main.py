from dp import bot
from aiogram import F, Router
from api.model import Transcriber
from aiogram.filters import CommandStart
from api.dependencies import user_service

from api.midleware import FloodControlMiddleware
from aiogram.types import Message, CallbackQuery
from config.lang import LANG, supported_languages
from config.config import ADMIN
from keyboard.keyboard import (
    main_menu_keyboard,
    profile_inline_keyboard,
    language_inline_keyboard,
    help_inline_keyboard,
    info_bot_inline_keyboard,
)


users = Router()
users.message.middleware(FloodControlMiddleware(limit=20, interval=60))

# Start command handler
@users.message(CommandStart())
async def start_message(m: Message, user_service=user_service()):
    """
    Handle the /start command.

    Registers a new user if not already in the database and sends the start message with the main menu.

    Args:
        m (Message): The incoming message object.
        user_service: The user service dependency.
    """
    if not await user_service.find_one_user(m.from_user.id):
        await user_service.add_user(
            id=m.from_user.id,
            username=m.from_user.username if m.from_user.username else "",
            lang=m.from_user.language_code,
            admin=False if m.from_user.id != ADMIN else True,
        )

    user = await user_service.find_user_by_id(id=m.from_user.id)
    await m.reply(
        LANG[user[0].lang]["start"], reply_markup=main_menu_keyboard(user[0].lang)
    )

# Help command handler
@users.message(F.text.startswith("📜"))
async def help_message(m: Message, user_service=user_service()):
    """
    Handle the help command.

    Sends help information to the user.

    Args:
        m (Message): The incoming message object.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(id=m.from_user.id)

    if user:
        lang = user[0].lang
        await m.reply(LANG[lang]["help"], reply_markup=help_inline_keyboard(lang))

# Profile command handler
@users.message(F.text.startswith("🗣️"))
async def about_user_message(m: Message, user_service=user_service()):
    """
    Handle the profile command.

    Sends user profile information.

    Args:
        m (Message): The incoming message object.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(id=m.from_user.id)

    if user:
        await m.reply(
            LANG[user[0].lang]["profile_info"].format(
                user[0].id, user[0].username, user[0].lang, user[0].admin
            ),
            reply_markup=profile_inline_keyboard(user[0].lang, user[0].admin),
        )

# About bot command handler
@users.message(F.text.startswith("🌐"))
async def about_bot_message(m: Message, user_service=user_service()):
    """
    Handle the about bot command.

    Sends information about the bot and the number of users.

    Args:
        m (Message): The incoming message object.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(id=m.from_user.id)

    if user:
        all_users = await user_service.get_count_users()
        lang = user[0].lang
        await m.reply(
            LANG[lang]["count_users"].format(all_users),
            reply_markup=info_bot_inline_keyboard(lang),
        )

# Back call data handler
@users.callback_query(F.data == "back")
async def back_callback(call: CallbackQuery, user_service=user_service()):
    """
    Handle the back button callback.

    Returns the user to the start message.

    Args:
        call (CallbackQuery): The callback query object.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(id=call.from_user.id)
    if user:
        lang = user[0].lang
        await call.message.edit_text(LANG[lang]["start"])
        await call.answer()

# Language call data handler
@users.callback_query(F.data == "language")
async def language_callback(call: CallbackQuery, user_service=user_service()):
    """
    Handle the language selection callback.

    Shows the language selection menu.

    Args:
        call (CallbackQuery): The callback query object.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(id=call.from_user.id)
    if user:
        lang = user[0].lang
        await call.message.edit_text(
            LANG[lang]["lang"], reply_markup=language_inline_keyboard(lang)
        )
        await call.answer()

# Language change call data handler
@users.callback_query(F.data.in_(supported_languages))
async def language_callback(call: CallbackQuery, user_service=user_service()):
    """
    Handle the language change callback.

    Updates the user's language and shows updated profile info.

    Args:
        call (CallbackQuery): The callback query object.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(id=call.from_user.id)
    if user:
        lang = call.data
        await user_service.update_user(call.from_user.id, lang=lang)
        await call.answer(LANG[lang]["change_lang"].format(lang), show_alert=True)
        await call.message.edit_text(
            LANG[lang]["profile_info"].format(
                user[0].id, user[0].username, lang, user[0].admin
            ),
            reply_markup=profile_inline_keyboard(lang),
        )

# Voice message handler
@users.message(F.voice)
async def voice_message(m: Message, user_service=user_service()):
    """
    Handle incoming voice messages.

    Downloads the voice message, transcribes it, and sends the text back to the user.

    Args:
        m (Message): The incoming message object.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(id=m.from_user.id)
    lang = user[0].lang if user else "en"
    voice_id = m.voice.file_id
    file = await bot.get_file(voice_id)
    file_path = file.file_path

    await m.reply(LANG[lang]["wait_transcribe"])
    await bot.download_file(file_path, f"temp/{voice_id}.ogg")
    transcriber = Transcriber(f"temp/{voice_id}.ogg", lang=lang)

    try:
        text = transcriber.transcribe()
        await m.reply(text)
    except Exception as e:
        print(e)
        await m.reply(LANG[lang]["error_transcribe"])

    del transcriber
