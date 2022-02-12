import time
import telebot
from telebot import types

import main

@main.bot.message_handler(commands=["start"])
def welcome(message):
    sticker = open("sticker.webp", "rb")
    main.bot.send_sticker(message.chat.id, sticker)

    welcome_str = "Здравствуй дружище {0.first_name}, Я <code>Akinator</code>, я буду отгадывать какой твой любимый язык программирование!".format(message.from_user, main.bot.get_me())

     
    simple_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    language_key = types.KeyboardButton("Загадать Язык Программирование")
    simple_keyboard.add(language_key)
    main.bot.send_message(message.chat.id, welcome_str, parse_mode="html", reply_markup = simple_keyboard)


@main.bot.message_handler(commands=["language"])
def answer(message):
     calculate_language(main.count)
     main.count = 0
     main.bot.send_message(message.chat.id, main.true_language, reply_markup=None)

@main.bot.message_handler(content_types=['text'])
def start (message):
    global number_of_questions
    if message.chat.type == "private":
        if message.text == "Загадать Язык Программирование":
            game_txt = "На данный момент я могу отгадывать один из этих языков - {}, если твой любимый язык программирование здесь, то нажми `Let's go!`".format(main.language)
            go_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            go_key = types.KeyboardButton("Lets go!")
            go_keyboard.add(go_key)
            main.bot.send_message(message.chat.id, game_txt, parse_mode="html", reply_markup = go_keyboard)

        if message.text == "Lets go!":


            for number_of_questions in range(len(main.questions)):
                yesno_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                yes_key = types.KeyboardButton("Yes")
                no_key = types.KeyboardButton("No")
                yesno_keyboard.add(yes_key, no_key)

                msg = main.bot.send_message(message.chat.id, main.questions[number_of_questions][0],
                 reply_markup=yesno_keyboard)

                main.bot.register_next_step_handler(msg, input_answer)
                time.sleep(4)

def input_answer(message):
    if message.text == "stop":
         main.bot.stop_polling() 
    if message.text == "Да":
        main.count += main.questions[number_of_questions][1]


def calculate_language(count):
    found = main.counts[0]
    for item in main.counts:
        if abs(item - count) < abs(found - count):
            found = item
    for i in range(len(main.counts)):
        if found == main.counts[i]:
            main.true_language = main.language[i]

     
main.bot.polling(none_stop=True)
