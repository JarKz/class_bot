from __main__ import bot
from vkbottle.bot import Message, rules
from database import show_dz, show_dz_day_filtred, show_dz_day, show_dz_filtred, new_dz_empty
from database.intital import initialise
from .keyboards import PREDMETS
from database import items


# Основной билдинг бд
@bot.on.message(text='/инициализация')
async def initial(message: Message):
    initialise()
    await message.answer('Инизиализация завершена!')

# Операции связанные с д/з
# Вывод всех д/з
@bot.on.message(text='/дз')
async def DomZad(message: Message):
    await message.answer('Вот домашние задания:')
    return show_dz()

# Вывод д/з по опред. предмету
@bot.on.message(text='/дз по <item>')
async def DomZadOneItem(message: Message, item):
    await message.answer(show_dz_filtred(item))

# Запись д/з в бд
@bot.on.message(text="/запись в дневник <item>")
async def Zapic(message: Message, item):
    new_dz_empty(item)
    await message.answer("Выберите предмет, в который хотите записать дом. задание:",
    keyboard=PREDMETS)
    
# Вывод всех д/з на определённый день (или завтра)
@bot.on.message(text='/дз на <item>')
async def DomZadOneDay(message: Message, item):
    if item == 'завтра':
        return show_dz_day()
    else:
        return show_dz_day_filtred(item)

# Операции связанные с объявлениями
# @bot.on.message(text='/объявления')
# async def Obyavlenia(message: Message):
#     await message.answer("Объявления на данный момент времени:")

# @bot.on.message(text='/запись в объявление')
# async def ZapicObyav(message: Message):
#     await message.answer('Объявление записано!')

# Помощь новичку
@bot.on.message(text='/помощь')
async def help(message: Message):
    return f'''❗Команды❗
    
    ❗ /дз - отображает все д/з.

    ❗ /дз на (какой-то день или завтра) - отображает д/з на определённый день или завтра. На определённый день пишется по правилам русского языка (например: /дз на среду)

    ❗ /дз по (определённый предмет) - отображает д/з по определённому предмету (нужно учитывать правила, ибо не будет реагировать).

    ❗ /правила - отображает правильность написания предметов. Учитывайте, всё пишется слитно!

    ❗ /запись в дневник (само д/з) - записывает д/з в "виртуальный дневник", после ввода указывать предмет. (Работает только на телефонах❗❗❗)
    
    '''

# Правила правописания школьн. предметов
@bot.on.message(text='/правила')
async def regulations(message: Message):
    string = ''
    a = 1
    for i in items:
        string += f'{a}. {i}\n'
        a+=1
    return string

# Команда реагирующая на всё, что не является командой
@bot.on.message()
async def AllMessages(message: Message):
    return '❗ Команда не опознана! Введите "/помощь", чтобы получить подробную информацию!❗'