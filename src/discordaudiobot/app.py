from bot import bot
from os import getenv


def main() -> None:
    bot.run(getenv('BOT_TOKEN', None))


if __name__ == '__main__':
    main()
