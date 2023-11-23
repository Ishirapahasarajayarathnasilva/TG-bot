import os
import telebot

bot = telebot.Telebot("API KEY")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hellow Im Ubetata chatbot")
    
@bot.message_handler(commands=["how"])
def send_message(message):
    bot.send_message(message,"Waren Kiyl Denna Pnny!!!!!!!!!!") 
    
 
 bot.polling()      