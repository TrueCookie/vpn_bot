# подключаем модуль для Телеграма
import telebot

import subprocess

# указываем токен для доступа к боту
bot = telebot.TeleBot('6180127098:AAHn1CEOf4LKlvx3K36lyLJT2vfD2iGAFN0')

# приветственный текст
start_txt = 'Привет! Это журнал «Код». \n\nТеперь у бота появился бэкенд.'


# КОМАНДА: /start
@bot.message_handler(commands=['start'])
def start(message):
    # выводим приветственное сообщение
    bot.send_message(message.from_user.id, start_txt, parse_mode='Markdown')

# КОМАНДА: /file
@bot.message_handler(commands=['file'], content_types=['text'])
def send_file(message):
    bot.send_document(message.chat.id, open(r"Пример файла.txt", 'rb'))

# КОМАНДА: /newclient
@bot.message_handler(commands=['newclient'])
def create_new_client(message):
    try:
        subprocess.run(["sh", "/root/dev/ovpn_serv/new_client.sh"])
        bot.send_message(chat_id=message.from_user.id, text="Новый клиент создан!")
    except:
        bot.send_message(chat_id=message.from_user.id, text="Нового клиента создать не удалось :(")
    # ДОБАВИТЬ: Проверять наличие нового файла .ovpn

# запускаем бота
if __name__ == '__main__':
    print('Бот запущен!')
    try:
        bot.polling(none_stop=True, interval=0)
    # если возникла ошибка — сообщаем про исключение и продолжаем работу
    except Exception as e: 
        print('❌❌❌❌❌ Сработало исключение! ❌❌❌❌❌')