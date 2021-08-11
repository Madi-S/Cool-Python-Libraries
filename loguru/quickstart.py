from loguru import logger


logger.debug('No need for configuration, handlers etc. Ready to go.')

logger.info('Starting the application.')
logger.warning('Too many connections. Restarting the application.')
logger.critical('DDOS Attack. Shutting down the application.')
logger.error('Cannot start the application.')
