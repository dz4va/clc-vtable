# CLC Table Formatting Functions
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_

# Coding Region Change Validation Exception


class ValidationException(Exception):
    def __init__(self, message, error_str):

        # Call the base class constructor with the message
        super(ValidationException, self).__init__(message)

        # Error String
        self.errors = error_str
        self.message = message
