import telebot
from telebot import types


token = ''
bot = telebot.TeleBot(token)

joined_file = open("documents/users_1.txt", "r")
joined_users = set()
for line in joined_file:
    joined_users.add(line.strip())
joined_file.close()

plan = ''
menu = ''
shtat = ''
crug = ''
reyt = ''

play = types.InlineKeyboardMarkup()
play.row(types.InlineKeyboardButton('Душевная', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_17'), (types.InlineKeyboardButton('Утренняя', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_16')), (types.InlineKeyboardButton('Танцующая', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_15')))
play.row(types.InlineKeyboardButton('Космическая', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_14'), (types.InlineKeyboardButton('Влюблённая', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_12')), (types.InlineKeyboardButton('Мотивационная', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_11')))
play.row(types.InlineKeyboardButton('Космос FM', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-158297736_2'), (types.InlineKeyboardButton('Мечтательная', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_9')), (types.InlineKeyboardButton('Зимняя', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_8')))
play.row(types.InlineKeyboardButton('Новогоднее', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_6'), (types.InlineKeyboardButton('Вожатские', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_7')), (types.InlineKeyboardButton('Атмокаст', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_5')))
play.row(types.InlineKeyboardButton('Зарядки', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_4'), (types.InlineKeyboardButton('Свечки', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_3')), (types.InlineKeyboardButton('Наше творчество', url='https://vk.com/audios-401713?section=playlists&z=audio_playlist-401713_2')))

uver = types.InlineKeyboardMarkup()
uver.row(types.InlineKeyboardButton('Да', callback_data='da'))
uver.row(types.InlineKeyboardButton('Нет', callback_data='net'))

mat = types.InlineKeyboardMarkup()
mat.row(types.InlineKeyboardButton('Игротека', url="https://drive.google.com/drive/folders/1i45-GR1HBY7WfMNiOZZgTiWbufLtMZW1"))
mat.row(types.InlineKeyboardButton('Свечки', url="https://drive.google.com/drive/folders/1LTKLUcH_9CP1oGkRiYcP6v1d7Ir6Ay_p"))
mat.row(types.InlineKeyboardButton('Отрядки', url="https://drive.google.com/drive/folders/1EJNDOqGIDsqy0sCf3NZVAT6C_8dxrIm9"))

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("План дня 📃")
btn13 = types.KeyboardButton("Рейтинг 📊")
btn11 = types.KeyboardButton("Круговерть 🔔")
btn01 = types.KeyboardButton("Меню 🍽")
btn3 = types.KeyboardButton("Плейлисты 🔊")
btn2 = types.KeyboardButton("Штатка 👤")
btn4 = types.KeyboardButton("Полезное 🛑")
btn5 = types.KeyboardButton("Отчёт 🖥")

markup.add(btn1, btn5)
markup.add(btn13, btn11)
markup.add(btn01, btn2)
markup.add(btn3, btn4)


@bot.message_handler(commands=['start'])
def start(message):
    TO_CHAT_ID = -1001605529954
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!"
                                           "\nЯ постараюсь сделать твою смену немного "
                                           "легче!\n\nПо вопросам "
                                           "технической помощи "
                                           "вк: vk.com/akeeo\nпочта: danilkov@atmosfera.moscow\nтг: @DanilkovvD".format(message.from_user))

    message = bot.send_message(message.chat.id, text='Введи пароль, чтобы продолжить:')
    bot.register_next_step_handler(message, passs)

@bot.message_handler(commands=['ras'])
def mess(message):
    for user in joined_users:
        bot.send_message(user, message.text[message.text.find(" "):])

def test1(message):
    global plan
    a = 1
    TO_CHAT_ID = -1001605529954
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'documents/' + message.photo[1].file_id + str(a) + '.jpg'
    plan = src
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "План дня добавлен")

def passs(message):
    TO_CHAT_ID = -1001605529954
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    if message.text == "RtEQxtFFF21675012xtAAAA_Q3_0":
        bot.send_message(message.chat.id, text="Доступ предоставлен", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Отказано в доступе")

def test2(message):
    global menu
    a = 1
    TO_CHAT_ID = -1001605529954
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'documents/' + message.photo[1].file_id + str(a) + '.jpg'
    menu = src
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Меню добавлено")

def test3(message):
    global shtat
    TO_CHAT_ID = -1001605529954
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    shtat = message.text
    bot.reply_to(message, "Штатка добавлена")

def test11(message):
    global crug
    a = 1
    TO_CHAT_ID = -1001605529954
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'documents/' + message.photo[1].file_id + str(a) + '.jpg'
    crug = src
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Кружки добавлены")

def test6(message):
    global reyt
    TO_CHAT_ID = -1001605529954
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    reyt = message.text
    bot.reply_to(message, "Рейтинг добавлен")

def otchet(message):
    TO_CHAT_ID = -1001816111607
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    message = bot.send_message(message.chat.id, text='Отчёт доставлен✅')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/дплан":
        TO_CHAT_ID = -1001605529954
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        message = bot.send_message(message.chat.id, text='Пришли мне фото расписания')
        bot.register_next_step_handler(message, test1)
    elif message.text == "План дня 📃":
        TO_CHAT_ID = -1001605529954
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        joined_file = open("documents/users_1.txt", "a")
        joined_file.write(str(message.chat.id)+"\n")
        joined_users.add(message.chat.id)

        bot.send_photo(message.chat.id, open(plan, 'rb'))
    elif message.text == "/дменю":
        TO_CHAT_ID = -1001605529954
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        message = bot.send_message(message.chat.id, text='Пришли мне фото меню')
        bot.register_next_step_handler(message, test2)
    elif message.text == "Меню 🍽":
        TO_CHAT_ID = -1001605529954
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        bot.send_photo(message.chat.id, open(menu, 'rb'))
    elif message.text == "/дштатка":
        TO_CHAT_ID = -1001605529954
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        message = bot.send_message(message.chat.id, text='Пришли мне штатку (Текст)')
        bot.register_next_step_handler(message, test3)
    elif message.text == "Штатка 👤":
        TO_CHAT_ID = -1001605529954
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        bot.send_message(message.chat.id, text=shtat)
    elif message.text == "Плейлисты 🔊":
        TO_CHAT_ID = -1001605529954
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        bot.send_message(message.chat.id, text="Держи", reply_markup=play)
    elif message.text == "Полезное 🛑":
        TO_CHAT_ID = -1001605529954
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        bot.send_message(message.chat.id, text="Держи", reply_markup=mat)
    elif message.text == "/дкружки":
        TO_CHAT_ID = -1001605529954
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        message = bot.send_message(message.chat.id, text='Пришли мне фото расписания')
        bot.register_next_step_handler(message, test11)
    elif message.text == "Круговерть 🔔":
        TO_CHAT_ID = -1001605529954
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        bot.send_photo(message.chat.id, open(crug, 'rb'))
    elif message.text == "/дрейтинг":
        TO_CHAT_ID = -1001605529954
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        message = bot.send_message(message.chat.id, text='Пришли мне рейтинг в формате:'
                                                         '\nАктуальный рейтинг на xx.xx.xxxx\n1 отряд - xx баллов'
                                                         '\n2 отряд - xx баллов')
        bot.register_next_step_handler(message, test6)

    elif message.text == "Рейтинг 📊":
        TO_CHAT_ID = -1001605529954
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        bot.send_message(message.chat.id, text=reyt)

    elif message.text == "Отчёт 🖥":
        TO_CHAT_ID = -1001605529954
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
        message = bot.send_message(message.chat.id, text='Ты уверен, что хочешь отправить отчёт?', reply_markup=uver)


@bot.message_handler(content_types=['photo'])
def handle_docs_document(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = '/smena/documents' + message.photo[1].file_id + '.jpg'
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Фото добавлено")



@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == "da":
        message = bot.send_message(call.message.chat.id, text='Пришли мне отчёт одним сообщением')
        bot.register_next_step_handler(message, otchet)
    elif call.data == "net":
        message = bot.send_message(call.message.chat.id, text='Отправка отчёта отменена')


bot.infinity_polling()
