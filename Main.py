import telebot

bot = telebot.TeleBot("8155559996:AAHExlHUhHQa5wh_SpAiEu1vri4FZ0FiA3I")

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "✅")

if __name__ == "__main__":
    bot.polling(none_stop=True)
