from config.lang import KEY_LANG
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

# This file contains the keyboard functions for the admin panel of the bot.
def admin_menu_keyboard(lang: str):
    """
    Create the admin menu inline keyboard.

    Args:
        lang (str): The language code.

    Returns:
        InlineKeyboardMarkup: The admin menu keyboard.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🗣️ " + KEY_LANG[lang]["add_admin"],
                    callback_data="add_admin",
                ),
                InlineKeyboardButton(
                    text="🗣️ " + KEY_LANG[lang]["delete_admin"],
                    callback_data="delete_admin",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="📤 " + KEY_LANG[lang]["mailing_list"],
                    callback_data="mailing_list",
                )
            ],
            [InlineKeyboardButton(text=KEY_LANG[lang]["back"], callback_data="back")],
        ]
    )
    return keyboard

def cancel_keyboard(lang: str):
    """
    Create a cancel/back inline keyboard for admin actions.

    Args:
        lang (str): The language code.

    Returns:
        InlineKeyboardMarkup: The cancel/back keyboard.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=KEY_LANG[lang]["back"], callback_data="back_admin_menu"
                )
            ]
        ]
    )
    return keyboard


def has_image_keyboard(lang: str):
    """
    Create a reply keyboard to ask if the message should include an image.

    Args:
        lang (str): The language code.

    Returns:
        ReplyKeyboardMarkup: The keyboard with options for image or no image.
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🟢 " + KEY_LANG[lang]["has"]),
                KeyboardButton(text="🔴 " + KEY_LANG[lang]["no"]),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def confirm_send_keyboard(lang: str):
    """
    Create an inline keyboard to confirm or cancel sending a message.

    Args:
        lang (str): The language code.

    Returns:
        InlineKeyboardMarkup: The confirm/cancel keyboard.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=KEY_LANG[lang]["send"], callback_data="send"),
                InlineKeyboardButton(
                    text=KEY_LANG[lang]["cancel"], callback_data="cancel"
                ),
            ]
        ]
    )
    return keyboard
