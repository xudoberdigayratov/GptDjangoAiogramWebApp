import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.session.middlewares.request_logging import logger
from django.core.management.base import BaseCommand

from tgbot.bot.loader import dp, bot


class Command(BaseCommand):
    help = 'Run bot in polling'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Bot started!"))
        try:
            main()
        except KeyboardInterrupt:
            self.stdout.write(self.style.NOTICE("Bot stopped!"))


def setup_handlers(dispatcher: Dispatcher) -> None:
    """HANDLERS"""
    from tgbot.bot.handlers import setup_routers

    dispatcher.include_router(setup_routers())


async def setup_aiogram(dispatcher: Dispatcher, bot: Bot) -> None:
    logger.info("Configuring aiogram")
    setup_handlers(dispatcher=dispatcher)
    logger.info("Configured aiogram")


async def aiogram_on_startup_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    logger.info("Starting polling")
    await setup_aiogram(bot=bot, dispatcher=dispatcher)
    await bot.delete_webhook(drop_pending_updates=True)


def main():
    """CONFIG"""
    dp.startup.register(aiogram_on_startup_polling)
    asyncio.run(dp.start_polling(bot, close_bot_session=True))

    # allowed_updates=['message', 'chat_member']
