import time
from typing import Dict
from config.lang import LANG
from api.dependencies import user_service

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject



# This middleware is used to limit the number of requests a user can make in a given time interval.
class FloodControlMiddleware(BaseMiddleware):
    """
    Middleware to limit the number of requests a user can make in a given time interval.
    Args:
        limit (int): Maximum number of requests allowed in the interval.
        interval (int): Time interval in seconds.
    """
    def __init__(self, limit: int = 5, interval: int = 1, user_service=user_service()):
        super().__init__()
        self.limit = limit
        self.interval = interval
        self.user_service = user_service
        self.user_requests: Dict[int, int] = {}

    async def __call__(self, handler, event, data):
        user_id = (
            getattr(event.from_user, "id", None)
            if hasattr(event, "from_user")
            else None
        )

        if user_id:
            user = await self.user_service.find_user_by_id(user_id)
            lang = user[0].lang if user else "en"

            now = time.time()
            # user_requests: Dict[int, List[float]]
            if user_id not in self.user_requests:
                self.user_requests[user_id] = []
            # Remove timestamps older than interval
            self.user_requests[user_id] = [
                t for t in self.user_requests[user_id] if now - t < self.interval
            ]
            if len(self.user_requests[user_id]) >= self.limit:
                await event.answer(LANG[lang]["flood"], show_alert=True)
                print(
                    f"Flood control triggered for user {user_id}. Limit: {self.limit}, Interval: {self.interval}"
                )
                return  # Don't call handler if flood detected
            self.user_requests[user_id].append(now)

        return await handler(event, data)
