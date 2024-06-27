import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile, web_app_data
from aiogram.enums import ChatAction
import users.usersKeyboards as start_kb
from database.requests import set_user

router = Router()

PHOTO_PATH = './pics2send/logo.jpg'
PHOTO = FSInputFile(PHOTO_PATH)

@router.message(CommandStart())
async def start(message: Message):
    await set_user(message.from_user.id)
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.TYPING)
    await asyncio.sleep(0.89)
    
    await message.answer(text=f'Привет, {message.from_user.first_name}!', reply_markup=start_kb.start_InlineKeyboard)

    # await message.answer_photo(PHOTO, caption=f'⚡️ Привет, {message.from_user.first_name}!\n\nЗдесь собрана важнейшая информация о нашем мероприятии', 
    #                            reply_markup=start_kb.start_InlineKeyboard)


@router.message(F.web_app_data)
async def web_app_data_handler(message: Message):
    data = message.web_app_data.data  # Данные, переданные из WebApp
    user_id = message.from_user.id

    if data == 'allow_messages':
        # Если пользователь разрешает отправку сообщений, создаем чат с ботом
        await message.bot.send_message(user_id, "Спасибо за разрешение! Теперь вы будете получать сообщения от бота.")
    else:
        await message.bot.send_message(user_id, "Вы отказались от получения сообщений.")

# @router.callback_query(F.data.in_({'FAQ', 'gala-dinner', 'meetup'}))
# async def handle_section(callback: CallbackQuery):
#     section_captions = {
#         'FAQ': '⚡️FAQ Section',
#         'gala-dinner': '⚡️Gala Dinner Section',
#         'meetup': '⚡️Meetup Section'
#     }
#     section_reply_keyboards = {
#         'FAQ': start_kb.faq_InlineKeyboard,
#         'gala-dinner': start_kb.gala_dinner_InlineKeyboard,
#         'meetup': start_kb.meetup_InlineKeyboard
#     }
#     await callback.answer('Выбери интересующий тебя раздел')
#     await callback.message.edit_caption(caption=section_captions[callback.data], reply_markup=section_reply_keyboards[callback.data])


# @router.callback_query(F.data.in_({'faq-cancel', 'gala-dinner-cancel', 'meetup-cancel'}))
# async def cancel(callback: CallbackQuery):
#     await callback.answer('Выбери интересующий тебя раздел')
#     await callback.message.edit_caption(caption=f'⚡️ Привет, {callback.message.from_user.first_name}!\n\nЗдесь собрана важнейшая информация о нашем мероприятии', 
#                                         reply_markup=start_kb.start_InlineKeyboard)
