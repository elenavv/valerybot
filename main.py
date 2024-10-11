import asyncio
import logging
import sys
from os import getenv
from notmain import keep_alive

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
#для help photo
from aiogram import F
from aiogram.filters import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


TOKEN = "7625625092:AAGuCLiXpw58zvLyvMVSdqrld5Xi5jK8GCU"
dp = Dispatcher()

#реакция на команду старт
#ф-ция назв_функции(имя_переменной тип_данных)
@dp.message(CommandStart())
async def command_start_handler(message:Message):
    await message.answer(f"Привет, {message.from_user.full_name}!",reply_markup=keyboard)



#Создание кнопки
#from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
#from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup
#from aiogram.types import InlineKeyboardButton
#Отдельно создается клавиатура и на неё добавляется клавиши
button = KeyboardButton(text="👧Нажми меня")
button1 = KeyboardButton(text="▶️🧸Мимимишки")
button2 = KeyboardButton(text="▶️🐕Щенячий Патруль")
button3 = KeyboardButton(text="▶️🚜Синий трактор")
keyboard = ReplyKeyboardMarkup(keyboard=[[button],[button1],[button2],[button3]])


'''
@dp.message(Command("go"))
async def send_welcome(message: Message):
    await message.answer("Добро пожаловать",reply_markup=keyboard)
'''

@dp.message(lambda message: message.text =="👧Нажми меня")
async def send_greeting(message: Message):
    await message.answer("Кнопка в разработке, нажми следующую) ")

@dp.message(lambda message: message.text =="▶️🧸Мимимишки")
async def mimimishki (message:Message):
    await message.answer("https://rutube.ru/video/34c026410bfd0bf4503187da033098ed/")

@dp.message(lambda message: message.text =="▶️🐕Щенячий Патруль")
async def pawpatrol(message:Message):
    await message.answer("https://rutube.ru/video/d33d3d6d26f9e72048323daa7749b5f8/")


@dp.message(lambda message: message.text =="▶️🚜Синий трактор")
async def Sinij_traktor (message:Message):
    await message.answer("https://rutube.ru/video/05121e89f2541de353b24d1bb4676c2e/")


async def main() -> None:
# Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(TOKEN)

    # And the run events dispatching
    await dp.start_polling(bot)

keep_alive()
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
