import logging
import sys


def log_maker():
    """
    Construct a logger formatted similarly to gunicorn's defaults
    :return: a configured Logger object
    """
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s',
        '%Y-%m-%d %H:%M:%S %z')
    ch.setFormatter(formatter)
    log.addHandler(ch)
    return log
