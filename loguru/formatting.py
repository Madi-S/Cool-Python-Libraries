import sys
from loguru import logger


logger.add(
    sys.stderr,
    format='<green>{time:YYYY-MM-DD at HH:mm:ss}</green> | <red>{level}</red> | <blue>{message}</blue>',
    level='WARNING',    # Min logging level
    colorize=True,      # Make logs colorful
    # enqueue=True,       # Make logging compatible with async
    # serialize=True,     # Convert logs to JSON
)
logger.add('app.log', rotation='500 MB',
           retention='10 days', compression='zip')

logger.warning('If you\'re using Python {}, prefer {feature} of course!',
               3.5, feature='f-strings')
logger.debug('I am not correctly formatted!')

'''
More configuration settings

logger.add('file_1.log', rotation='500 MB')    # Automatically rotate too big file

logger.add('file_2.log', rotation='12:00')     # New file is created each day at noon

logger.add('file_3.log', rotation='1 week')    # Once the file is too old, it's rotated

logger.add('file_X.log', retention='10 days')  # Cleanup after some time

logger.add('file_Y.log', compression='zip')    # Save some loved space

'''
