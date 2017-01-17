"""
# CLC Table variant data class
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
# How it works:
    TODO: Explain
"""


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
        self.reference_position = kwargs["reference_position"]
        self.variant_type = kwargs["variant_type"]
        self.length = kwargs["length"]
        self.reference = kwargs["reference"]
        self.allele = kwargs["allele"]
        self.linkage = kwargs["linkage"]
        self.zygosity = kwargs["zygosity"]
        self.allele_count = kwargs["allele_count"]
        self.coverage = kwargs["coverage"]
        self.frequency = kwargs["frequency"]
        self.forward_reverse_balance = kwargs["forward_reverse_balance"]
        self.average_quality = kwargs["average_quality"]
        self.overlapping_annotations = kwargs["overlapping_annotations"]
        self.coding_region_change = kwargs["coding_region_change"]
        self.amino_acid_change = kwargs["amino_acid_change"]
