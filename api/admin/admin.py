from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from config.lang import LANG
from dp import bot

from api.dependencies import user_service
from api.admin.filter import IsAdminFilter
from api.admin.keyoards import (
    admin_menu_keyboard,
    cancel_keyboard,
    has_image_keyboard,
    confirm_send_keyboard,
)
from api.admin.states import AddAdmin, DeleteAdmin, MailingList


admin = Router()


# Admin menu
@admin.callback_query(IsAdminFilter(), F.data == "admin_menu")
async def admin_menu(call: CallbackQuery, user_service=user_service()):
    """
    Handles the admin menu callback query.

    This asynchronous function retrieves the user information based on the Telegram user's ID,
    then edits the current message to display the admin menu in the user's language with the appropriate keyboard.

    Args:
        call (CallbackQuery): The callback query from the Telegram bot.
        user_service (UserService, optional): The service used to interact with user data. Defaults to user_service().

    Returns:
        None
    """
    user = await user_service.find_user_by_id(call.from_user.id)
    await call.message.edit_text(
        LANG[user[0].lang]["admin_menu"],
        reply_markup=admin_menu_keyboard(user[0].lang),
    )


# Enter admin ID for adding
@admin.callback_query(IsAdminFilter(), F.data == "add_admin")
async def admin_enter_admin_id(call: CallbackQuery, state, user_service=user_service()):
    """
    Prompt the admin to enter the user ID to grant admin rights.

    Args:
        call (CallbackQuery): The callback query from the admin.
        state: The FSM state.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(call.from_user.id)
    await call.message.edit_text(
        LANG[user[0].lang]["enter_admin"],
        reply_markup=cancel_keyboard(user[0].lang),
    )
    await state.set_state(AddAdmin.id)


# Adding admin
@admin.message(IsAdminFilter(), F.text, StateFilter(AddAdmin.id))
async def add_admin(m: Message, state, user_service=user_service()):
    """
    Add a new admin by user ID.

    Args:
        m (Message): The message containing the user ID.
        state: The FSM state.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(m.from_user.id)
    if m.text.isdigit():
        await user_service.update_user(int(m.text), admin=True)
        await m.answer(LANG[user[0].lang]["success_add_admin"])
        await state.clear()
    else:
        await m.answer(LANG[user[0].lang]["enter_admin"])


# Enter admin ID for deleting
@admin.callback_query(IsAdminFilter(), F.data == "delete_admin")
async def enter_admin_id(call: CallbackQuery, state, user_service=user_service()):
    """
    Prompt the admin to enter the user ID to revoke admin rights.

    Args:
        call (CallbackQuery): The callback query from the admin.
        state: The FSM state.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(call.from_user.id)
    await call.message.edit_text(
        LANG[user[0].lang]["enter_admin"],
        reply_markup=cancel_keyboard(user[0].lang),
    )
    await state.set_state(DeleteAdmin.id)


# Deleting admin
@admin.message(IsAdminFilter(), F.text, StateFilter(DeleteAdmin.id))
async def delete_admin(m: Message, state, user_service=user_service()):
    """
    Remove admin rights from a user by user ID.

    Args:
        m (Message): The message containing the user ID.
        state: The FSM state.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(m.from_user.id)
    if m.text.isdigit():
        await user_service.update_user(int(m.text), admin=False)
        await m.answer(LANG[user[0].lang]["success_delete_admin"])
        await state.clear()
    else:
        await m.answer(LANG[user[0].lang]["enter_admin"])


### Mailing list


# Enter text for mailing list
@admin.callback_query(IsAdminFilter(), F.data == "mailing_list")
async def enter_mailing_list(call: CallbackQuery, state, user_service=user_service()):
    """
    Prompt the admin to enter the text for the mailing list.

    Args:
        call (CallbackQuery): The callback query from the admin.
        state: The FSM state.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(call.from_user.id)
    await call.message.edit_text(
        LANG[user[0].lang]["enter_text"],
        reply_markup=cancel_keyboard(user[0].lang),
    )
    await state.set_state(MailingList.text)


# Check if has image
@admin.message(IsAdminFilter(), F.text, StateFilter(MailingList.text))
async def send_text(m: Message, state, user_service=user_service()):
    """
    Ask the admin if the mailing list message should include an image.

    Args:
        m (Message): The message containing the mailing text.
        state: The FSM state.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(m.from_user.id)
    await m.answer(
        LANG[user[0].lang]["has_image"], reply_markup=has_image_keyboard(user[0].lang)
    )
    await state.set_state(MailingList.has_image)
    await state.update_data(text=m.text)


# Has image
@admin.message(
    IsAdminFilter(), F.text.startswith("🟢"), StateFilter(MailingList.has_image)
)
async def has_image(m: Message, state, user_service=user_service()):
    """
    Prompt the admin to send an image for the mailing list.

    Args:
        m (Message): The message indicating an image will be sent.
        state: The FSM state.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(m.from_user.id)
    await m.answer(
        LANG[user[0].lang]["send_image"],
        reply_markup=cancel_keyboard(user[0].lang),
    )
    await state.set_state(MailingList.image_id)
    await state.update_data(has_image=True)


# Catch image
@admin.message(IsAdminFilter(), F.photo, StateFilter(MailingList.image_id))
async def send_image(m: Message, state, user_service=user_service()):
    """
    Handle the image sent by the admin for the mailing list.

    Args:
        m (Message): The message containing the photo.
        state: The FSM state.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(m.from_user.id)
    data = await state.get_data()
    await m.answer_photo(
        m.photo[-1].file_id,
        caption=data["text"],
        reply_markup=confirm_send_keyboard(user[0].lang),
    )
    await state.set_state(MailingList.confirm)
    await state.update_data(
        image_id=m.photo[-1].file_id, has_image=True, text=data["text"]
    )


# No image
@admin.message(
    IsAdminFilter(), F.text.startswith("🔴"), StateFilter(MailingList.has_image)
)
async def no_image(m: Message, state, user_service=user_service()):
    """
    Handle the case when the admin chooses not to send an image.

    Args:
        m (Message): The message indicating no image will be sent.
        state: The FSM state.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(m.from_user.id)
    data = await state.get_data()
    await m.answer(
        data["text"],
        reply_markup=confirm_send_keyboard(user[0].lang),
    )
    await state.set_state(MailingList.text)
    await state.update_data(has_image=False, text=data["text"])


# Confirm sending
@admin.callback_query(
    IsAdminFilter(), F.data == "send"
)  # StateFilter(MailingList.confirm))
async def confirm_send(call: CallbackQuery, state, user_service=user_service()):
    """
    Send the mailing list message to all users.

    Args:
        call (CallbackQuery): The callback query to confirm sending.
        state: The FSM state.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(call.from_user.id)
    all_users = await user_service.get_all_users()
    data = await state.get_data()

    suc_count = 0
    error_count = 0

    if data["has_image"]:
        try:
            for u in all_users:
                await bot.send_photo(
                    chat_id=u.id,
                    photo=data["image_id"],
                    caption=data["text"],
                )
                suc_count += 1
        except Exception as e:
            error_count += 1

    else:
        try:
            for u in all_users:
                await bot.send_message(
                    chat_id=u.id,
                    text=data["text"],
                )
                suc_count += 1
        except Exception as e:
            error_count += 1

    await call.message.answer(
        LANG[user[0].lang]["mail_list_end"].format(suc_count, error_count),
        reply_markup=ReplyKeyboardRemove(),
    )
    await call.message.answer(
        LANG[user[0].lang]["admin_menu"],
        reply_markup=admin_menu_keyboard(user[0].lang),
    )
    await state.clear()


# Cancel
@admin.callback_query(IsAdminFilter(), F.data == "cancel")
async def cancel(call: CallbackQuery, state, user_service=user_service()):
    """
    Cancel the current admin operation and return to the admin menu.

    Args:
        call (CallbackQuery): The callback query to cancel.
        state: The FSM state.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(call.from_user.id)
    await call.message.edit_text(
        LANG[user[0].lang]["admin_menu"],
        reply_markup=admin_menu_keyboard(user[0].lang),
    )
    await state.clear()


@admin.callback_query(IsAdminFilter(), F.data == "back_admin_menu")
async def back_admin_menu(call: CallbackQuery, state, user_service=user_service()):
    """
    Return to the admin menu from a sub-menu.

    Args:
        call (CallbackQuery): The callback query to go back.
        state: The FSM state.
        user_service: The user service dependency.
    """
    user = await user_service.find_user_by_id(call.from_user.id)
    await call.message.edit_text(
        LANG[user[0].lang]["admin_menu"],
        reply_markup=admin_menu_keyboard(user[0].lang),
    )
    await state.clear()
