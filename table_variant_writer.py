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
from table_variant import TableVariant
from table_formatter import TableFormatter


class TableVariantWriter(ExcelWriter):
    def __init__(self, output_file):
        super(TableVariantWriter, self).__init__(output_file)

    def get_formatted(self, table_variant):
        variant = table_variant.get_as_dict()
        return TableFormatter.format(variant)
