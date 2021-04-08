#Lets build our first our real development project, its going to be an echo bot!
bot_token ="bot_token"
from telegram.ext import MessageHandler, CommandHandler, Filters, Updater, updater
from datetime import date
from speechtext2 import audio_processor
from imdb_scraper import scraper
movie_cmd_list = []
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello I am Yash's IMDB Movie Bot!\
        \njust type in the name of the movie you want to search and i'll send you all the information I could grab from the imdb website!!!")

#def current_date(update, context):
   # context.bot.send_message(chat_id=update.effective_chat.id, text=str(date.today()))

def message(update, context):
    print(update)
    transcription = update.message.text
    print("calling scraper with " + transcription)
    info = scraper(transcription)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Your movie details are: \n")
    for field in info:
        if field=='genres':
            category = "Genres:"
            for i in range(0, len(info[field])):
                category = category + "\n" + str(info[field][i])
            context.bot.send_message(chat_id=update.effective_chat.id, text=category)    
        elif field=='cast':
            stars = "Cast:"
            length = len(info[field])-3
            for i in range (0, length):
                if info[field][i]=='':
                    stars = stars + '\n'
                elif info[field][i+3]=='':
                    stars = stars + info[field][i] + " as " + info[field][i+1] +"/" + info[field][i+2] + "\n"
                    i = i - 2
                    continue
                elif info[field][i+2]=='':
                    stars = stars + info[field][i] + " as " + info[field][i+1] +"\n"
                    i = i-1
                    continue
                    
            context.bot.send_message(chat_id=update.effective_chat.id, text = stars)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=field+": "+str(info[field]))
    context.bot.send_message(chat_id=update.effective_chat.id, text="There you go!👍 Thanks for using me🤗 If you want to search for another movie just type in the name and i'll get those details right back to you")
def error_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ooops!!Looks like my scraper threw an error😥! Double checked the name you typed in, and enter again, no results pop up again then the movie name probably doesn't exist on the IMDB website!🤦")
def audio_msg(update, context):
    print("Hey, please wait I am transcripting your audio!")
    audio_file = context.bot.getFile(update.message.voice.file_id)
    audio_file.download('voice.ogg')
    transcription = audio_processor()
    print("calling scraper with " + transcription)
    context.bot.send_message(chat_id=update.effective_chat.id, text="You just said "+transcription+" in the voice note!")
    info = scraper(transcription)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Your movie details are: \n")
    for field in info:
        if field=='genres':
            category = "Genres:"
            for i in range(0, len(info[field])):
                category = category + "\n" + str(info[field][i])
            context.bot.send_message(chat_id=update.effective_chat.id, text=category)    
        elif field=='cast':
            stars = "Cast:"
            length = len(info[field])-3
            for i in range (0, length):
                if info[field][i]=='':
                    stars = stars + '\n'
                elif info[field][i+3]=='':
                    stars = stars + info[field][i] + " as " + info[field][i+1] +"/" + info[field][i+2] + "\n"
                    i = i - 2
                    continue
                elif info[field][i+2]=='':
                    stars = stars + info[field][i] + " as " + info[field][i+1] +"\n"
                    i = i-1
                    continue
            context.bot.send_message(chat_id=update.effective_chat.id, text = stars)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=field+": "+str(info[field]))
    context.bot.send_message(chat_id=update.effective_chat.id, text="There you go!👍 Thanks for using me🤗 If you want to search for another movie just type in the name and i'll get those details right back to you")

# def movie(update, context):
#     movie_cmd_list.append('movie')
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Hey there, type in or speak the name of the movie you want me to search")

def not_defined(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, this is not a supported command!\
        \nThe list of available commands is:\
        \n1./start to start the bot")


def run_bot():
    updater = Updater(bot_token)
    dispatcher = updater.dispatcher
    start_cmd_handler = CommandHandler('start', start)
    #date_handler = CommandHandler('date', current_date)
    #translation_handler = CommandHandler('movie', movie)
    audio_handler = MessageHandler(Filters.voice, audio_msg)
    message_handler = MessageHandler(Filters.text, message)
    unknown_handler = MessageHandler(Filters.command, not_defined)
    
    #adding handlers in the dispatcher
    dispatcher.add_handler(start_cmd_handler)
    #dispatcher.add_handler(translation_handler)
    #dispatcher.add_handler(date_handler)
    dispatcher.add_handler(unknown_handler)
    dispatcher.add_handler(message_handler)
    dispatcher.add_handler(audio_handler)
    dispatcher.add_error_handler(error_handler)
    #this command is used to start the bot
    updater.start_polling()
    #this is used to keep the bot idle
    updater.idle()

run_bot()