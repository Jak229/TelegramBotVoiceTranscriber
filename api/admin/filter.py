from aiogram.filters import BaseFilter
from api.dependencies import user_service


class IsAdminFilter(BaseFilter):
    """
    Filter to check if the user is an admin.

    This filter uses the user_service to determine if the user
    who sent the message or callback is an administrator.

    Methods:
        __call__(message): Returns True if the user is admin, otherwise False.
    """
    def __init__(self):
        self.user_service = user_service()

    async def __call__(self, message) -> bool:
        """
        Check if the user is an admin.

        Args:
            message: The incoming message or callback query.

        Returns:
            bool: True if the user is admin, False otherwise.
        """
        user = await self.user_service.find_one_user(message.from_user.id)
        if user and user.admin:
            return True
        return False
