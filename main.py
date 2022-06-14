from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text

API_TOKEN = '5312790302:AAHBFbKkD5zsmYmNkouupWqkAgUTbQ3vrGw'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

p.message_handler(commands=['start'])
async def start
(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Geo-manzil",request_location=True)
    button2 = KeyboardButton("Telefon raqam",request_contact=True)
    button3 = KeyboardButton("Test tuzish",request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ))
    button4 = KeyboardButton("Botton4")
    button5 = KeyboardButton("Botton5")
    button6= KeyboardButton("Botton6")
    button7 = KeyboardButton("Botton7")

    # keyboard.add(button1).add(button4)#add yngi qatorga tugma qoshish
    # keyboard.add(button2)
    # keyboard.add(button3)
   _mark keyboard.row(button1, button2, button3)  # row bu bir qatorga tugmalarni terish
    keyboard.insert(button4).insert(button5)  # insert bu uchtadan kop tugmani yngi qatorga tushiradi
    await message.answer("Tugmalar", reply_markup=keyboard)

@dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Birinchi ovqatlar")
    button2 = KeyboardButton("Ikkinchi ovqatlar")

    keyboard.row(button1, button2, )  # row bu bir qatorga tugmalarni terish
    await message.answer("Taomnoma", replyup=keyboard)


@dp.message_handler(Text(equals="Birinchi ovqatlar"))
async def birinchi(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("shorva")
    button2 = KeyboardButton("mastava")

    keyboard.insert(button1)
    keyboard.insert(button2)

    await message.answer("brinchi ovqatlar roehati", reply_markup=keyboard)


@dp.message_handler(Text(equals="Ikkinchi ovqatlar"))
async def ikkinchi(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button3 = KeyboardButton("osh")
    button4 = KeyboardButton("shashlik")
    keyboard.insert(button3)
    keyboard.insert(button4)

    await message.answer("Ikkinchi ovqatlar roehati", reply_markup=keyboard)



@dp.message_handler(commands=['yordam'])
async def help(message: types.Message):
    await message.reply("Bu bot qandaedir ish bajaradi")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("bundae buruqni tushunmaeman")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
