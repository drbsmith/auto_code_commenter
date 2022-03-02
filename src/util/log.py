"""! @file

# Log

Helper to setup logging, print to console/stream and fill a file in ./logs

## Classes
	* GMTFormatter

## Functions
	* setup_logging
@package src"""



import os
import time
import logging
import logging.config

## switch to True to disable debug prints
DEPLOYED = False

class GMTFormatter(logging.Formatter):
    converter = time.gmtime

def setup_logging(filename: str = 'auto_code_commenter'):
    lowest_level = 'DEBUG'
    if DEPLOYED:
        lowest_level = 'INFO'
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(asctime)s %(levelname)-8s %(message)s'
            },
            'detail': {
                'format': '%(asctime)s - [%(levelname)s] - File: %(filename)s - Func: %(funcName)s() - Line: %(lineno)d %(message)s',
                '()': GMTFormatter
            }
        },
        'handlers': {
            'stream': {
                'class': 'logging.StreamHandler',
                'level': lowest_level,
                'formatter': 'simple'
            },
            'file_handler': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'level': 'ERROR',
                'formatter': 'detail',
                'filename': '../logs/{}.log'.format(filename),
                'interval': 1,
                'when': 'midnight',
                'backupCount': 10,
                'utc': True,
                'encoding': 'utf8'
            },
            'debug_handler': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': lowest_level,
                'formatter': 'detail',
                'filename': '../logs/{}-{}.log'.format(filename, lowest_level),
                'maxBytes': 2097152,
                'backupCount': 10
            }
        },
        'root': {
            'handlers': ['stream', 'file_handler', 'debug_handler'],
            'level': lowest_level
        }
    })

    return logging.getLogger()