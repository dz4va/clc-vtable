# CLC Table Formatting Functions
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_

import logging as log

FILE_WARNING = "warnings.log"
FILE_ERROR = "errors.log"


class Logger(object):
    @staticmethod
    def Warn(warning_message):
        """Log the warning message to the log file

        Args:
            warning_message (string): Warning Message to be written

        Returns:
            None: None
        """
        log.basicConfig(filename=FILE_WARNING, level=log.WARNING)
        log.warning(warning_message)

    # @staticmethod
    # def Error(error_message):
    #     """Log the error message to the log file

    #     Args:
    #         error_message (string): Error Message to be written

    #     Returns:
    #         None: None
    #     """
    #     log.basicConfig(filename=FILE_ERROR, level=log.ERROR)
    #     log.error(error_message)
