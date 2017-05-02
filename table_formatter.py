"""
# CLC Table Formatting Functions
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
# How it works:
    TODO: Explain
"""
import config as cfg
from collections import OrderedDict
from variant_format import VariantFormat


class TableFormatter(object):

    @staticmethod
    def format(table_variant):
        formatted = OrderedDict()

        formatted[cfg.F_LOCATION] = table_variant[cfg.V_REFPOS]

        formatted[cfg.F_VARIANT] = VariantFormat.FormatVariant(
            table_variant.file_info,
            table_variant[cfg.V_TYPE],
            table_variant[cfg.V_REF],
            table_variant[cfg.V_ALLELE],
            table_variant[cfg.V_CRC]
        )

        formatted[cfg.F_CODONPOS] = VariantFormat.CodonPos(
            formatted[cfg.F_VARIANT]
        )

        formatted[cfg.F_AAC] = "" # TODO: first change the AminoAcidChange()

        formatted[cfg.F_OA] = table_variant[cfg.V_ANOT]

        formatted[cfg.F_FREQ] = table_variant[cfg.V_FREQ]

        return formatted
