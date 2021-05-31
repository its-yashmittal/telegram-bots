bot_token ="1750591707:AAG6fYZzz0lEyuybZOUn47Og67Z84bkDxNw"
from telegram.ext import MessageHandler, CommandHandler, Filters, Updater, updater
from translate import translatorFn 
from speechToText import audio_processor
from textToSpeech import textToSpeech
import requests
bot_cmd_list = []
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello I am Yash's Translator Bot!\
        \njust type the command corresponding to your target language and then in the next message send the text you want to translate !!!\
        NOTE: The commands correspond to the target language you want your expression in!\n\
        Command List:\n1./en\n2./hn\n3./cn\n4./es")

def eng(update, context):
    bot_cmd_list.append(1)

def hin(update, context):
    bot_cmd_list.append(2)

def chn(update, context):
    bot_cmd_list.append(3)
def esp(update, context):
    bot_cmd_list.append(4)

def message(update, context):
    print(update)
    transcription = update.message.text
    translate_text = translatorFn(transcription, bot_cmd_list[-1])
    print(translate_text)
    #textToSpeech(translate_text)
    context.bot.send_message(chat_id=update.effective_chat.id, text = translate_text)
    
def error_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ooops!!Looks like my translator broke😥!")
def audio_msg(update, context):
    print("Hey, please wait I am transcripting your audio!")
    audio_file = context.bot.getFile(update.message.voice.file_id)
    audio_file.download('voice.ogg')
    transcription = audio_processor()
    print("calling translator with " + transcription)
    context.bot.send_message(chat_id=update.effective_chat.id, text="You just said "+transcription+" in the voice note!")
    tranlate_text = translatorFn(transcription, bot_cmd_list[-1])
    context.bot.send_message(chat_id=update.effective_chat.id, text="Translated Text: " + tranlate_text)
    textToSpeech(tranlate_text)
    # with open('reply.ogg', 'rb') as audio:
    #     payload = {
    #         'chat_id': update.effective_chat.id,
    #         'title': 'reply.ogg',
    #         'parse_mode': 'HTML'
    #     }
    #     files = {
    #         'audio': audio.read(),
    #     }
    #     resp = requests.post(
    #         "https://api.telegram.org/bot{token}/sendAudio".format(token=bot_token),
    #         data=payload,
    #         files=files).json()
    # context.bot.send_audio(chat_id=update.effective_chat.id, audio_msg = open("reply.ogg", 'rb'))

def not_defined(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, this is not a supported command!\
        \nThe list of available commands is:\
        \n1./start to start the bot\
        \n2./en for translation into English\
        \n3./hi for translation into Hindi\
        \n4./cn for translation into chinese\
        \n5./es for translation into spanish")


def run_bot():
    updater = Updater(bot_token)
    dispatcher = updater.dispatcher
    start_cmd_handler = CommandHandler('start', start)
    en_cmd_handler = CommandHandler('en', eng)
    hn_cmd_handler = CommandHandler('hi', hin)
    cn_cmd_handler = CommandHandler('cn', chn)
    es_cmd_handler = CommandHandler('es', esp)
    audio_handler = MessageHandler(Filters.voice, audio_msg)
    message_handler = MessageHandler(Filters.text, message)
    unknown_handler = MessageHandler(Filters.command, not_defined)
    
    #adding handlers in the dispatcher
    dispatcher.add_handler(start_cmd_handler)
    dispatcher.add_handler(en_cmd_handler)
    dispatcher.add_handler(hn_cmd_handler)
    dispatcher.add_handler(cn_cmd_handler)
    dispatcher.add_handler(es_cmd_handler)
    dispatcher.add_handler(unknown_handler)
    dispatcher.add_handler(message_handler)
    dispatcher.add_handler(audio_handler)
    dispatcher.add_error_handler(error_handler)
    #this command is used to start the bot
    updater.start_polling()
    #this is used to keep the bot idle
    updater.idle()

run_bot()