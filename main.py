import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from telebot import TeleBot
import telebot
from telebot import types

BOT_TOKEN = os.environ.get('5919221259:AAGSAveZ-DAdNSL0jtwqOlVnG445hCQvia8')
bot = TeleBot('5919221259:AAGSAveZ-DAdNSL0jtwqOlVnG445hCQvia8')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, чем могу помочь?\n Вот возможные команды: \n /start - старт,\n /expenses - посчитает все Ваши расходы,\n /economyadvice - даст советы экономии,\n /investmenttips - даст советы по инвестициям,\n /findajob - поможет найти работу,\n /инвестиции [зарплата] - расчитает сумму инвестиции от заработной платы,\n /stocks - акции, которые вы можете приобрести \n /text - расчитает Ваш баланс на данный момент")



@bot.message_handler(commands=['economyadvice'])
def send_advise(message):
    bot.reply_to(message, "Конечно! Вот несколько советов, как экономить деньги:\n1. Определите свои приоритеты и составьте бюджет на месяц. Планируя свои расходы, вы сможете контролировать свои финансы и избежать неожиданных трат.\n 3. Используйте купоны и специальные предложения. Это может быть купон на скидку или акционное предложение в магазине. Это поможет сэкономить деньги, особенно если вы покупаете продукты.\n 4. Разработайте план для своих крупных трат, таких как покупка автомобиля или дома. Следите за ценами и смотрите, где можно сэкономить деньги \n 5. Изучайте и сравнивайте цены в разных магазинах. В некоторых магазинах продукты могут быть дешевле, чем в других.\n 6. Избегайте совершения необдуманных покупок. Перед тем как что-то купить, подумайте, действительно ли вам это необходимо.\n 7. Используйте альтернативные методы передвижения, такие как велосипед или общественный транспорт. Это не только позволит сэкономить, но и будет полезно для здоровья.\n 8. Имейте терпение. Сэкономление денег может быть долгим процессом, но с терпением и настойчивостью вы достигнете своих целей.")

@bot.message_handler(commands=['investmenttips'])
def send_advise(message):
    bot.reply_to(message, "Некоторые общие советы по инвестированию:\n 1. Разнообразьте свой портфель. Не вкладывайте все деньги в одну компанию или отрасль. \n 2. Не берите на себя больше риска, чем можете позволить себе. Инвестирование всегда связано с риском, но возьмите риск, который соответствует вашим целям и возможностям.\n 3. Не паникуйте при падении рынка. Рынок акций колеблется, но в долгосрочной перспективе рост тенденции будет положительным \n 4. Ищите альтернативные варианты для инвестирования, например, недвижимость, ценные бумаги, золото, криптовалюты и т.д \n 5. Сделайте свой собственный анализ и изучите рынок, чтобы принимать взвешенные решения. При этом используйте только надежные источники информации \n Для тех, кто хочет узнать больше:                                                                  Список лучших книг по финансовой грамотности                                   \n Роберт Кийосаки «Богатый папа, бедный папа», «Квадрант денежного потока» \nНаполеон Хилл «Думай и богатей» \n Брайан Трейси «Наука денег»\n Джордж Клейсон «Самый богатый человек в Вавилоне» \n Бодо Шефер «Мани, или Азбука денег»\n Бодо Шефер «Путь к финансовой свободе» Юлия Сахаровская «Куда уходят деньги»")

@bot.message_handler(commands=['expenses'])
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

@bot.message_handler(commands=['findajob'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Сайт hh.ru", url='https://kazan.hh.ru/')
    markup.add(button1)
    button2 = types.InlineKeyboardButton("Сайт Авито", url='https://www.avito.ru/kazan/rabota')
    markup.add(button2)
    bot.send_message(message.chat.id, "{0.first_name}, Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['stocks'])
def send_we(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Акции разных компаний", url='https://bcs-express.ru/recommendations/126')
    markup.add(button)
    bot.send_message(message.chat.id, "{0.first_name}, Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        # Получение дохода из сообщения пользователя
        income = float(message.text)
        # Отправка пользователю сообщения для ввода расходов
        msg = bot.send_message(message.chat.id, "Напишите сумму ваших расходов")
        bot.register_next_step_handler(msg, subtract_expenses, income)
    except ValueError:
        bot.reply_to(message, "Напишите сумму ваших доходов")
# Функция для вычитания расходов из доходов
def subtract_expenses(message, income):
    try:
        # Получение расхода из сообщения пользователя
        expenses = float(message.text)
        # Вычисление баланса
        balance = income - expenses
        # Отправка пользователю сообщения с балансом
        bot.reply_to(message, f"Ваш текущий баланс: {balance:.2f}")
    except ValueError:
        bot.reply_to(message, "Извините, я не понимаю. Пожалуйста, отправьте число.")


bot.infinity_polling()