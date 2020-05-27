import time


def success(sleep_time):
    time.sleep(sleep_time)


def failure(sleep_time):
    time.sleep(sleep_time)
    raise
