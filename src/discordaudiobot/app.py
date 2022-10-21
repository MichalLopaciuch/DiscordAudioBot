from os import getenv
from bot import bot
import logging


def main() -> None:
    handler = logging.FileHandler(filename='discord_bot.log', encoding='utf-8', mode='a')
    bot.run(getenv('BOT_TOKEN', None), log_handler=handler, log_level=logging.INFO)


if __name__ == '__main__':
    main()
