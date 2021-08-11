from loguru import logger


logger.add('exceptions.log', backtrace=True, diagnose=True)


try:
    5 / 0
except:
    logger.exception('Execution failed')


@logger.catch
def do_crazy_stuff():
    return 'Hello W' + 0 + 'rld'


@logger.catch
def do_bizarre_stuff():
    return logger.do_bizarre_stuff()


if __name__ == '__main__':
    do_crazy_stuff()
    do_bizarre_stuff()
