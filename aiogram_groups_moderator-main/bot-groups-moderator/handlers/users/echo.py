from aiogram import types
from filters import IsPrivate

from loader import dp
import wikipedia

# Echo bot
@dp.message_handler(IsPrivate(), state=None)
async def bot_echo(message: types.Message):
    # print(message.chat.id)
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bunday malumot topilmadi")
        