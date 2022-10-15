from aiogram import Bot, Dispatcher, types
import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio

from parser import subjects_week

from config import API_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("я дам тебе расписание")


@dp.message_handler(commands=['schedule'])
async def send_schedule(message: types.Message):
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keybord.add("Понедельник", "Вторник", "Среда",
                "Четверг", "Пятница", "Суббота")
    await message.reply("Выберите день", reply_markup=keybord)


@dp.message_handler()
async def echo(message: types.Message):
    temp = ""
    if message.text == "Понедельник":
        temp = "monday"
    elif message.text == "Вторник":
        temp = "tuesday"
    elif message.text == "Среда":
        temp = "wednesday"
    elif message.text == "Четверг":
        temp = "thursday"
    elif message.text == "Пятница":
        temp = "friday"
    elif message.text == "Суббота":
        temp = "saturday"
    iter = 1
    for i in subjects_week[temp]:
        await message.answer(f"{iter}. {i}")
        iter += 1


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
