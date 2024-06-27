import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from users.usersHandlers import router
from database.models import async_main

async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

async def on_startup(dispatcher):
    await async_main()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try: 
        asyncio.run(main())
    except KeyboardInterrupt: 
        print('done')


