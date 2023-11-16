# подключаем модуль для Телеграма
import telebot
from telebot import types

import uuid
import subprocess

from core import queries

# указываем токен для доступа к боту
bot = telebot.TeleBot('6180127098:AAHn1CEOf4LKlvx3K36lyLJT2vfD2iGAFN0')

# приветственный текст
start_txt = 'Привет! Это журнал «Код». \n\nТеперь у бота появился бэкенд.'

# ВЫЗОВ СКРИПТОВ BASH:
def reg_client(client_id):
    # 1.регистрируем клиента
    try:
        subprocess.run(["sh", "/root/dev/ovpn_serv/reg_client.sh", client_id])
    except Exception as e:
        print('Не удалось выполнить bash-скрипт:', e)
        raise

def new_client(client_id):
    # 2.создаём файл конфигурации клиента
    try:
        subprocess.run(["sh", "/root/dev/ovpn_serv/new_client.sh", client_id])
    except Exception as e:
        print('Не удалось выполнить bash-скрипт:', e)
        raise

def revoke_client(client_id):
    try:
        subprocess.run(["sh", "/root/dev/ovpn_serv/revoke.sh", client_id])
    except Exception as e:
        print('Не удалось выполнить bash-скрипт:', e)
        raise

def renew_client(client_id):
    try:
        subprocess.run(["sh", "/root/dev/ovpn_serv/renew.sh", client_id])
    except Exception as e:
        print('Не удалось выполнить bash-скрипт:', e)
        raise

# ВНУТРЕННИЕ МЕТОДЫ БОТА:
# Отправить сертификат клиента
def send_cert(bot, message, client_id):
    try:
        # 3.высылаем файл
        bot.send_message(chat_id=message.from_user.id, 
                        text="""Новый сертификат создан!\nОсталось только добавить его в приложение""")
        bot.send_document(message.chat.id, open(rf"/root/{client_id}.ovpn", 'rb'))
    except Exception as e:
        bot.send_message(chat_id=message.from_user.id, text=f"Нового клиента создать не удалось :(.\n{e}")


# ОБРАБОТКА КОМАНД:
# КОМАНДА: /start
@bot.message_handler(commands=['start'])
def start(message):
    # выводим приветственное сообщение
    bot.send_message(message.from_user.id, start_txt, parse_mode='Markdown')

# КОМАНДА: /register
@bot.message_handler(commands=['register'])
def new_user(message):
    try:
        # TODO: Заменить на читаемое имя (client_N)
        # 0.генерируем id клиента
        client_id = str(uuid.uuid4())

        reg_client(client_id)
        queries.add_client(client_id)

        new_client(client_id)
        send_cert(bot, message, client_id)
        print(f"INFO: Нового клиент создан: {client_id}")
    except Exception as e:
        bot.send_message(chat_id=message.from_user.id, text=f"Нового клиента создать не удалось :(.\n{e}")
        print(f"FATAL: Нового клиента создать не удалось :(.\n{e}")

# БЛОКИРОВКА ПОЛЬЗОВАТЕЛЯ:

# ВОЗОБНОВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ:

# запускаем бота
if __name__ == '__main__':
    print('Бот запущен!')
    try:
        bot.polling(none_stop=True, interval=0)
    # если возникла ошибка — сообщаем про исключение и продолжаем работу
    except Exception as e: 
        print(f'❌❌❌❌❌ Сработало исключение! ❌❌❌❌❌.\n{e}')