"""
# CLC Table variant data writer class for writing data in openpyxl given sheet
# row
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
# How it works:
    TODO: Explain
"""

import openpyxl as xl


class TableVariantWriter(object):
    """Writes table variant into the openpyxl sheet row

    Attributes:
        table_variant (TYPE): Description
    """

    def __init__(self, table_variant):
        """Summary

        Args:
            table_variant (TYPE): Description
        """
        self.table_variant = table_variant

    def write(self):
        """Summary

        Returns:
            TYPE: Description
        """
        pass
