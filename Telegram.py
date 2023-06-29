import telebot

BOT_TOKEN = "6054603071:AAEPRgYHvU1Rg8a--eWFZAtZKul1ZybGNpU"
bot = telebot.TeleBot (BOT_TOKEN)

@bot.message_handler (commands= ['start'])
def start (message):
    bot.send_message (message.chat.id, "Hello, welcome to Calculator bot")

@bot.message_handler (commands= ['help'])
def help (message):
    bot.reply_to (message,"I support following commands: \n /start \n /help")

@bot.message_handler (func=lambda message: True)
def calculator (message):
    Result = eval (message.text)
    bot.reply_to (message,f"the result is {Result}")



print ("running")
bot.infinity_polling ()
