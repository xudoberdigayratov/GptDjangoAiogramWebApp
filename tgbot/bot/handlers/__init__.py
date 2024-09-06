from aiogram import Router

from tgbot.bot.filters import ChatPrivateFilter


def setup_routers() -> Router:
    from .users import start

    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating
    start.router.message.filter(ChatPrivateFilter())
    # admin.router.message.filter(IsAdminFilter())

    router.include_routers(start.router,

                           )

    return router
