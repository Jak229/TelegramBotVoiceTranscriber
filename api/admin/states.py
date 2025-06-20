from aiogram.fsm.state import State, StatesGroup


class AddAdmin(StatesGroup):
    """
    FSM states for adding a new admin.

    States:
        id: Waiting for the user ID to grant admin rights.
    """
    id = State()


class DeleteAdmin(StatesGroup):
    """
    FSM states for deleting an admin.

    States:
        id: Waiting for the user ID to revoke admin rights.
    """
    id = State()


class MailingList(StatesGroup):
    """
    FSM states for creating and sending a mailing list.

    States:
        text: Waiting for the mailing text.
        has_image: Waiting for the admin to choose if an image will be attached.
        image_id: Waiting for the image to be sent.
        confirm: Waiting for confirmation to send the mailing.
    """
    text = State()
    has_image = State()
    image_id = State()
    confirm = State()
