from datetime import datetime, timedelta

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters)

T_INFO, T_ALOQA, T_RASMLAR, T_DARSLAR, T_BIRTH = (
    '🖇info', '🤙aloqa', '🎑rasmlar', '📆jadval', "🥳tug'ilgan kunlar")
tugmalar = ReplyKeyboardMarkup([
    [T_INFO, T_ALOQA, T_RASMLAR], [T_DARSLAR, T_BIRTH]
], resize_keyboard=True)


def start(update, context):
    user = update.message.from_user
    buttons = [         
               [InlineKeyboardButton('Bizning kanal👉', url='https://t.me/URL')],
               [InlineKeyboardButton("a'zo bo'ldim😊", callback_data='Raxmat😊')]
              ]
    update.message.reply_html(
        "Assalomu alaykum <b>{}!</b>\n \n<b>hush kelibsiz!!!</b>\n \n 🤖Bu bot orqali siz o'zingizni qiziqtirgan savollarga albatta javob topasiz, lekin avval kanalga a'zo bo'ling!!!".
            format(user.first_name), reply_markup=InlineKeyboardMarkup(buttons))


def inline_callback(update, context):
    try:
        std = update.callback_query
        std.message.delete()
        std.message.reply_html(text="<b>Tanlov uchun tashakkur</b>\n\n {} \n\ntanlash👇".format(std.data),reply_markup=tugmalar)
    except Exception as e:
        print('error ', str(e))

def malumotlar(update, context):
    try:
        photo_path = 'hkte.jpg'
        message = "<b>HKTE</b>2️⃣0️⃣2️⃣1️⃣ \n<b>{}</b> bu guruh AVIATSIYA TRANSPORTI MUHANDISLIGI".format('Havo Kemalarining Texnik Ekspluatatsiyasi')
    
        update.message.reply_photo(photo=open(photo_path, 'rb'), caption=message, parse_mode='HTML',
                                   reply_markup=main_buttons)
    except Exception as e:
        print('error ', str(e))

def aloqa(update, context):
    update.message.reply_text("a'loqa uchun: @netotxodit ga yozing📬")

def rasm(update, context):
    photo_path = '1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg'
    update.message.reply_photo(photo=open(photo_path, 'rb'),
                                   reply_markup=main_buttons)

def jadval(update, context):
    photo_path = '6.jpg'
    update.message.reply_photo(photo=open(photo_path, 'rb'),
                                   reply_markup=main_buttons)
def happybirth(update, context):

    YAQ = "SH.SHAXZOD 11.05.2002"     

    kunlar = [
                [InlineKeyboardButton("⌛️eng yaqin", callback_data=YAQ)],
                [InlineKeyboardButton("🌈bahor", url='https://t.me/URL')],
                [InlineKeyboardButton("☀️yoz", url='https://t.me/URL')],
                [InlineKeyboardButton("☔️kuz", url='https://t.me/URL')],
                [InlineKeyboardButton("❄️qish", url='https://t.me/URL')]
               ]
    update.message.reply_text('Bittasini tanlang:⬇️', reply_markup=InlineKeyboardMarkup(kunlar))


def main():
    # Updater o`rnatib olamiz
    updater = Updater('1330438263:AAGDYPG5miH8BaWPl1D1BKIF4Eg59w4jIA8', use_context=True)

    # Dispatcher eventlarni aniqlash uchun
    dispatcher = updater.dispatcher

    # start kommandasini ushlab qolish
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(inline_callback))
    dispatcher.add_handler(MessageHandler(Filters.regex('^(' + T_INFO + ')$'), malumotlar))
    dispatcher.add_handler(MessageHandler(Filters.regex('^(' + T_ALOQA + ')$'), aloqa))
    dispatcher.add_handler(MessageHandler(Filters.regex('^(' + T_RASMLAR + ')$'), rasm))
    dispatcher.add_handler(MessageHandler(Filters.regex('^(' + T_DARSLAR + ')$'), jadval))
    dispatcher.add_handler(MessageHandler(Filters.regex('^(' + T_BIRTH + ')$'), happybirth))


    updater.start_polling()
    updater.idle()


main()