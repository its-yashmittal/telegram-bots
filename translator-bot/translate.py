from google_trans_new import google_translator
translator = google_translator()
def translatorFn(transcription, target):
    if target==1:
        translate_text = translator.translate(transcription,lang_tgt='en')  
    elif target==2:
        translate_text = translator.translate(transcription, lang_tgt='hi')
    elif target==3:
        translate_text = translator.translate(transcription, lang_tgt='zh-cn')
    elif target==4:
        translate_text = translator.translate(transcription, lang_tgt='es')
    return translate_text