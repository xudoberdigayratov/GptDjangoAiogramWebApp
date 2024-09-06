from datetime import datetime

from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.filters.command import CommandStart
from aiogram.types import Message
from asgiref.sync import sync_to_async

from tgbot.bot.loader import bot
from tgbot.bot.utils.gptApi import gpt_api
from tgbot.models import Users, Chat

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    answer_web_app_keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Tarxni ko\'rish',
                                           web_app=types.WebAppInfo(
                                               url=f"https://73c9-84-54-115-212.ngrok-free.app/{user_id}/"))
            ]
        ]
    )
    user_exists = await sync_to_async(Users.objects.filter(user_id=user_id).first)()

    if not user_exists:
        await sync_to_async(Users.objects.create)(user_id=user_id, name=user_name)
    else:
        if user_exists.lasted_at.day != datetime.now().day:
            user_exists.lasted_at = datetime.now()
            await sync_to_async(user_exists.save)()

    await message.answer(
        """Salom, men ChatGPT botiman. Men OpenAI tomonidan yaratilganman. 
Men sizga savollarga javob berishga yordam bera olaman. Menga har qanday savol bering!""",
        reply_markup=answer_web_app_keyboard)


@router.message(StateFilter(None), F.text)
async def chatgpt_handler(message: Message):
    await bot.send_chat_action(chat_id=message.chat.id, action='TYPING')
    data = await gpt_api(message.text)
    response = ""
    if not data['error']:
        response = data['answer']
        # await message.answer(response, parse_mode='MARKDOWN')
    else:
        response = "Kechirasiz, qandaydir xatolik yuz berdi!"

    await sync_to_async(Chat.objects.create)(user_id=message.from_user.id, message=message.text, answer=response)
    await message.answer(response, parse_mode='MARKDOWN')
