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
from argparser import VTableArgparser
from table_variant import TableVariant
from table_variant_reader import TableVariantReader
from table_variant_writer import TableVariantWriter
# import pprint


def format_directory(input_directory, output_directory):
    print("Starting with directory...")
    print(input_directory)
    print(output_directory)
    # TODO: implement this after format_single_file because this will consist
    # mostly looping over the files and calling format single file, thus
    # format_single_file has to do most of the work maybe we could even run
    # concurrently. Let's see.


def format_single_file(input_file, output_file):
    print("Starting with single file...")
    print(input_file)
    print(output_file)
    # TODO: implement this first to have thread safe code only for concurrent
    # running superpowers then this should be called on all the files inside
    # the directory and a single file

    # input_workbook = xl.load_workbook("test_data/test.xlsx")
    # # output_workbook = xl.Workbook()

    # input_workbook_sheet = input_workbook.active
    # # input_workbook_row_data = {}

    # for row in range(2, input_workbook_sheet.max_row + 1):
    #     for col in range(1, input_workbook_sheet.max_column + 1):
    #         print(input_workbook_sheet.cell(row=row, column=col).value)


def main():

    # Get VTable args choose mode and run functions accordingly
    args = VTableArgparser("python3 clc_vtable.py").fill().parseAsVTableArgs()

    if (args.format_mode):
        # If input file or directory is a directory and output file or
        # directory is also a directory and they don't match run format
        # directory
        if args.directories_valid():
            format_directory(args.input_file_or_directory,
                             args.output_file_or_directory)
        else:
            print("Directory validations unsuccessful! Please try again.")
    else:
        # If the input file or directory is a file and output file or directory
        # is also a file and they don't match run format single file
        if args.files_valid():
            format_single_file(args.input_file_or_directory,
                               args.output_file_or_directory)
        else:
            print("File name validations unsuccessful! Please try again.")


if __name__ == "__main__":
    main()
