import datetime
import menu
import parser_cyt
import parser_hum
import parser_toast
import settings
import telebot
import time


bot = telebot.TeleBot(settings.API, parse_mode="html")


@bot.message_handler(commands=["bot"])
def start_menu(message):

    menu.show_button(message)


@bot.message_handler(content_types=['text'])
def proc_buttons(message):

    if message.text == "Что по ЧСЧ?✅":
        options = ["Да", "Нет, я хуесос"]
        cur_wd = datetime.datetime.weekday(datetime.datetime.now())
        dif = 3 - cur_wd
        if dif == 1:
            bot.reply_to(message, f"До ЧСЧ остался <b>{dif}</b> день")
        if 1 < dif < 5:
            bot.reply_to(message, f"До ЧСЧ осталось <b>{dif}</b> дня")
        if dif > 5:
            bot.reply_to(message, f"До ЧСЧ осталось <b>{dif}</b> дней")
        elif dif < 0:
            bot.reply_to(message, f"До ЧСЧ осталось <b>{7 + dif}</b> дней")
        elif dif == 0:
            bot.reply_to(message, (f"ЧСЧ по плану <b>сегодня</b>!!! Не забудь " +
                                   "и напомни братанам, подняв этот вопрос"))
            bot.send_poll(message.chat.id, ("Поднимается вопрос относительно " +
                                            "сегодняшнего события. Организуем ли мы ЧСЧ сегодня?"),
                          options,
                          is_anonymous=False)

    if message.text == "Попросить заказать пивас🍻":

        menu.beer_menu(message)

    if message.text == "Другие активности🎉":

        menu.other(message)

    if message.text == "На главную👑":

        menu.show_button(message)

    if message.text == "Нефиль👨🏽‍🦱":
        bot.reply_to(message, f"Товарищ <b>{message.from_user.first_name}</b> "
                              "задерживается, очень извиняется. Оформите нефильтрованное пиво, по человечески")

    if message.text == "Тёмное👨🏿‍🦱":
        bot.reply_to(message, f"Товарищ <b>{message.from_user.first_name}</b> "
                              "задерживается, очень извиняется. Оформите тёмное пиво, по человечески")

    if message.text == "Светлое👨🏼‍🦱":
        bot.reply_to(message, f"Товарищ <b>{message.from_user.first_name}</b>"
                              " задерживается, очень извиняется. Оформите светлое пиво, по человечески")

    if message.text == "Сидр🧔🏻":
        bot.reply_to(message, f"Товарищ <b>{message.from_user.first_name}</b>"
                              " задерживается, очень извиняется. Оформите сидр, по человечески")

    if message.text == "Мб сегодня по пивку?🍻":
        options = ["Да", "Нет, я хуесос"]
        bot.send_poll(message.chat.id, f"Поднимается вопрос относительно "
                                       f"сегодняшнего вечера. Господин с именем {message.from_user.first_name} "
                                       f"{message.from_user.last_name} предлагает организовать ЧСЧ сегодня. "
                                       f"Можно не чисто симсолически. Ваше мнение?", options, is_anonymous=False)

    if message.text == "Ебануть анекдот, порадовать пацанов😆":
        bot.reply_to(message, f"Внимание, анекдот от господина с именем "
                              f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>:")
        time.sleep(3)
        bot.reply_to(message, parser_hum.hum_pars())

    if message.text == "Поразить своей мудростью🐺":
        bot.reply_to(message, f"Изрядно покумекав, господин <b>{message.from_user.first_name} "
                              f"{message.from_user.last_name}</b> решил резко поделиться с нами своей мудростью:")
        time.sleep(3)
        bot.reply_to(message, f"{parser_cyt.cyt_pars()}")

    if message.text == "Бахнем?!🍻":
        bot.reply_to(message, "ЗА... ЕБИСЬ!!!")
        time.sleep(3)
        bot.reply_to(message, parser_toast.toast_pars())


bot.infinity_polling()
