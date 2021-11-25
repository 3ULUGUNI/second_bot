import telebot
from config import TOKEN, getRegData
from telebot import types
import urllib



markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup1.row("Телефоны и их характеристики", "Выбрать и купить товар", "Информация о боте", "Корзина")
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Добрый день! Я помогу тебе с выбором и покупкой товара!", reply_markup=markup1)
@bot.message_handler(content_types=['text'])
def charakters(message):
    if message.text == "Телефоны и их характеристики":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=False)
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup2.row("IPHONE", "SAMSUNG", "MI", "Назад в меню")
        bot.send_message(message.chat.id, "Выберите марку телефона", reply_markup=markup2)
    if message.text == "IPHONE":
        iphone13 = open('PHONE/13.webp', 'rb')
        iphone11 = open('PHONE/11.webp', 'rb')
        iphone12 = open('PHONE/12PRO.webp', 'rb')
        bot.send_photo(message.chat.id, iphone13, "IPHONE 13 Pro Max\n"
                                                  "Цвет: Синий\n"
                                                  "Дисплей: Super Retina XDR. "
                                                  "OLED, на всю переднюю панель, диагональ 6,7 дюйма\n"
                                                  "Размеры и вес: Длина - 8 мм, ширина - 78,1 мм, Толщина - 7,65 мм\n"
                                                  "Процессор: Рейтинг IP68 по стандарту IEC 60529 (допускается погружение в воду на глубину до 6 метров длительностью до 30 минут)\n"
                                                  "Цена: 129048")
        bot.send_photo(message.chat.id, iphone11, "IPHONE 13 Pro Max\n"
                                                  "Цвет: Синий\n"
                                                  "Дисплей: Super Retina XDR. "
                                                  "OLED, на всю переднюю панель, диагональ 6,7 дюйма\n"
                                                  "Размеры и вес: Длина - 8 мм, ширина - 78,1 мм, Толщина - 7,65 мм\n"
                                                  "Процессор: Рейтинг IP68 по стандарту IEC 60529 (допускается погружение в воду на глубину до 6 метров длительностью до 30 минут)\n"
                                                  "Цена: 129048")
        bot.send_photo(message.chat.id, iphone12, "IPHONE 13 Pro Max\n"
                                                  "Цвет: Синий\n"
                                                  "Дисплей: Super Retina XDR. "
                                                  "OLED, на всю переднюю панель, диагональ 6,7 дюйма\n"
                                                  "Размеры и вес: Длина - 8 мм, ширина - 78,1 мм, Толщина - 7,65 мм\n"
                                                  "Процессор: Рейтинг IP68 по стандарту IEC 60529 (допускается погружение в воду на глубину до 6 метров длительностью до 30 минут)\n"
                                                  "Цена: 129048")
    elif message.text == "SAMSUNG":
        iphone13 = open('PHONE/13.webp', 'rb')
        iphone11 = open('PHONE/11.webp', 'rb')
        iphone12 = open('PHONE/12PRO.webp', 'rb')
        bot.send_photo(message.chat.id, iphone13, "IPHONE 13 Pro Max\n"
                                                  "Цвет: Синий\n"
                                                  "Дисплей: Super Retina XDR. "
                                                  "OLED, на всю переднюю панель, диагональ 6,7 дюйма\n"
                                                  "Размеры и вес: Длина - 8 мм, ширина - 78,1 мм, Толщина - 7,65 мм\n"
                                                  "Процессор: Рейтинг IP68 по стандарту IEC 60529 (допускается погружение в воду на глубину до 6 метров длительностью до 30 минут)\n"
                                                  "Цена: 129048")
        bot.send_photo(message.chat.id, iphone11, "IPHONE 13 Pro Max\n"
                                                  "Цвет: Синий\n"
                                                  "Дисплей: Super Retina XDR. "
                                                  "OLED, на всю переднюю панель, диагональ 6,7 дюйма\n"
                                                  "Размеры и вес: Длина - 8 мм, ширина - 78,1 мм, Толщина - 7,65 мм\n"
                                                  "Процессор: Рейтинг IP68 по стандарту IEC 60529 (допускается погружение в воду на глубину до 6 метров длительностью до 30 минут)\n"
                                                  "Цена: 129048")
        bot.send_photo(message.chat.id, iphone12, "IPHONE 13 Pro Max\n"
                                                  "Цвет: Синий\n"
                                                  "Дисплей: Super Retina XDR. "
                                                  "OLED, на всю переднюю панель, диагональ 6,7 дюйма\n"
                                                  "Размеры и вес: Длина - 8 мм, ширина - 78,1 мм, Толщина - 7,65 мм\n"
                                                  "Процессор: Рейтинг IP68 по стандарту IEC 60529 (допускается погружение в воду на глубину до 6 метров длительностью до 30 минут)\n"
                                                  "Цена: 129048")
    elif message.text == "MI":
        resource = urllib.urlopen("https://mi-shop.kg/wp-content/uploads/2021/05/poco_x3_pro_zolotoy_ava1-800x800_wmark-300x300.jpg")
        out = open("...\img.jpg", 'wb')
        k = out.write(resource.read())
        bot.send_photo(message.chat.id, k)

    elif message.text == "Назад в меню":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=False)
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup2.row("Телефоны и их характеристики", "Выбрать и купить товар", "Информация о боте")

    elif message.text == "Выбрать и купить товар":
        markup3 = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("IPHONE", callback_data="I")
        item2 = types.InlineKeyboardButton("SAMSUNG", callback_data="S")
        item3 = types.InlineKeyboardButton("MI", callback_data="M")
        markup3.add(item1, item2, item3)
        bot.send_message(message.chat.id, f"<b>Выбери марку телефона</b>", reply_markup=markup3,
                         parse_mode="html")
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
            if call.data == "S":
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("IPHONE13", callback_data="13")
                item2 = types.InlineKeyboardButton("IPHONE12", callback_data="12")
                item3 = types.InlineKeyboardButton("IPHONE11", callback_data="11")
                markup.add(item1, item2, item3)
                bot.send_message(call.message.chat.id, f"<b>Выберите марку телефона</b>", reply_markup=markup, parse_mode="html")
    except Exception as e:
        print(repr(e))





bot.polling(none_stop=True)