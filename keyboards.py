from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup


mainMenu_time = KeyboardButton(text='Налаштування🛠')
mainMenu_go = KeyboardButton(text='Почати🎲')
Main = ReplyKeyboardMarkup(resize_keyboard=True)
Main.add(mainMenu_time, mainMenu_go)


inline_btn_1 = InlineKeyboardButton(text='📑Записати розклад', callback_data='start_go')
inline_btn_2 = InlineKeyboardButton(text='🔊Змінити стан нагадування', callback_data='add_time')
inline_start = InlineKeyboardMarkup()
inline_start.add(inline_btn_1, inline_btn_2)


states = KeyboardButton(text='❌Cancel❗')
states_miss = KeyboardButton(text='❎Пропустити')
all_states = ReplyKeyboardMarkup(resize_keyboard=True)
all_states.add(states, states_miss)