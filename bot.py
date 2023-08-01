import telebot

bot = telebot.TeleBot("YOUR_BOT_TOKEN")

@bot.message_handler(commands=["start"])
def start(message):
  bot.reply_to(message, "Hi! I'm a bot that replies what you say.")

@bot.message_handler(content_types=["text"])
def reply(message):
  bot.reply_to(message, message.text)

bot.polling()
