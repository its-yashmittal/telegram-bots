bot_token ="1750591707:AAG6fYZzz0lEyuybZOUn47Og67Z84bkDxNw"
from telegram.ext import MessageHandler, CommandHandler, Filters, Updater, updater
from datetime import date
from google_trans_new import google_translator 
from translate import translatorFn 
from speechToText import audio_processor
from textToSpeech import textToSpeech
bot_cmd_list = []
translator = google_translator()
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello I am Yash's IMDB Movie Bot!\
        \njust type in the name of the movie you want to search and i'll send you all the information I could grab from the imdb website!!!")

def eng(update, context):
    bot_cmd_list.append("en")

def hin(update, context):
    bot_cmd_list.append("hi")

def chn(update, context):
    bot_cmd_list.append("cn")


def message(update, context):
    print(update)
    transcription = update.message.text
    print("calling scraper with " + transcription)
    if bot_cmd_list[-1]=="en":
        translate_text = translator.translate(transcription,lang_tgt='en')  
    elif bot_cmd_list[-1]=="hi":
        translate_text = translator.translate(transcription, lang_tgt='hi')
    elif bot_cmd_list[-1]=="cn":
        translate_text = translator.translate(transcription, lang_tgt='zh-cn')
    print(translate_text)

    context.bot.send_message(chat_id=update.effective_chat.id, text = translate_text)
    
def error_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ooops!!Looks like my translator broke😥!")
# def audio_msg(update, context):
#     print("Hey, please wait I am transcripting your audio!")
#     audio_file = context.bot.getFile(update.message.voice.file_id)
#     audio_file.download('voice.ogg')
#     transcription = audio_processor()
#     print("calling scraper with " + transcription)
#     context.bot.send_message(chat_id=update.effective_chat.id, text="You just said "+transcription+" in the voice note!")
#     info = scraper(transcription)
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Your movie details are: \n")
#     for field in info:
#         if field=='genres':
#             category = "Genres:"
#             for i in range(0, len(info[field])):
#                 category = category + "\n" + str(info[field][i])
#             context.bot.send_message(chat_id=update.effective_chat.id, text=category)    
#         elif field=='cast':
#             stars = "Cast:"
#             length = len(info[field])-3
#             for i in range (0, length):
#                 if info[field][i]=='':
#                     stars = stars + '\n'
#                 elif info[field][i+3]=='':
#                     stars = stars + info[field][i] + " as " + info[field][i+1] +"/" + info[field][i+2] + "\n"
#                     i = i - 2
#                     continue
#                 elif info[field][i+2]=='':
#                     stars = stars + info[field][i] + " as " + info[field][i+1] +"\n"
#                     i = i-1
#                     continue
#             context.bot.send_message(chat_id=update.effective_chat.id, text = stars)
#         else:
#             context.bot.send_message(chat_id=update.effective_chat.id, text=field+": "+str(info[field]))
#     context.bot.send_message(chat_id=update.effective_chat.id, text="There you go!👍 Thanks for using me🤗 If you want to search for another movie just type in the name and i'll get those details right back to you")


def not_defined(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, this is not a supported command!\
        \nThe list of available commands is:\
        \n1./start to start the bot\
        \n2./en for translation into English\
        \n3./hi for translation into Hindi")


def run_bot():
    updater = Updater(bot_token)
    dispatcher = updater.dispatcher
    start_cmd_handler = CommandHandler('start', start)
    en_cmd_handler = CommandHandler('en', eng)
    hn_cmd_handler = CommandHandler('hi', hin)
    cn_cmd_handler = CommandHandler('cn', chn);
    #date_handler = CommandHandler('date', current_date)
    #translation_handler = CommandHandler('movie', movie)
    #audio_handler = MessageHandler(Filters.voice, audio_msg)
    message_handler = MessageHandler(Filters.text, message)
    unknown_handler = MessageHandler(Filters.command, not_defined)
    
    #adding handlers in the dispatcher
    dispatcher.add_handler(start_cmd_handler)
    dispatcher.add_handler(en_cmd_handler)
    dispatcher.add_handler(hn_cmd_handler)
    dispatcher.add_handler(cn_cmd_handler)
    #dispatcher.add_handler(translation_handler)
    #dispatcher.add_handler(date_handler)
    dispatcher.add_handler(unknown_handler)
    dispatcher.add_handler(message_handler)
    #dispatcher.add_handler(audio_handler)
    dispatcher.add_error_handler(error_handler)
    #this command is used to start the bot
    updater.start_polling()
    #this is used to keep the bot idle
    updater.idle()

run_bot()