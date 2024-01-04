from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import CHANNELS
from keyboards.inline.filters import check_button
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.misc import subcribe
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hello: {message.from_user.full_name}")
