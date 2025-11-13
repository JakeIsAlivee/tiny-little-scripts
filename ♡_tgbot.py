import telebot
TGB = telebot.TeleBot('token')

herid = '0'
myid = '1'

@TGB.message_handler(content_types=['text','animation','audio','contact','document','location','photo','sticker','video','voice'])
def correspondance(message):
    if str(message.from_user.id) == myid:
        TGB.copy_message(herid,myid,message.message_id)
    if str(message.from_user.id) == herid:
        TGB.copy_message(myid,herid,message.message_id)
    else:
        TGB.send_sticker(message.from_user.id,'CAACAgIAAxkBAAEN4KVnuhkyYdsELaU1bTlBC7xjv-Zy5QAC8ksAAt8fwElJI0IgrcwkVjYE')


TGB.infinity_polling()