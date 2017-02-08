"""
# CLC Table Formatting Functions
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
"""
import unittest
from variant_format import VariantFormat
from table_formatter_exceptions import ValidationException
from clc_vtable import *
from argparser import *
from table_variant import *
from table_variant_reader import *
from table_variant_writer import *


class TestMethods(unittest.TestCase):
    # VariantFormat Tests
    def test_FormatVariant_snv(self):
        file_info = "sample_data.xlsx row 25"
        variant_type = "SNV"
        reference = 'G'
        allele = 'A'
        crc = "YP_512841.1:c.150G>A"
        self.assertEqual(VariantFormat.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            crc), "G150A")

    def test_FormatVariant_snv_nocrc(self):
        file_info = "sample_data.xlsx row 25"
        variant_type = "SNV"
        reference = 'G'
        allele = 'A'
        crc = ''
        self.assertEqual(VariantFormat.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            crc), "G>A")

    def test_FormatVariant_snv_contains_illegal(self):
        file_info = "sample_data.xlsx row 25"
        variant_type = "SNV"
        reference = 'G'
        allele = 'A'
        crc = "YP_513095.1:c.[1delA];YP_513094.1:c.[590_591delAA]"
        self.assertEqual(VariantFormat.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            crc),
            "G>A_error: YP_513095.1:c.[1delA];YP_513094.1:c.[590_591delAA]")

    def test_FormatVariant_insertion(self):
        file_info = "sample_data.xlsx row 25"
        variant_type = "Insertion"
        reference = '-'
        allele = 'C'
        crc = "YP_512901.1:c.292_293insG"
        self.assertEqual(VariantFormat.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            crc), "Cins293")

    def test_FormatVariant_insertion_contains_illegal(self):
        file_info = "sample_data.xlsx row 25"
        variant_type = "Insertion"
        reference = '-'
        allele = 'C'
        crc = "YP_513095.1:c.[1delA];YP_513094.1:c.[590_591delAA]"
        self.assertEqual(VariantFormat.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            crc),
            "Cins_error: YP_513095.1:c.[1delA];YP_513094.1:c.[590_591delAA]")

    def test_FormatVariant_deletion(self):
        file_info = "sample_data.xlsx row 25"
        variant_type = "Deletion"
        reference = 'A'
        allele = '-'
        crc = "YP_513007.1:c.907delA"
        self.assertEqual(VariantFormat.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            crc), "Adel907")

    def test_FormatVariant_deletion_contains_illegal(self):
        file_info = "sample_data.xlsx row 25"
        variant_type = "Deletion"
        reference = 'A'
        allele = '-'
        crc = "YP_513095.1:c.[1delA];YP_513094.1:c.[590_591delAA]"
        self.assertEqual(VariantFormat.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            crc),
            "Adel_error: YP_513095.1:c.[1delA];YP_513094.1:c.[590_591delAA]")

    def test_FormatVariant_unknown(self):
        file_info = "-"
        variant_type = "unknown"
        reference = '-'
        allele = '-'
        crc = "-"
        self.assertEqual(VariantFormat.FormatVariant(
            file_info,
            variant_type,
            reference,
            allele,
            crc), "")

    def test_ContainsIllegal(self):
        crc = "YP_513007.1:c.907delA"
        self.assertEqual(VariantFormat.ContainsIllegal(
            crc, ['[', ';']), False)

    def test_ContainsIllegal_contains(self):
        crc = "YP_513095.1:c.[1delA];YP_513094.1:c.[590_591delAA]"
        self.assertEqual(VariantFormat.ContainsIllegal(
            crc, ['[', ';']), True)

    def test_GetIntFromString(self):
        val = "Abgdfsb dasdasdw adsad dasd78dasdsd"
        self.assertEqual(VariantFormat.GetIntFromString(val), "78")

    def test_GetIntFromString_doesntcontain(self):
        val = "dasdasdadsdsdad dasdasdas das dsada"
        self.assertEqual(VariantFormat.GetIntFromString(val), "")

    def test_CodonPos_three(self):
        val = "A288C"
        self.assertEqual(VariantFormat.CodonPos(val), "3")

    def test_CodonPos_two(self):
        val = "A287C"
        self.assertEqual(VariantFormat.CodonPos(val), "2")

    def test_CodonPos_one(self):
        val = "A286C"
        self.assertEqual(VariantFormat.CodonPos(val), "1")

    def test_CodonPos_none(self):
        val = "A>C"
        self.assertEqual(VariantFormat.CodonPos(val), "")

    def test_AminoAcidChange_contains(self):
        aac = "YP_512823.1:p.Ser35Tyr"
        self.assertEqual(VariantFormat.AminoAcidChange(aac), "Ser35Tyr")

    def test_AminoAcidChange_doesnt_contain(self):
        aac = ""
        self.assertEqual(VariantFormat.AminoAcidChange(aac), "")

    def test_AminoAcidChange_exception(self):
        aac = "YP_512823.1:p.Ser35Tyr.[Ser35Tyr]"
        try:
            VariantFormat.AminoAcidChange(aac)
        except ValidationException as aac_error:
            self.assertEqual(aac_error.errors,
                             "_error: YP_512823.1:p.Ser35Tyr.[Ser35Tyr]")


if __name__ == "__main__":
    unittest.main()
