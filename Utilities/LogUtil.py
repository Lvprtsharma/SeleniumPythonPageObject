import logging
import time

class Logger():

    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        curr_time = time.strftime(" %y-%m-%d ")
        self.LogFileName = '..\\Logs\\log' + curr_time + '.txt'

        fh = logging.FileHandler(self.LogFileName, mode="w")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
