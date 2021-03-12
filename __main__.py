from vkbottle.bot import Bot, Message
from cfg import TOKEN
import logging

bot = Bot(TOKEN)

bot.labeler.vbml_ignore_case = True
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':

    #commands
    from commands import bot

    bot.run_forever()