
from translate import translate
import telebot

TOKEN = "5172806845:AAF_ZdhMcpCTlu2eIOE7-n2-FR4N8ihrv7w"
tarjimonbot = telebot.TeleBot(token=TOKEN)

@tarjimonbot.message_handler(commands=['start'])
def salom(message):
    xabar = "Assalomu alaykum"
     xabar = '\n Matningizni yuboring'
     tarjimonbot.reply_to(message, xabar)
tarjimonbot.pooling()