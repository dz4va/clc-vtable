"""
# CLC variants table formatter contains main that should be run.
# Inludes two modes. Formatting for single file and formatting on a directory.
# Help: python3 clc_vtable.py -h
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
import os
import errno
# import _thread
import config as cfg
import openpyxl as xl
from argparser import VTableArgparser
from table_variant import TableVariant
from table_variant_reader import TableVariantReader
from table_variant_writer import TableVariantWriter
from table_formatter import TableFormatter


def format_directory(input_dir, output_dir):
    print("\nDirectory Validations Successful!")
    print("Starting directory formatting. At: " + input_dir +
          " Outputting to: " + output_dir)

    for input_file in os.listdir(input_dir):
        if input_file[0] != '.' and input_file.endswith(".xlsx"):
            # TODO: implement multithreading for many xlsx files
            # not working threaded version might try threading module instead
            # making thread class for single file formatter
            # try:
            #     _thread.start_new_thread(format_single_file, (
            #         os.path.abspath(input_file),
            #         os.path.abspath(os.path.join(output_dir, input_file))
            #     ))
            # except:
            #     print("Error: Unable to start thread.")
            format_single_file(
                os.path.abspath(os.path.join(input_dir, input_file)),
                os.path.abspath(os.path.join(output_dir, input_file)))


def format_single_file(input_file, output_file):
    print("\nFormatting file: " + input_file +
          "\nSave file: " + output_file)

    # Create variant reader and input_workbook
    variant_reader = TableVariantReader(input_file)

    # Create variant writer and output_workbook
    variant_writer = TableVariantWriter(output_file)

    variant_writer.write_header(cfg.FINAL_COLUMNS)

    for row in range(2, variant_reader.active_sheet.max_row + 1):
        # Read
        table_variant = variant_reader.read_variant(row)
        # Set file info
        table_variant.set_file_info(output_file + " [ row " + str(row) + " ]")
        # Format
        formatted_variant = TableFormatter.format(table_variant)
        # Write
        variant_writer.write_data_row(formatted_variant, row)

    # Save output file
    variant_writer.save()


def main():

    # Get VTable args choose mode and run functions accordingly
    args = VTableArgparser("python3 clc_vtable.py").fill().parseAsVTableArgs()

    if args.format_mode:
        input_dir = args.input_file_or_directory
        output_dir = args.output_file_or_directory

        print("Table formatter started in directory formatting mode with:\n" +
              "Input Directory \n\t- " + input_dir +
              "\nOutput Directory \n\t- " + output_dir + "\n")

        if os.path.isdir(input_dir):
            if input_dir != output_dir:
                try:
                    os.mkdir(output_dir)
                    print("Output directory created. At: " + output_dir)
                except OSError as e:
                    if e.errno == errno.EEXIST:
                        print("Output directory already exists. At: " +
                              output_dir)
                finally:
                    if len(os.listdir(output_dir)) == 0:
                        # print("Output directory is empty.")
                        format_directory(input_dir, output_dir)
                    else:
                        print("Ouptut directory is not empty." +
                              " Please, try again")
            else:
                print("Output and input directories can't be equal")
        else:
            print("Given input directory is incorrect. Please, try again.")
    else:
        input_file = args.input_file_or_directory
        output_file = args.output_file_or_directory
        format_single_file(input_file, output_file)


if __name__ == "__main__":
    main()
