"""
# CLC Table Formatting Functions
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
"""

import openpyxl as xl
import typecheck as tc


class ExcelWriter(object):
    @tc.typecheck
    def __init__(self, output_file: str):
        self.output_file = output_file
        self.output_workbook = xl.Workbook()
        self.active_sheet = self.output_workbook.active

    @tc.typecheck
    def set_cell_value(self, row: int, column: int, value: str):
        self.active_sheet.cell(row=row, column=column).value = value

    @tc.typecheck
    def fill_row(self, row: int, data_columns: tc.list_of[str]):
        for column, col_str in enumerate(self.data_columns):
            self.set_cell_value(row, column, col_str)

    @tc.typecheck
    def write_header(self, header_columns: tc.list_of[str]):
        self.fill_row(1, header_columns)

    @tc.typecheck
    def write_data_row(self, data_columns: tc.list_of[str], row: int):
        self.fill_row(row, data_columns)

    def save(self):
        self.output_workbook.save(self.output_file)
