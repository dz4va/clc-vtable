"""
# Arguments parser for the clc variants table formatter
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
# How it works:
    TODO: Explain
"""
import os
import argparse


class VTableArgparser(object):
    """VTable args parser initializes argparse library's ArgumentParser with
    given description then you should call fill() on a returned newly created
    object to fill it with the desired arguments and then as it returns the
    self you can also call parseAsVTableArgs to return an object of VTableArgs
    for ease of use and known fields.

    Attributes:
        parser (ArgumentParser): Parser that is used for parsing of arguments
    """

    def __init__(self, description):
        self.parser = argparse.ArgumentParser(description)

    def fill(self):
        """Adds arguments for the parser. There are two modes for the argsparser
        and the formatter to work. If the -d directory mode argument is false
        then the program runs on a single file. If the argument for directory
        formatting is true then the program runs on a directory containing xlsx
        files. Input file or directory depends on the mode if the program is
        run with single file mode then the -i argument should contain a single
        xlsx file to be formatted and the -o output arguement should also
        contain a single output xlsx file that will be used for writing output.
        If the multiple i.e directory mode is selected then the -i argument
        should contain name of the input directory to grab xlsx files from
        and -o output argument should contain an output directory where the
        files will be written with the same names as they had previously.

        Note* - please don't use same name for files and for directory

        Returns:
            None: None
        """
        # Run Formatter On A Directory
        self.parser.add_argument("-d", "--format_mode",
                                 action="store_true",
                                 help="Run formatter on a directory or file.")
        # Input File Argument Depends on Mode
        self.parser.add_argument("-i", "--input_file_or_directory",
                                 help="Specify input file or directory.")
        # Output File Argument Depends on Mode
        self.parser.add_argument("-o", "--output_file_or_directory",
                                 help="Specify output file or directory.")

        return self

    def parseAsVTableArgs(self):
        # TODO: change this to return VTableArgs
        args = self.parser.parse_args()
        v_table_args = VTableArgs(args.format_mode,
                                  args.input_file_or_directory,
                                  args.output_file_or_directory)
        return v_table_args


class VTableArgs(object):
    """Contains args of the clc_vtable

    Attributes:
        format_mode (bool): Format mode true for directory, false for file
        input_file_or_directory (str): Input file or directory path
        output_file_or_directory (TYPE): Output fila or directory path
    """

    def __init__(self, format_mode,
                 input_file_or_directory,
                 output_file_or_directory):
        """Initialize Table Args class with format mode input_file_or_directory
        and output_file_or_directory

        Args:
            format_mode (TYPE): Description
            input_file_or_directory (TYPE): Description
            output_file_or_directory (TYPE): Description
        """
        self.format_mode = format_mode
        self.input_file_or_directory = input_file_or_directory
        self.output_file_or_directory = output_file_or_directory
