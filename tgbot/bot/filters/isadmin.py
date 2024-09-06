from aiogram.filters import BaseFilter
from aiogram.types import Message

from chatGptProject.settings import ADMINS


class IsAdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return str(message.from_user.id) in ADMINS or message.from_user.id in ADMINS
