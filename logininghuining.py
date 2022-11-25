import logging

'''
logging.basicConfig(level=logging.DEBUG)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
logging.debug('debug2')
logging.info('info2')
'''

'''
logging.basicConfig(level = logging.DEBUG,
                    filename='logs.log',
                    filemode='w',
                    format='We have next logging message:'
                    '%(asctime)s:%(levelname)s - %(message)s'
                    )

try:
    print(10 / 0)
except Exception:
    logging.exception("Exception")


c = 2 + 2
print(c == 5)

assert 2 + 2 == 5, "vy debil"
'''

"""
>>> 2 + 2
5
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()