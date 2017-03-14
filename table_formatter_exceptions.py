# CLC Table Formatting Functions
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_

# Coding Region Change Validation Exception


class ValidationException(Exception):
    def __init__(self, message, error_str):
        super(ValidationException, self).__init__(message)

        self.errors = error_str
        self.message = message
