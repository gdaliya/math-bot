import telebot
import random
symbol=['+','*','-']
num1=None
num2=None
symb=None
result=None
bot=telebot.TeleBot('7444367736:AAFjYZU0hAWwCc0cNwV2ceRiecN4aUmXzCw')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'hello type /start_game to start game /help for help')
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'/start game to start_game /stop to stop')
@bot.message_handler(commands=['start_game'])
def start_game(message):
    bot.send_message(message.chat.id,'type next for next question')
@bot.message_handler(content_types=['text'])
def answer(message):
    global num1
    global num2
    global symb
    global result
    if message.text == 'next':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        symb = random.choice(symbol)
        bot.send_message(message.chat.id, str(num1) + symb + str(num2))
    if message.text.isdigit():
        if symb=='+':
            result=int(num1) + int(num2)
        if symb=='*':
            result=int(num1) * int(num2)
        if symb=='-':
            result=int(num1)-int(num2)
        if result==int(message.text):
            bot.send_message(message.chat.id,'good job')
        else:
            bot.send_message(message.chat.id,f'wrong,try again')
@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id,'bye')
bot.infinity_polling()
