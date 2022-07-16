import telebot
import config as cfg
import text as txt

bot = telebot.TeleBot(cfg.token, parse_mode=None)
print("Бот для рейда запущен")

@bot.message_handler(commands=['start'])
def start (message):
    bot.send_message(message.chat.id, txt.startmsg)
    # Вы можете указать любое стартовое сообщение для все пользователей кроме вас
    if message.chat.id == cfg.admin or cfg.admin2:
        bot.send_message(message.chat.id, "Привет мой владелец добавляй меня в группу и начнем рейд напиши /help чтобы увидить список команд 😉")
        
@bot.message_handler(commands=['help'])
def help (message):
        bot.send_message(message.chat.id, txt.helpmsg)
        if message.chat.id == cfg.admin or cfg.admin2:
            bot.send_message(message.chat.id, "Напиши /raid в группе и я начну рейд сообщениями. Чтобы добавить меня в группу вам нужно быть админом либо попросить админа добавить вашего бота в группу, а так же вы можете добавить команд и другого чтобы бот был более доверчивым и никто не думал что бот для рейда!")
            bot.send_message(message.chat.id, "Все настройки текста находятся в text.py Все настройки бота находяться в config.py")
            bot.reply_to(message, "Удачного вам рейда! 😁")
           
@bot.message_handler(commands=['raid'])
def raid (message):
    for i in range(20000000):
        bot.send_message(message.chat.id, f"{txt.raid1}")
        bot.send_message(message.chat.id, txt.raid2)
        bot.send_message(message.chat.id, txt.lag)
        bot.send_message(message.chat.id, txt.gifka)
        bot.send_message(message.chat.id, txt.gifka)
        bot.send_message(message.chat.id, txt.gifka)
        bot.send_message(message.chat.id, txt.iplog)
        bot.send_message(message.chat.id, txt.alpengold)
        bot.send_message(message.chat.id, txt.agonym)
        bot.send_message(message.chat.id, txt.Feel)
        
        
        
        
        
           

bot.polling(none_stop=True, interval=0)