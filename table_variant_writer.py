"""
# CLC Table variant data writer class for writing data in openpyxl given sheet
# row
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
# How it works:
    TODO: Explain
"""
import config as cfg
import openpyxl as xl
import typecheck as tc
from excel_writer import ExcelWriter
from table_variant import TableVariant
from variant_format import VariantFormat
from table_formatter import TableFormatter


class TableVariantWriter(ExcelWriter):
    @tc.typecheck
    def __init__(self, output_file: str):
        super(TableVariantWriter, self).__init__(output_file)

    @tc.typecheck
    def get_formatted(self, table_variant: TableVariant):
        variant = table_variant.get_as_dict()
        formatted = []
        # here we format it
        return formatted
