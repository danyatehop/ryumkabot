import settings
import telebot
from telebot import types

bot = telebot.TeleBot(settings.API, parse_mode="html")


def show_button(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    butt_stat = types.KeyboardButton('Что по ЧСЧ?✅')
    butt_meet = types.KeyboardButton('Мб сегодня по пивку?🍻')
    butt_bear = types.KeyboardButton('Попросить заказать пивас🍻')
    butt_other = types.KeyboardButton('Другие активности🎉')

    markup.row(butt_stat)
    markup.row(butt_meet)
    markup.row(butt_bear)
    markup.row(butt_other)
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)


def beer_menu(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    butt_unfil = types.KeyboardButton('Нефиль👨🏽‍🦱')
    butt_dark = types.KeyboardButton('Тёмное👨🏿‍🦱')
    butt_light = types.KeyboardButton('Светлое👨🏼‍🦱')
    butt_cider = types.KeyboardButton('Сидр🧔🏻')
    butt_main = types.KeyboardButton('На главную👑')

    markup.row(butt_unfil, butt_dark)
    markup.row(butt_light, butt_cider)
    markup.row(butt_main)

    bot.send_message(message.chat.id, "Чем порадуетесь?", reply_markup=markup)


def other(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    butt_cytata = types.KeyboardButton('Поразить своей мудростью🐺')
    butt_humor = types.KeyboardButton('Ебануть анекдот, порадовать пацанов😆')
    # butt_sponk = types.KeyboardButton('Отшлёпать бота по заднице ✋🍑')
    butt_toast = types.KeyboardButton('Бахнем?!🍻')
    butt_main = types.KeyboardButton('На главную👑')

    markup.row(butt_humor)
    markup.row(butt_toast, butt_cytata)
    markup.row(butt_main)

    bot.send_message(message.chat.id, "Выберите актвность...", reply_markup=markup)
