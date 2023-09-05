import time
import random
import openai
import telebot
from telebot import types
from telebot.types import InputMediaPhoto
import datetime
from dotenv import load_dotenv
import os

load_dotenv()


print('Starting smena_bot!')

token = os.getenv('TG_TOKEN')
bot = telebot.TeleBot(token)
openai.api_key = os.getenv('OPENAI_TOKEN')

chat_otchet = "" # Прописать ID чата культоргов для доставки отчётов. Обратить особое внимание!
debug_logs = "" # Прописать ID чата, куда будут доставляться логи работы бота. Проверьте, что данный ID не совпадает с ID выше.

plan_for_the_day = ""
TIME_plan_for_the_day = ""
hobby_one = ""
TIME_hobby_one = ""
hobby_two = ""
hobby_three = ""
dining_room = ""
TIME_dining_room = ""
phone_book = ""
rating = ""
TIME_rating = ""

pod = types.InlineKeyboardMarkup()
pod.row(types.InlineKeyboardButton('Принять', callback_data='pood'))

play = types.InlineKeyboardMarkup()
play.row(types.InlineKeyboardButton('Душевная', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_17'), (types.InlineKeyboardButton('Утренняя', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_16')), (types.InlineKeyboardButton('Танцующая', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_15')))
play.row(types.InlineKeyboardButton('Космическая', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_14'), (types.InlineKeyboardButton('Влюблённая', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_12')), (types.InlineKeyboardButton('Мотивационная', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_11')))
play.row(types.InlineKeyboardButton('Космос FM', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-158297736_2'), (types.InlineKeyboardButton('Мечтательная', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_9')), (types.InlineKeyboardButton('Зимняя', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_8')))
play.row(types.InlineKeyboardButton('Новогоднее', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_6'), (types.InlineKeyboardButton('Вожатские', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_7')), (types.InlineKeyboardButton('Атмокаст', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_5')))
play.row(types.InlineKeyboardButton('Зарядки', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_4'), (types.InlineKeyboardButton('Свечки', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_3')), (types.InlineKeyboardButton('Наше творчество', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_2')))

useful = types.InlineKeyboardMarkup()
useful.row(types.InlineKeyboardButton('Игротека', url="https://drive.google.com/drive/folders/1i45-GR1HBY7WfMNiOZZgTiWbufLtMZW1"))
useful.row(types.InlineKeyboardButton('Свечки', url="https://drive.google.com/drive/folders/1LTKLUcH_9CP1oGkRiYcP6v1d7Ir6Ay_p"))
useful.row(types.InlineKeyboardButton('Отрядки', url="https://drive.google.com/drive/folders/1EJNDOqGIDsqy0sCf3NZVAT6C_8dxrIm9"))

access_denied = types.InlineKeyboardMarkup()
access_denied.row(types.InlineKeyboardButton('Ввести пароль заново', callback_data='re-enter_the_password'))

sure_phone_book = types.InlineKeyboardMarkup()
sure_phone_book.row(types.InlineKeyboardButton('Уверен, хочу отправить отчёт', callback_data='yes'))
sure_phone_book.row(types.InlineKeyboardButton('Нет, сорри, верните меня в меню', callback_data='no'))

sure_p = types.InlineKeyboardMarkup()
sure_p.row(types.InlineKeyboardButton('Уверен, хочу отправить лайк или дизлайк', callback_data='yes_l'))
sure_p.row(types.InlineKeyboardButton('Нет, сорри, верните меня в меню', callback_data='no'))

how_play = types.InlineKeyboardMarkup()
how_play.row(types.InlineKeyboardButton('Порядок проведения игры', callback_data='game_por'), types.InlineKeyboardButton('Первичная тактилка', callback_data='game_pertak'))
how_play.row(types.InlineKeyboardButton('Вторичная тактилка', callback_data='game_vtortak'), types.InlineKeyboardButton('Первичное знакомство', callback_data='perv_znakomstvo'))
how_play.row(types.InlineKeyboardButton('Закрепление знакомства', callback_data='zakrep_znak'), types.InlineKeyboardButton('Розыгрыши', callback_data='rozgr'))
how_play.row(types.InlineKeyboardButton('Выявление лидера', callback_data='lider'), types.InlineKeyboardButton('Миксеры', callback_data='mikser'))
how_play.row(types.InlineKeyboardButton('Секс', callback_data='seks'))

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("План дня 📃")
btn2 = types.KeyboardButton("Кружки 🔔")
btn3 = types.KeyboardButton("Меню 🍽")
btn4 = types.KeyboardButton("Штатка 👤")
btn5 = types.KeyboardButton("Отчёт 🖥")
btn6 = types.KeyboardButton("Рейтинг 📊")
btn7 = types.KeyboardButton("Music 🔊")
btn8 = types.KeyboardButton("Полезно 🛑")
btn9 = types.KeyboardButton("ChatGPT")
btn10 = types.KeyboardButton("👍 or 👎")
btn11 = types.KeyboardButton("Игры 🦴")
menu.add(btn1, btn2, btn3)
menu.add(btn4, btn5, btn6)
menu.add(btn7, btn8)
menu.add(btn10, btn9, btn11)

admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
bt1 = types.KeyboardButton("обновить план дня")
bt2 = types.KeyboardButton("обновить кружки")
bt3 = types.KeyboardButton("обновить меню")
bt4 = types.KeyboardButton("обновить штатку")
bt5 = types.KeyboardButton("обновить рейтинг")
bt6 = types.KeyboardButton("вернуться в меню")
admin.add(bt1)
admin.add(bt2)
admin.add(bt3)
admin.add(bt4)
admin.add(bt5)
admin.add(bt6)

photo = types.ReplyKeyboardMarkup(resize_keyboard=True)
bb1 = types.KeyboardButton("одно фото")
bb2 = types.KeyboardButton("два фото")
bb3 = types.KeyboardButton("три фото")
photo.add(bb1)
photo.add(bb2)
photo.add(bb3)


@bot.message_handler(commands=['start'])
def start(message):
    TO_CHAT_ID = 736959096
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! \n\nПо вопросам технической помощи "
                                           "вк: vk.com/v_mango_d\nтг: @DanilkovvD".format(message.from_user))
    time.sleep(0.5)
    bot.send_message(message.chat.id, text="Нажимая данную кнопку, вы подтвердждаете, что не будете передавать название, ссылку или другую информацию позволяющую получить доступ к боту третьим лицам", reply_markup=pod)


@bot.message_handler(commands=['ad'])
def start(message):
    bot.send_message(message.chat.id, text="Добро пожаловать, администратор!", reply_markup=admin)


def password(message):
    password = message.text
    try:
        if password.lower() == "я люблю своих детей":
            bot.send_message(message.chat.id, text="Доступ предоставлен", reply_markup=menu)
            TO_CHAT_ID = 736959096
            bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        else:
            bot.send_message(message.chat.id, text="Пароль отличен от заданного", reply_markup=access_denied)
    except Exception as e:
        bot.send_message(message.chat.id, text="В доступе отказано\n\nLOGS: {" + e + "}")


def update_the_plan_for_the_day(message):
    global TIME_plan_for_the_day
    TIME_plan_for_the_day = datetime.datetime.now()
    global plan_for_the_day
    TO_CHAT_ID = 736959096
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    a = 1
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'downoload/' + message.photo[1].file_id + str(a) + '.jpg'
    plan_for_the_day = src
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "План дня добавлен")


def chatgp(message):
    TO_CHAT_ID = 736959096
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    bot.reply_to(message, "Ожидайте ответа, нейросеть думает")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    msg = bot.send_message(message.chat.id, text=response['choices'][0]['text'], reply_markup=menu)


def one_photo(message):
    global TIME_hobby_one
    TIME_hobby_one = datetime.datetime.now()
    global hobby_one
    global hobby_two
    global hobby_three
    hobby_two = ""
    hobby_three = ""
    a = 1
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'downoload/' + message.photo[1].file_id + str(a) + '.jpg'
    hobby_one = src
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Кружки добавлены")


def two_photo(message):
    global hobby_one
    global TIME_hobby_one
    TIME_hobby_one = datetime.datetime.now()
    global hobby_three
    hobby_three = ""
    a = 1
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'downoload/' + message.photo[1].file_id + str(a) + '.jpg'
    hobby_one = src
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    message = bot.reply_to(message, "Первое фото добавлено. Пришли мне второе фото")
    bot.register_next_step_handler(message, two_photo_step_two)


def two_photo_step_two(message):
    global hobby_two
    a = 1
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'downoload/' + message.photo[1].file_id + str(a) + '.jpg'
    hobby_two = src
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Второе фото обновлено. Кружки успешно добавлены")


def three_photo(message):
    global hobby_one
    global TIME_hobby_one
    TIME_hobby_one = datetime.datetime.now()
    a = 1
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'downoload/' + message.photo[1].file_id + str(a) + '.jpg'
    hobby_one = src
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    message = bot.reply_to(message, "Первое фото добавлено. Пришли мне второе фото")
    bot.register_next_step_handler(message, three_photo_step_two)


def three_photo_step_two(message):
    global hobby_two
    a = 1
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'downoload/' + message.photo[1].file_id + str(a) + '.jpg'
    hobby_two = src
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Второе фото обновлено. Пришли мне третье фото")
    bot.register_next_step_handler(message, three_photo_step_three)


def three_photo_step_three(message):
    global hobby_three
    a = 1
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'downoload/' + message.photo[1].file_id + str(a) + '.jpg'
    hobby_three = src
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Кружки добавлены")


def add_dining_room(message):
    global dining_room
    global TIME_dining_room
    TIME_dining_room = datetime.datetime.now()
    a = 1
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'downoload/' + message.photo[1].file_id + str(a) + '.jpg'
    dining_room = src
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Новое меню добавлено")

def add_phone_book(message):
    global phone_book
    phone_book = message.text
    bot.reply_to(message, "Штатка добавлена")


def send_a_report(message):
    TO_CHAT_ID = -1001828048973
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    message = bot.send_message(message.chat.id, text='Отчёт доставлен✅', reply_markup=menu)

def add_rating(message):
    global rating
    global TIME_rating
    TIME_rating = datetime.datetime.now()
    rating = message.text
    bot.reply_to(message, "Рейтинг добавлен")

def obratka(message):
    TO_CHAT_ID = -1001828048973
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    message = bot.send_message(message.chat.id, text='Успешно✅', reply_markup=menu)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "вернуться в меню":
        bot.send_message(message.chat.id, text='Хорошо, вот меню', reply_markup=menu)

    elif message.text == "меню 💼":
        bot.send_message(message.chat.id, text='Хорошо, вот меню', reply_markup=menu)

    elif message.text == "обновить план дня":
        message = bot.send_message(message.chat.id, text='Пришли мне фото расписания', reply_markup=menu)
        bot.register_next_step_handler(message, update_the_plan_for_the_day)

    elif message.text == "План дня 📃":
        print(TIME_plan_for_the_day)
        bot.send_message(message.chat.id, text='План дня обновлён:\n' + str(TIME_plan_for_the_day))
        bot.send_photo(message.chat.id, open(plan_for_the_day, 'rb'), reply_markup=menu)

    elif message.text == "обновить кружки":
        bot.send_message(message.chat.id, text='Сколько фото ты хошечь загрузить?', reply_markup=photo)

    elif message.text == "одно фото":
        bot.send_message(message.chat.id, text='Хорошо, отправь мне фото', reply_markup=menu)
        bot.register_next_step_handler(message, one_photo)

    elif message.text == "два фото":
        bot.send_message(message.chat.id, text='Хорошо, отправь мне ПЕРВОЕ фото, затем я ПОПРОШУ ВТОРОЕ', reply_markup=menu)
        bot.register_next_step_handler(message, two_photo)
    
    elif message.text == "три фото":
        bot.send_message(message.chat.id, text='Хорошо, отправь мне ПЕРВОЕ фото, затем я ПОПРОШУ ОСТАЛЬНЫЕ', reply_markup=menu)
        bot.register_next_step_handler(message, three_photo)

    elif message.text == "Кружки 🔔":
        bot.send_message(message.chat.id, text='Кружки обновлены:\n' + str(TIME_hobby_one))
        f1 = open(hobby_one, "rb")
        if hobby_three != "":
            f2 = open(hobby_two, "rb")
            f3 = open(hobby_three, "rb")
            bot.send_media_group(message.chat.id, [InputMediaPhoto(f1), InputMediaPhoto(f2), InputMediaPhoto(f3)])
        else:
            if hobby_two != "":

                f2 = open(hobby_two, "rb")
                bot.send_media_group(message.chat.id, [InputMediaPhoto(f1), InputMediaPhoto(f2)])
            else:
                bot.send_photo(message.chat.id, f1, reply_markup=menu)

    elif message.text == "обновить меню":
        message = bot.send_message(message.chat.id, text='Пришли мне фото меню', reply_markup=menu)
        bot.register_next_step_handler(message, add_dining_room)

    elif message.text == "Меню 🍽":
        bot.send_message(message.chat.id, text='Меню обновлено:\n' + str(TIME_dining_room))
        bot.send_photo(message.chat.id, open(dining_room, 'rb'), reply_markup=menu)

    elif message.text == "обновить штатку":
        message = bot.send_message(message.chat.id, text='Пришли мне штатку (Текст)', reply_markup=menu)
        bot.register_next_step_handler(message, add_phone_book)

    elif message.text == "Штатка 👤":
        bot.send_message(message.chat.id, text=phone_book, reply_markup=menu)

    elif message.text == "Отчёт 🖥":
        bot.send_message(message.chat.id, text='Ты уверен, что хочешь отправить отчёт?', reply_markup=sure_phone_book)

    elif message.text == "👍 or 👎":
        bot.send_message(message.chat.id, text='Если тебе есть кому поставить лайк или дизлайк, ты выбрал правильный пункт', reply_markup=sure_p)

    elif message.text == "обновить рейтинг":
        message = bot.send_message(message.chat.id, text='Пришли мне рейтинг в формате:'
                                                         '\nАктуальный рейтинг на xx.xx.xxxx\n1 отряд - xx баллов'
                                                         '\n2 отряд - xx баллов', reply_markup=menu)
        bot.register_next_step_handler(message, add_rating)

    elif message.text == "Рейтинг 📊":
        bot.send_message(message.chat.id, text='Рейтинг обновлен:\n' + str(TIME_rating))
        bot.send_message(message.chat.id, text=rating)

    elif message.text == "Music 🔊":
        bot.send_message(message.chat.id, text="Держи наши плейлисты", reply_markup=play)

    elif message.text == "Полезно 🛑":
        bot.send_message(message.chat.id, text="Держи", reply_markup=useful)
    
    elif message.text == "ChatGPT":
        message = bot.send_message(message.chat.id, text='Напиши свой вопрос', reply_markup=menu)
        bot.register_next_step_handler(message, chatgp)

    elif message.text == "Игры 🦴":
        message = bot.send_message(message.chat.id, text='Выбирай блок', reply_markup=how_play)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == "re-enter_the_password":
        message = bot.send_message(call.message.chat.id, text='Введи пароль, чтобы продолжить:')
        bot.register_next_step_handler(message, password)

    elif call.data == "yes":
        message = bot.send_message(call.message.chat.id, text='Пришли мне отчёт одним сообщением.\n\n ФОРМАТ СООБЩЕНИЯ:\nМаксимум 1 фото\nНомер отряда')
        bot.register_next_step_handler(message, send_a_report)

    elif call.data == "no":
        bot.send_message(call.message.chat.id, text='окей, вот меню', reply_markup=menu)
    
    elif call.data == "yes_l":
        message = bot.send_message(call.message.chat.id, text='Окей! Напиши кому ты хочешь поставить лайк или дизайк в формате\n\nxx.xx.xxxx\nЛайк xxxx за')
        bot.register_next_step_handler(message, obratka)

    elif call.data == "game_pertak":
        bot.send_message(call.message.chat.id, text='окей, вот тебе игра')
        new_line = random.choice(open('pervtakt.txt').readlines())
        bot.send_message(call.message.chat.id, text=new_line, reply_markup=menu)

    elif call.data == "game_vtortak":
        bot.send_message(call.message.chat.id, text='окей, вот тебе игра')
        line = random.choice(open('vtortakt.txt').readlines())
        bot.send_message(call.message.chat.id, text=str(line), reply_markup=menu)

    elif call.data == "perv_znakomstvo":
        bot.send_message(call.message.chat.id, text='окей, вот тебе игра')
        line = random.choice(open('pervznak.txt').readlines())
        bot.send_message(call.message.chat.id, text=str(line), reply_markup=menu)

    elif call.data == "zakrep_znak":
        bot.send_message(call.message.chat.id, text='окей, вот тебе игра')
        line = random.choice(open('zakrepzn.txt').readlines())
        bot.send_message(call.message.chat.id, text=str(line), reply_markup=menu)
    
    elif call.data == "rozgr":
        bot.send_message(call.message.chat.id, text='окей, вот тебе игра')
        line = random.choice(open('rozgr.txt').readlines())
        bot.send_message(call.message.chat.id, text=str(line), reply_markup=menu)
    
    elif call.data == "lider":
        bot.send_message(call.message.chat.id, text='окей, вот тебе игра')
        line = random.choice(open('lider.txt').readlines())
        bot.send_message(call.message.chat.id, text=str(line), reply_markup=menu)
    
    elif call.data == "mikser":
        bot.send_message(call.message.chat.id, text='окей, вот тебе игра')
        line = random.choice(open('mikser.txt').readlines())
        bot.send_message(call.message.chat.id, text=str(line), reply_markup=menu)
    
    elif call.data == "seks":
        bot.send_message(call.message.chat.id, text='окей, вот тебе игра')
        line = random.choice(open('seks.txt').readlines())
        bot.send_message(call.message.chat.id, text=str(line), reply_markup=menu)

    elif call.data == "pood":
            message = bot.send_message(call.message.chat.id, text='Введи пароль, чтобы продолжить:')
            bot.register_next_step_handler(message, password)
    
    elif call.data == "game_por":
        bot.send_message(call.message.chat.id, text="1. Загон/легенда\n2. Название\n3. Цель\n4. Правила\n5. ТБ\n6. Всё ли понятно?\n7. УКВ\n8. Завершение", reply_markup=menu)


bot.infinity_polling()