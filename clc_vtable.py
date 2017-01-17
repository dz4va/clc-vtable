"""
# CLC Table variant data reader class uses given openpyxl
# sheet row to read data and return TableVariant object
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
# How it works:
    TODO: Explain
"""
# Add openpyxl and make table formatter work with one file
# storing everything in one new excel file created in the output directory
# then implement iterating over the files contained in a given input
# directory and formatting, saving them in output directory

import openpyxl as xl
from table_variant import TableVariant
# import pprint

print("Opening WorkBook...")

input_workbook = xl.load_workbook("test_data/test.xlsx")
output_workbook = xl.Workbook()

input_workbook_sheet = input_workbook.active
input_workbook_row_data = {}

for row in range(2, input_workbook_sheet.max_row + 1):
    for col in range(1, input_workbook_sheet.max_column + 1):
        print(input_workbook_sheet.cell(row=row, column=col).value)
