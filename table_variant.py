"""
# CLC Table variant data class
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
# How it works:
    TODO: Explain
"""


class TableVariant(object):

    def __init__(self, **kwargs):
        self.variant_dict = kwargs

    def __getitem__(self, key):
        return self.variant_dict[key]

    def set_file_info(self, file_info):
        self.file_info = file_info
