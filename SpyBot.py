import telebot

token = '988970189:AAFYGi7uA_Q7SVjOSmmCzL2YnM2RcwBb-F4'

telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot(token=token)

@bot.message_handler(content_types=['text'])

def spy(message):

    print('spy.txt')
    f = open('spy.txt', 'a')
    f.write(message.text + ' ')
    f.close()

bot.polling(none_stop=True)