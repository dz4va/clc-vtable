from collections import OrderedDict

SNP = "SNV"
INSERTION = "Insertion"
DELETION = "Deletion"

V_REFPOS = "reference_position"
V_TYPE = "variant_type"
V_LENGTH = "length"
V_REF = "reference"
V_ALLELE = "allele"
V_LINKAGE = "linkage"
V_ZYGOSITY = "zygosity"
V_ALCOUNT = "allele_count"
V_COV = "coverage"
V_FREQ = "frequency"
V_FR_BAL = "forward_reverse_balance"
V_AVG_QUAL = "average_quality"
V_ANOT = "overlapping_annotations"
V_CRC = "coding_region_change"
V_AAC = "amino_acid_change"

columns_to_write = OrderedDict()

columns_to_write[V_REFPOS] = True
columns_to_write[V_REFPOS] = True
columns_to_write[V_TYPE] = True
columns_to_write[V_LENGTH] = True
columns_to_write[V_REF] = True
columns_to_write[V_ALLELE] = True
columns_to_write[V_LINKAGE] = True
columns_to_write[V_ZYGOSITY] = True
columns_to_write[V_ALCOUNT] = True
columns_to_write[V_COV] = True
columns_to_write[V_FREQ] = True
columns_to_write[V_FR_BAL] = True
columns_to_write[V_AVG_QUAL] = True
columns_to_write[V_ANOT] = True
columns_to_write[V_CRC] = True
columns_to_write[V_AAC] = True
