from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.types.web_app_info import WebAppInfo

# start_ReplyKeyboard = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Общая информация', web_app=WebAppInfo(url="https://vk.com/pakkkharev"))],
#     [KeyboardButton(text='Гала-ужин', web_app=WebAppInfo(url='https://vk.com/pakkkharev'))],
#     [KeyboardButton(text='Конференция', web_app=WebAppInfo(url='https://vk.com/pakkkharev'))],
#     [KeyboardButton(text='Обратная связь', web_app=WebAppInfo(url='https://t.me/pakkkharev'))]
# ],
#             resize_keyboard=True,
#             input_field_placeholder='Выбери интересующий тебя пункт ниже!')

start_InlineKeyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Дайджест', web_app=WebAppInfo(url='https://master--inspiring-stroopwafel-ad3720.netlify.app'))],
    # [InlineKeyboardButton(text='Гала-ужин', callback_data='gala-dinner')],
    # [InlineKeyboardButton(text='Конференция', callback_data='meetup')],
    # [InlineKeyboardButton(text='Обратная связь', callback_data='feedback')]
])

# faq_InlineKeyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Что входит', web_app=WebAppInfo(url='https://vk.com/pakkkharev'))],
#     [InlineKeyboardButton(text='🗺 Карта', web_app=WebAppInfo(url='https://vk.com/pakkkharev'))],
#     [InlineKeyboardButton(text='🛏 Проживание', web_app=WebAppInfo(url='https://vk.com/pakkkharev'))],
#     [InlineKeyboardButton(text='◀️ Назад', callback_data='faq-cancel')]
    
# ])

# gala_dinner_InlineKeyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='❓Концепция', web_app=WebAppInfo(url='https://vk.com/pakkkharev'))],
#     [InlineKeyboardButton(text='🕘Тайминги', web_app=WebAppInfo(url='https://vk.com/pakkkharev'))],
#     [InlineKeyboardButton(text='🤵🏼‍♂️🤵🏼‍♀️Дресскод', web_app=WebAppInfo(url='https://vk.com/pakkkharev'))],
#     [InlineKeyboardButton(text='◀️ Назад', callback_data='gala-dinner-cancel')]
    
# ])

# meetup_InlineKeyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='❓Концепция', web_app=WebAppInfo(url='https://vk.com/pakkkharev'))],
#     [InlineKeyboardButton(text='🤔Панельная дискуссия', web_app=WebAppInfo(url='https://vk.com/pakkkharev'))],
#     [InlineKeyboardButton(text='🕘Тайминги', web_app=WebAppInfo(url='https://vk.com/pakkkharev'))],
#     [InlineKeyboardButton(text='🎤Спикеры', web_app=WebAppInfo(url='https://vk.com/pakkkharev'))],
#     [InlineKeyboardButton(text='◀️ Назад', callback_data='meetup-cancel')]
    
# ])

