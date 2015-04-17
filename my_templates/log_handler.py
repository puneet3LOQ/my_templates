import logging

# Create a logger
logger = logging.getLogger('log_handler')
logger.setLevel(logging.DEBUG)

# Filehandler for logging to a persistent source.
fh = logging.FileHandler('rest_api.log')
fh.setLevel(logging.INFO)

# Stream handler for logging to stdout
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Set formatting
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

# Test that the logger works.
# Calls are in order of ascending importance.
logger.debug('This is a debug log')
logger.info('Creating an instance of the log_handler.')
logger.warn('This is a warning log')
logger.error('This is an error log.')
logger.critical('This is a critical log. '\
                +'That usually means something has'\
                +' happened from which we could not recover')

