import telebot
from telebot import types

bot = telebot.TeleBot("5105427800:AAFl8_ZZrwu2lDw5TZkXTL2v93SQAkTrE44")

language = ["Html", "Css", "JavaScript", "Python", "Java", "React.js"]
counts = [34, 21, 10, 64, 41, 20]
questions = [
    ["Ваш язык применяется в области Веб-разработке?", 10],
    ["Ваш язык Html или Css?", 11],
    ["Ваш язык Html?", 13],
    ["Ваш язык применяется в области Бэкенд-разработки?", 20],
    ["Ваш язык Python или Java?", 21],
    ["Ваш язык Python?", 23],
]

count = 0
true_language = "Django"