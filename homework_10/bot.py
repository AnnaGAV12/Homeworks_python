import asyncio

from aiogram import Bot, Dispatcher, executor, filters, types
from pathlib import Path

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(filters.CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Доброго времени суток")
    await asyncio.sleep(1)
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()

    path = Path.home() /'Downloads' / 'orange.jpg'
    media.attach_photo(types.InputFile(path), 'orange!')

    media.attach_photo('http://lorempixel.com/400/200/cats/', 'Random cat.')

    await message.reply_media_group(media=media)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)