import os
import requests
import pandas as pd
from telebot import TeleBot
import telebot
from telebot import types

bot = telebot.TeleBot('API токен вашего бота')


@bot.message_handler(commands=['start'])
def start_cmd(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Кнопка 1')
    button2 = types.KeyboardButton('Кнопка 2')
    button3 = types.KeyboardButton('Кнопка 3')
    markup.add(button1, button2, button3)

    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)

BOT_TOKEN = os.environ.get('5919221259:AAGSAveZ-DAdNSL0jtwqOlVnG445hCQvia8')
bot = TeleBot('5919221259:AAGSAveZ-DAdNSL0jtwqOlVnG445hCQvia8')

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Привет, чем могу помочь?\n Вот возможные команды: /start, /расходы, /советыэкономии, /советыпоинвестициям, /инвестиции [зарплата], /найтиработу, /акции")

@bot.message_handler(commands=['советыэкономии'])
def send_advise(message):
    bot.reply_to(message, "Конечно! Вот несколько советов, как экономить деньги:\n1. Определите свои приоритеты и составьте бюджет на месяц. Планируя свои расходы, вы сможете контролировать свои финансы и избежать неожиданных трат.\n 3. Используйте купоны и специальные предложения. Это может быть купон на скидку или акционное предложение в магазине. Это поможет сэкономить деньги, особенно если вы покупаете продукты.\n 4. Разработайте план для своих крупных трат, таких как покупка автомобиля или дома. Следите за ценами и смотрите, где можно сэкономить деньги \n 5. Изучайте и сравнивайте цены в разных магазинах. В некоторых магазинах продукты могут быть дешевле, чем в других.\n 6. Избегайте совершения необдуманных покупок. Перед тем как что-то купить, подумайте, действительно ли вам это необходимо.\n 7. Используйте альтернативные методы передвижения, такие как велосипед или общественный транспорт. Это не только позволит сэкономить, но и будет полезно для здоровья.\n 8. Имейте терпение. Сэкономление денег может быть долгим процессом, но с терпением и настойчивостью вы достигнете своих целей.")


@bot.message_handler(commands=['советыпоинвестициям'])
def send_advise3(message):
    bot.reply_to(message,"Некоторые общие советы по инвестированию:\n 1. Разнообразьте свой портфель. Не вкладывайте все деньги в одну компанию или отрасль. \n 2. Не берите на себя больше риска, чем можете позволить себе. Инвестирование всегда связано с риском, но возьмите риск, который соответствует вашим целям и возможностям.\n 3. Не паникуйте при падении рынка. Рынок акций колеблется, но в долгосрочной перспективе рост тенденции будет положительным \n 4. Ищите альтернативные варианты для инвестирования, например, недвижимость, ценные бумаги, золото, криптовалюты и т.д \n 5. Сделайте свой собственный анализ и изучите рынок, чтобы принимать взвешенные решения. При этом используйте только надежные источники информации")

@bot.message_handler(commands=['расходы'])
def start_message(message):
    global expenses
    expenses = 0.
    bot.send_message(message.chat.id, "Давай посчитаем твои расходы в месяц. Чтобы добавить расходы, отправь мне сообщение в виде 'расход [сумма]'. Чтобы узнать текущую сумму расходов, отправь мне 'сумма'.")

# обрабатываем сообщения с расходами
@bot.message_handler(func=lambda message: message.text.lower().startswith("расход"))
def add_expenses(message):
    global expenses
    try:
        value = int(message.text.lower().split()[1])
        expenses += value
        bot.send_message(message.chat.id, f"Расходы успешно добавлены. Текущая сумма расходов: {expenses}.")
    except:
        bot.send_message(message.chat.id, "Ошибка. Введите корректную сумму расходов.")

# обрабатываем запрос на текущую сумму расходов
@bot.message_handler(func=lambda message: message.text.lower() == "сумма")
def show_expenses(message):
    global expenses
    bot.send_message(message.chat.id, f"Текущая сумма расходов: {expenses}.")


# Функция, которая будет вызываться в ответ на команду /invest <зарплата>
@bot.message_handler(commands=['инвестиции'])
def invest(message):
    salary = message.text.split()[1]
    try:
        salary = float(salary)
    except ValueError:
        bot.reply_to(message, "Некорректно задана зарплата")
        return

    invest = salary * 0.2

    # Отправляем ответ пользователю
    bot.reply_to(message, f"По данной зарплате инвестируйте {invest} рублей в месяц")

@bot.message_handler(commands=['найтиработу']) #обрабатываем команду /link
def send_link(message):
    bot.send_message(message.chat.id, "Варианты сайтов для поиска работы в интернете: https://kazan.hh.ru/ , https://www.avito.ru/kazan/rabota")

@bot.message_handler(commands=['акции'])
def send_message(message):
    bot.reply_to(message, "Вот варианты, во что можно вложится:\n 1.сбербанк 241.74 руб 1 акция\n 2. Роснефть 483.40 руб 1 акция")


bot.infinity_polling()