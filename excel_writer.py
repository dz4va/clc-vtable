"""
# CLC Table Formatting Functions
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
"""

import openpyxl as xl

class ExcelWriter(object):
    def __init__(self, output_file):
        self.output_file = output_file
        self.output_workbook = xl.Workbook()
        self.active_sheet = self.output_workbook.active

    def set_cell_value(self, row, column, value):
        self.active_sheet.cell(row=row, column=column).value = value

    def fill_row(self, row, data_columns):
        for column, col_str in enumerate(data_columns):
            self.set_cell_value(row, column + 1, data_columns[col_str])

    def write_header(self, header_columns):
        for column, value in enumerate(header_columns):
            self.set_cell_value(1, column + 1, value)

    def write_data_row(self, data_columns, row):
        self.fill_row(row, data_columns)

    def save(self):
        self.output_workbook.save(self.output_file)
