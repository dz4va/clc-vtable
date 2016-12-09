"""
# CLC Table Formatting Functions
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
"""
import unittest
from table_formatter import TableFormatter


class TestMethods(unittest.TestCase):

    def test_FormatVariant_snv(self):
        file_info = "FT_74_6955.xlsx row 25"
        variant_type = "SNV"
        reference = 'G'
        allele = 'A'
        coding_region_change = "YP_512841.1:c.150G>A"
        self.assert_equal(TableFormatter.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            coding_region_change), "G150A")

    def test_FormatVariant_snv_contains_illegal(self):
        file_info = "FT_74_6955.xlsx row 25"
        variant_type = "SNV"
        reference = 'G'
        allele = 'A'
        coding_region_change = "[1delA];YP_513094.1:c.[590_591delAA]"
        self.assert_equal(TableFormatter.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            coding_region_change),
            "G>A_error: YP_513095.1:c.[1delA];YP_513094.1:c.[590_591delAA]")

    def test_FormatVariant_insertion(self):
        file_info = "FT_74_6955.xlsx row 25"
        variant_type = "Insertion"
        reference = '-'
        allele = 'C'
        coding_region_change = "YP_512901.1:c.292_293insG"
        self.assert_equal(TableFormatter.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            coding_region_change), "Cins293")

    def test_FormatVariant_insertion_contains_illegal(self):
        file_info = "FT_74_6955.xlsx row 25"
        variant_type = "Insertion"
        reference = '-'
        allele = 'C'
        coding_region_change = "[1delA];YP_513094.1:c.[590_591delAA]"
        self.assert_equal(TableFormatter.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            coding_region_change),
            "Cins_error: YP_513095.1:c.[1delA];YP_513094.1:c.[590_591delAA]")

    def test_FormatVariant_deletion(self):
        file_info = "FT_74_6955.xlsx row 25"
        variant_type = "Deletion"
        reference = 'A'
        allele = '-'
        coding_region_change = "YP_513007.1:c.907delA"
        self.assert_equal(TableFormatter.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            coding_region_change), "Adel907")

    def test_FormatVariant_deletion_contains_illegal(self):
        file_info = "FT_74_6955.xlsx row 25"
        variant_type = "Deletion"
        reference = 'A'
        allele = '-'
        coding_region_change = "[1delA];YP_513094.1:c.[590_591delAA]"
        self.assert_equal(TableFormatter.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            coding_region_change),
            "Adel_error: YP_513095.1:c.[1delA];YP_513094.1:c.[590_591delAA]")

    def test_FormatVariant_unknown(self):
        file_info = "-"
        variant_type = "unknown"
        reference = '-'
        allele = '-'
        coding_region_change = "-"
        self.assert_equal(TableFormatter.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            coding_region_change), "")

    def test_ContainsIllegal(self):
        coding_region_change = "YP_513007.1:c.907delA"
        self.assert_equal(TableFormatter.ContainsIllegal(
            coding_region_change, ['[', ';']), False)

    def test_ContainsIllegal_contains(self):
        coding_region_change = "[1delA];YP_513094.1:c.[590_591delAA]"
        self.assert_equal(TableFormatter.ContainsIllegal(
            coding_region_change, ['[', ';']), True)

    def test_GetIntFromString(self):
        val = "Abgdfsb dasdasdw adsad dasd78dasdsd"
        self.assert_equal(TableFormatter.GetIntFromString(
            val), "78")

    def test_GetIntFromString_doesntcontain(self):
        val = "dasdasdadsdsdad dasdasdas das dsada"
        self.assert_equal(TableFormatter.GetIntFromString(
            val), "")

    def test_CodonPos_three(self):
        val = "A288C"
        self.assert_equal(TableFormatter.CodonPos(
            val), "3")

    def test_CodonPos_two(self):
        val = "A287C"
        self.assert_equal(TableFormatter.CodonPos(
            val), "2")

    def test_CodonPos_one(self):
        val = "A286C"
        self.assert_equal(TableFormatter.CodonPos(
            val), "1")

    def test_CodonPos_none(self):
        val = "A>C"
        self.assert_equal(TableFormatter.CodonPos(
            val), "")


if __name__ == "__main__":
    unittest.main()
