import datetime


class Logger:
    @staticmethod
    def log(msg: str | list) -> None:
        if type(msg) != list:
            print(f'{datetime.datetime.now()}', msg)
        else:
            print(f'{datetime.datetime.now()}', *msg)
