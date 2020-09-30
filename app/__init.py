import logging
from os.path import dirname
from datetime import datetime

LOG_PATH=r'.\logs'
CURRENT_TIME = datetime.now()
LOG_FILE_NAME = f'{str(CURRENT_TIME.day).zfill(2)}-{str(CURRENT_TIME.month).zfill(2)}-{str(CURRENT_TIME.year).zfill(2)}-{str(CURRENT_TIME.minute).zfill(2)}-{str(CURRENT_TIME.second).zfill(2)}-{str(CURRENT_TIME.microsecond).zfill(2)}-{str(CURRENT_TIME.month).zfill(2)}'

logging.basicConfig(filename=rf'{dirname(dirname(__file__))}{LOG_PATH}\{LOG_FILE_NAME}.log', level=logging.INFO, format='%(levelname)s:%(asctime)s:File %(filename)s Module %(module)s line %(lineno)s => %(message)s')

logger = logging.getLogger('elior')
logger.setLevel(logging.WARNING)
formatter = logging.Formatter('%(levelname)s:%(asctime)s:File %(filename)s Module %(module)s line %(lineno)s => %(message)s')
file_handler = logging.FileHandler(rf'{dirname(dirname(__file__))}{LOG_PATH}\{LOG_FILE_NAME}.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)