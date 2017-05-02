"""
# Arguments parser for the clc variants table formatter
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
# How it works:
    TODO: Explain
"""
# import os
import argparse


class VTableArgparser(object):
    def __init__(self, description):
        self.parser = argparse.ArgumentParser(description)

    def fill(self):
        self.parser.add_argument("-d", "--format_mode",
                                 action="store_true",
                                 help="Run formatter on a directory or file.")
        self.parser.add_argument("-i", "--input_file_or_directory",
                                 help="Specify input file or directory.")
        self.parser.add_argument("-o", "--output_file_or_directory",
                                 help="Specify output file or directory.")

        return self

    def parseAsVTableArgs(self):
        args = self.parser.parse_args()
        v_table_args = VTableArgs(args.format_mode,
                                  args.input_file_or_directory,
                                  args.output_file_or_directory)
        return v_table_args


class VTableArgs(object):

    def __init__(self,
                 format_mode,
                 input_file_or_directory,
                 output_file_or_directory):

        self.format_mode = format_mode
        self.input_file_or_directory = input_file_or_directory
        self.output_file_or_directory = output_file_or_directory
