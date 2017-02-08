"""
# CLC Table variant data class
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
# How it works:
    TODO: Explain
"""
import config as cfg
from collections import OrderedDict


class TableVariant(object):
    """Table variant data class for holding each row of the clc variants table

    Attributes:
        allele (str): Description
        allele_count (str): Description
        amino_acid_change (str): Description
        average_quality (str): Description
        coding_region_change (str): Description
        coverage (str): Description
        forward_reverse_balance (str): Description
        frequency (str): Description
        length (str): Length of the variant
        linkage (str): Description
        overlapping_annotations (str): Description
        reference (str): Pattern in reference
        reference_position (str): Position in the reference
        variant_type (str): SNV, Deletion, Insertion
        zygosity (str): Description
    """

    def __init__(self, **kwargs):
        """Initializes this class giving all the information that is required

        Args:
            **kwargs (dict): Dictionary of the keyword arguments
        """
        self.reference_position = kwargs[cfg.V_REFPOS]
        self.variant_type = kwargs[cfg.V_TYPE]
        self.length = kwargs[cfg.V_LENGTH]
        self.reference = kwargs[cfg.V_REF]
        self.allele = kwargs[cfg.V_ALLELE]
        self.linkage = kwargs[cfg.V_LINKAGE]
        self.zygosity = kwargs[cfg.V_ZYGOSITY]
        self.allele_count = kwargs[cfg.V_ALCOUNT]
        self.coverage = kwargs[cfg.V_COV]
        self.frequency = kwargs[cfg.V_FREQ]
        self.forward_reverse_balance = kwargs[cfg.V_FR_BAL]
        self.average_quality = kwargs[cfg.V_AVG_QUAL]
        self.overlapping_annotations = kwargs[cfg.V_ANOT]
        self.coding_region_change = kwargs[cfg.V_CRC]
        self.amino_acid_change = kwargs[cfg.V_AAC]

    def get_as_dict(self):
        variant_dict = OrderedDict()

        variant_dict[cfg.V_REFPOS] = self.reference_position
        variant_dict[cfg.V_TYPE] = self.variant_type
        # variant_dict[cfg.V_LENGTH] = self.length
        variant_dict[cfg.V_REF] = self.reference
        variant_dict[cfg.V_ALLELE] = self.allele
        # variant_dict[cfg.V_LINKAGE] = self.linkage
        # variant_dict[cfg.V_ZYGOSITY] = self.zygosity
        # variant_dict[cfg.V_ALCOUNT] = self.allele_count
        # variant_dict[cfg.V_COV] = self.coverage
        variant_dict[cfg.V_FREQ] = self.frequency
        # variant_dict[cfg.V_FR_BAL] = self.forward_reverse_balance
        # variant_dict[cfg.V_AVG_QUAL] = self.average_quality
        variant_dict[cfg.V_ANOT] = self.overlapping_annotations
        variant_dict[cfg.V_CRC] = self.coding_region_change
        variant_dict[cfg.V_AAC] = self.amino_acid_change

        return variant_dict
