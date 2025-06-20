from config.lang import KEY_LANG
from config.config import ADMIN_USERNAME, HAS_CHANNEL, CHANNEL_USERNAME
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


def main_menu_keyboard(lang: str):
    """
    Create the main menu reply keyboard.

    Args:
        lang (str): The language code.

    Returns:
        ReplyKeyboardMarkup: The main menu keyboard.
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f"🗣️ {KEY_LANG[lang]['profile']}"),
                KeyboardButton(text=f"📜 {KEY_LANG[lang]['help']}"),
                KeyboardButton(text=f"🌐 {KEY_LANG[lang]['info']}"),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def profile_inline_keyboard(lang: str, admin: bool = False):
    """
    Create the profile inline keyboard.

    Args:
        lang (str): The language code.
        admin (bool): Whether the user is an admin.

    Returns:
        InlineKeyboardMarkup: The profile keyboard with admin menu if applicable.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=KEY_LANG[lang]["language"], callback_data="language"
                )
            ],
            [InlineKeyboardButton(text=KEY_LANG[lang]["back"], callback_data="back")],
        ]
        + (
            [
                [
                    InlineKeyboardButton(
                        text=KEY_LANG[lang]["admin_menu"], callback_data="admin_menu"
                    )
                ]
            ]
            if admin
            else []
        )
    )
    return keyboard


def language_inline_keyboard(lang: str):
    """
    Create the language selection inline keyboard.

    Args:
        lang (str): The current language code.

    Returns:
        InlineKeyboardMarkup: The language selection keyboard.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=("✅ " if lang == "ru" else "") + "Русский", callback_data="ru"
                ),
                InlineKeyboardButton(
                    text=("✅ " if lang == "ua" else "") + "Українська",
                    callback_data="ua",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=("✅ " if lang == "de" else "") + "Deutsch", callback_data="de"
                ),
                InlineKeyboardButton(
                    text=("✅ " if lang == "fr" else "") + "Français",
                    callback_data="fr",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=("✅ " if lang == "es" else "") + "Español", callback_data="es"
                ),
                InlineKeyboardButton(
                    text=("✅ " if lang == "it" else "") + "Italiano",
                    callback_data="it",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=("✅ " if lang == "en" else "") + "English", callback_data="en"
                ),
                InlineKeyboardButton(
                    text=("✅ " if lang == "pl" else "") + "Polski", callback_data="pl"
                ),
            ],
            [
                InlineKeyboardButton(
                    text=("✅ " if lang == "pt" else "") + "Português",
                    callback_data="pt",
                ),
                InlineKeyboardButton(
                    text=("✅ " if lang == "tr" else "") + "Türkçe", callback_data="tr"
                ),
            ],
            [
                InlineKeyboardButton(
                    text=("✅ " if lang == "ro" else "") + "Română", callback_data="ro"
                ),
            ],
            [
                InlineKeyboardButton(text=KEY_LANG[lang]["back"], callback_data="back"),
            ],
        ]
    )
    return keyboard


def help_inline_keyboard(lang: str):
    """
    Create the help inline keyboard.

    Args:
        lang (str): The language code.

    Returns:
        InlineKeyboardMarkup: The help keyboard.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=KEY_LANG[lang]["back"], callback_data="back")]
        ]
    )
    return keyboard


def info_bot_inline_keyboard(lang: str):
    """
    Create the info/about bot inline keyboard.

    Args:
        lang (str): The language code.

    Returns:
        InlineKeyboardMarkup: The info/about bot keyboard.
    """
    row = [
        InlineKeyboardButton(
            text=KEY_LANG[lang]["admin"], url="https://t.me/" + ADMIN_USERNAME
        )
    ]
    if HAS_CHANNEL:
        row.append(
            InlineKeyboardButton(
                text=KEY_LANG[lang]["channel"], url="https://t.me/" + CHANNEL_USERNAME
            )
        )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            row,
            [InlineKeyboardButton(text=KEY_LANG[lang]["back"], callback_data="back")],
        ]
    )
    return keyboard
