import requests
from aiogram import Bot, Dispatcher, executor, types
import asyncio

API_TOKEN = "6374052666:AAHdHy9f3sopRjabnSqFXqioXW5NMwW6S9o"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


count = 0

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    while (count > 3):
        count = count + 1
        # Send your desired message here
        message = "This is a looped message!"

        # Send the message using the bot
        await message.answer(message.chat.id, message)

        # Delay for a certain amount of time before sending the next message
        await asyncio.sleep(1)  # Delay for 1 hour (3600 seconds)


@dp.message_handler(commands=['logo'])
async def logo(message: types.Message):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    if response.status_code == 200:
        data = response.json()
        image_url = data['message']
        await message.answer_photo(image_url)
    else:
        await message.reply("Failed to fetch a random image.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
