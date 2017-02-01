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
from table_variant import TableVariant


class TableVariantWriter(object):
    @tc.typecheck
    def __init__(self, output_file: str):
        self.output_file = output_file
        self.output_workbook = xl.Workbook()
        self.active_sheet = self.output_workbook.active

    @tc.typecheck
    def set_cell_value(self, row: int, column: int, value: str):
        self.active_sheet.cell(row=row, column=column).value = value

    def strify(self, value):
        if isinstance(value, float):
            return str(round(value, 2))
        elif value is None:
            return ""
        return str(value)

    def write_header(self):
        column = 1
        for key, must_write in cfg.columns_to_write.items():
            if must_write:
                self.set_cell_value(1, column, key)
                column += 1

    @tc.typecheck
    def write(self, table_variant: TableVariant, row: int):
        column = 1
        variant_dict = table_variant.toDict()
        for key, must_write in cfg.columns_to_write.items():
            if must_write:
                self.set_cell_value(
                    row, column, self.strify(variant_dict[key]))
                column += 1

    def save(self):
        self.output_workbook.save(self.output_file)
