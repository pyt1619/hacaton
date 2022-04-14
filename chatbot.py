from telebot import types
import os, telebot, time
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5121446290:AAH9mBewPTtcd8g-B_GWJQ9w7Y2FQnE4YKg')

def getText(url, type, message):
    while True:
        response2 = requests.get(url=f'https://college.edunetwork.ru{url}')
        soup2 = BeautifulSoup(response2.text, 'lxml')
        # Название
        description = ''
        title = ''
        metro = ''
        info = ''
        gpa = ''
        try:
            title = soup2.find('div', attrs={'id':'unit-header'}).find('h1', attrs={'itemprop':'name'}).text
        except:
            pass
        # Метро
        try:
            metro = soup2.find('div', attrs={'id':'unit-header'}).find('li',class_="metro truncate").text
        except:
            pass
        # Общая информация
        try:
            info = soup2.find('section', attrs={'id':'general'}).text.strip()
        except:
            pass
        # Средний балл аттестата(grade point average)
        try:
            gpa = soup2.find('div', class_="row unit-values").text
        except:
            pass
        # Описание
        try:

            for i in range(100):
                try:
                    description += soup2.find('section', attrs={'id':'about'}).findAll('p')[i].text
                    description += '\n'
                except IndexError:
                    break
        except:
            pass
        if(title!=''):
            bot.send_message(message.chat.id,  "Название", reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id,  title, reply_markup=keyboard1)
            if(metro!=''):
                bot.send_message(message.chat.id,  "Метро", reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(message.chat.id,  metro, reply_markup=keyboard1)
            if(description!=''):
                bot.send_message(message.chat.id,  "Общая информация", reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(message.chat.id,  description, reply_markup=keyboard1)
            if(info!=''):
                bot.send_message(message.chat.id,  "Описание", reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(message.chat.id,  info, reply_markup=keyboard1)
            if(gpa!=''):
                bot.send_message(message.chat.id,  "Средний балл", reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(message.chat.id,  gpa, reply_markup=keyboard1)
            bot.send_message(message.chat.id,  "Средний балл", reply_markup=keyboard1)
            
            break

keyboard1 = types.ReplyKeyboardMarkup()
keyboard1.row('Вывести список колледжей')
with open('names.txt', 'r') as f:
    names = f.read().splitlines()
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравсвуйте.\nЯ могу помочь с выбором колледжа для вас', reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if(message.text.lower() == 'вывести список колледжей'):
        mes = ["","","","",""]
        
        for i in range(len(names)):
            mes[0]+=str(i+1)+"."+names[i].split(":::::")[0]+"\n"
            if(i%30 == 0 or i+1 == len(names) and i != 0):
                bot.send_message(message.chat.id,  mes[0], reply_markup=keyboard1)
                mes[0] = ''
        bot.send_message(message.chat.id,  "Напишите номер колледжа чтобы вывести информацию о нем", reply_markup=types.ReplyKeyboardRemove())
    else:
        try:
            num = int(message.text)-1

            getText(names[num].split(":::::")[1], 1, message)

            

        except:
            bot.send_message(message.chat.id,  "Напишите номер колледжа чтобы вывести информацию о нем или запросите список колледжей коммандой:вывести список колледжей", reply_markup=types.ReplyKeyboardRemove())
            return

bot.polling()
