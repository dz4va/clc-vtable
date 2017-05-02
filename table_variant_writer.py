"""
# CLC Table variant data writer class for writing data in openpyxl given sheet
# row
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
# How it works:
    TODO: Explain
"""
from excel_writer import ExcelWriter

class TableVariantWriter(ExcelWriter):
    def __init__(self, output_file):
        super(TableVariantWriter, self).__init__(output_file)
