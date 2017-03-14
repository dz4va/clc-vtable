# CLC Table Formatting Functions
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_

import logging as log

FILE_WARNING = "warnings.log"


class Logger(object):
    @staticmethod
    def Warn(warning_message):
        log.basicConfig(filename=FILE_WARNING, level=log.WARNING)
        log.warning(warning_message)
