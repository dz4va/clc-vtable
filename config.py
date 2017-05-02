# from collections import OrderedDict

SNP = "SNV"
INSERTION = "Insertion"
DELETION = "Deletion"

# Original header names
V_REFPOS = "Reference Position"
V_TYPE = "Variant"
V_LENGTH = "Length"
V_REF = "Reference"
V_ALLELE = "Allele"
V_LINKAGE = "Linkage"
V_ZYGOSITY = "Zygosity"
V_ALCOUNT = "Allele Count"
V_COV = "Coverage"
V_FREQ = "Frequency"
V_FR_BAL = "Forward Reverse Balance"
V_AVG_QUAL = "Average Quality"
V_ANOT = "Overlapping Annotation"
V_CRC = "Coding Region Change"
V_AAC = "Amino Acid Change"

# Desired columns in the final output
F_LOCATION = "Location"
F_VARIANT = "Variant"
F_CODONPOS = "Codon Position"
F_AAC = "Amino Acid Change"
F_OA = "Overlapping Annotation"
F_FREQ = "Frequency"

FINAL_COLUMNS = [
    F_LOCATION,
    F_VARIANT,
    F_CODONPOS,
    F_AAC,
    F_OA,
    F_FREQ
]
