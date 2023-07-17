"""Сервер бота"""
import logging
import os
#import aiohttp
from aiogram import Bot, Dispatcher, executor, types




logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
# PROXY_URL = os.getenv("TELEGRAM_PROXY_URL")
# PROXY_AUTH = aiohttp.BasicAuth(
#     login=os.getenv("TELEGRAM_PROXY_LOGIN"),
#     password=os.getenv("TELEGRAM_PROXY_PASSWORD")
# )
ACCESS_ID = os.getenv("TELEGRAM_ACCESS_ID")

bot = Bot(token=API_TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(ACCESS_ID))

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Приветственное сообщение + помощь"""
    await message.reply(
        "Бот для учета финансов\n\n" 
        "Добавить расход: 250 такси\n"
        "Сегодняшняя статистика: /today\n"
        "За текущий месяц: /month\n"
        "Последние внесённые расходы: /expenses\n"
        "Категории трат: /categories"
    )





@dp.message_handler()
"""Добавляется расход"""
async def add_expense(message: types.Message):
    """Добавляет новый расход"""
    try:
        expense = expenses.add_expense(message.text)
    except exceptions.NotCorrectMessage as e:
        await message.answer(str(e))
        return
    answer_message = (
        f"Добавлены траты {expense.amount} руб на {expense.category_name}.\n\n"
        f"{expenses.get_today_statistics()}")
    await message.answer(answer_message)


# #Не пошло через телебота, попробую через айограм
# import telebot
#
# bot = telebot.TeleBot("5598305102:AAF68rW_fWOKLIPnrJhyQEzg8Zxokdmri4k")
# @bot.message_handler(commands= ['start', 'help'])
# def start(message):
#     bot.send_message(message.chat.id, 'Приветствую тебя, путник, в обработке твоих зелёных деньжат. Будь добр, следи инструкциям:'
#                     'Пример добавления расхода: 100 магазин'
#                      "Траты сегодня: ")
#
# @bot.message_handler()
# def user_text(message):
#     bot.send_message(message.chat.id)