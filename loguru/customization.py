from loguru import logger


new_logging_level = logger.level('START', no=12, color='<green>', icon='🐍')

logger.log('START', 'Application has been launched')
