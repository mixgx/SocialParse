import telebot
import sys
import os
import subprocess
from config import *

bot = telebot.TeleBot(botkey)
password = 'test'
global acsess
global admin
global startc
global dst
dst = False
acsess = False
admin = 'None'
startc = False

@bot.message_handler(commands=['admin'])
def login(message):
    global acsess
    global admin
    if message.text.lower() == ('/admin '+password):
        admin = message.from_user.first_name
        acsess = True
        bot.send_message(message.from_user.id, 'Hello My Owner!')

@bot.message_handler(commands=['stop'])
def stop(message):
    global acsess
    if acsess:
        bot.stop_bot()
    if not acsess:
        bot.send_message(message.from_user.id, 'No permission👺')

@bot.message_handler(commands=['startc'])
def start_command(message):
    global acsess
    global startc
    if acsess:
        startc = True
        bot.send_message(message.from_user.id, 'Console launched! You can send commands')
        bot.send_message(message.from_user.id, 'IF YOU WANT TO USE CMD COMMAND, USE [cmd /c (command)]')

@bot.message_handler(commands=['stopc'])
def stop_command(message):
    global acsess
    global startc
    if acsess:
        startc = False
        bot.send_message(message.from_user.id, 'Console Stoped!')

@bot.message_handler(commands=['downloadstart'])
def downloadsta(message):
    global acsess
    if acsess:
        bot.send_message(message.from_user.id, 'DOWNLOADER STARTED')
        global dst
        dst = True

@bot.message_handler(commands=['downloadstop'])
def downloadsto(message):
    global acsess
    if acsess:
        bot.send_message(message.from_user.id, 'DOWNLOADER STOPED')
        global dst
        dst = False

@bot.message_handler(commands=['help'])
def help(message):
    global acsess
    if acsess:
        bot.send_message(message.from_user.id, 'stop - stop script\nstartc/stopc - start/stop console\nhelp - this message\nadmin - login\nprintsc - screenshot\n~ - change dir(please use \ but not /. and dont use 4)')

@bot.message_handler(content_types=['text'])
def console(message):
    global acsess
    if acsess:
        global startc
        cd = False
        if startc:
            output = '0'
            if cd:
                os.chdir(message.text.lower())
                bot.send_message(message.from_user.id, 'DIRECTORY = '+os.getcwd())
            if message.text.lower() == 'dir':
                output = subprocess.check_output('cmd /c dir')
            if message.text.lower() == 'cd':
                cd = True
                bot.send_message(message.from_user.id, 'PATH:')
            else:
                if not message.text.lower() == 'dir':
                    if not message.text.lower() == 'cd':
                        if not cd:
                            output = subprocess.check_output(message.text.lower())
            
            bot.send_message(message.from_user.id, output)


@bot.message_handler(content_types=['text'])
def downloader(message):
    global acsess
    if acsess:
        global dst
        if dst:
            bot.send_document(message.from_user.id, open(message.text.lower(), 'rb'))

bot.polling(none_stop=True)