import telebot
import random
symbol=['+','*','-']
num1=None
num2=None
symb=None
result=None
tries=3
bot=telebot.TeleBot('7444367736:AAFjYZU0hAWwCc0cNwV2ceRiecN4aUmXzCw')
def new_numbers(message):
    global num1,num2,symb,result
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    symb = random.choice(symbol)
    if symb == '+':
        result = int(num1) + int(num2)
    if symb == '*':
        result = int(num1) * int(num2)
    if symb == '-':
        result = int(num1) - int(num2)
    bot.send_message(message.chat.id, str(num1) + symb + str(num2))
    return result
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'hello type /start_game to start game /help for help')
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'/start game to start_game /stop to stop')
@bot.message_handler(commands=['start_game'])
def start_game(message):
    global tries
    bot.send_message(message.chat.id,'type next for next question u have 3 tries')
    tries=3
@bot.message_handler(content_types=['text'])
def answer(message):
    global num1
    global num2
    global symb
    global result
    global tries
    if message.text == 'next':
        result=new_numbers(message)
    if tries>0:
        if message.text.isdigit():
            print(result)
            print(message.text)
            if result==int(message.text):
                bot.send_message(message.chat.id,'good job')
                result = new_numbers(message)
            else:
                bot.send_message(message.chat.id,'wrong,try again')
                tries-=1
    if tries<=0:
        bot.send_message(message.chat.id,'u lost good luck next time')
@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id,'bye')
bot.infinity_polling()
