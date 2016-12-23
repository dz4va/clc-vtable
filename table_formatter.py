"""
# CLC Table Formatting Functions
# Author: George Dzavashvili
# Email: dzavashviligeorge@gmail.com
# Twitter: @redpix_
# How it works:
    TODO: Explain
"""

# Standard
import re
from config import *

# Own
from table_formatter_exceptions import ValidationException
from logger import Logger

# Constants
FILE_CONFIG = "config_table_formatter.yaml"


class TableFormatter(object):
    """Table Formatter class that contains methods for formatting"""

    @staticmethod
    def FormatVariant(FileInfo, Type, Ref, Allele, Crc):
        """Format the variant based on the type

        Args:
            FileInfo (string): In case of error log this info about file
            Type (string): (SNV || Deletion || Insertion)
            Ref (string): Nucleotide[s] that is/are present in the reference
            Allele (string): Nucleotide[s] that is/are present in the allele
            Crc (string): Coding Region Change

        Returns:
            string: Processed and Formatted variant for the Variant Column
        """
        try:
            if Type == SNP:
                return TableFormatter.ProcessSNP(Ref, Allele, Crc)
            elif Type == INSERTION:
                return TableFormatter.ProcessInsertion(Ref, Allele, Crc)
            elif Type == DELETION:
                return TableFormatter.ProcessDeletion(Ref, Allele, Crc)
            else:
                return ""
        except ValidationException as crc_error:
            # Log here the crc_error message with File info wherever it
            # happened
            Logger.Warn("{} <> {} <> {}".format(FileInfo, crc_error.message,
                                                crc_error.errors))
            return crc_error.errors

    @staticmethod
    def ContainsIllegal(str, illegal_characters):
        """Check if string is in the correct format

        Args:
            str (string): String to check against
            illegal_characters (string): Array of illegal characters

        Returns:
            bool: Valid or not
        """
        for i in illegal_characters:
            if i in str:
                return True
        return False

    @staticmethod
    def ErrorValue(value):
        """Return Crc invalid string in format _error: Crc Value

        Args:
            Crc (string): Coding Region Change

        Returns:
            string: Formatted error indicating string
        """
        return "_error: " + value

    @staticmethod
    def GetIntFromString(value):
        """Extract position as a number from string

        Args:
            value (string): String to search against

        Returns:
            string: Representing the first number in value
        """
        find = re.search(r'\d+', value)
        if find:
            return find.group()
        return ""

    @staticmethod
    def ProcessSNP(Ref, Allele, Crc):
        """Process the SNP in format: T236C
        If Crc is valid
        If Not append whatever is in Crc as _error: Crc Value

        Args:
            Ref (string): Nucleotide[s] that is/are present in the reference
            Allele (string): Nucleotide[s] that is/are present in the allele
            Crc (string): Coding Region Change

        Returns:
            string: Formatted SNP

        Raises:
            ValidationException: If Crc Validation Fails
        """
        final = Ref
        if Crc:
            # Split on :c. because of the AFT92060.1:c.104C>A format and
            coded = Crc.split(":c.")[1]
            if not TableFormatter.ContainsIllegal(coded, ["[", ";"]):
                # Extract the position
                final += TableFormatter.GetIntFromString(coded)
            else:
                # If it's not Valid raise Validation Exception
                fr = "{}{}{}{}".format(
                    final, ">", Allele, TableFormatter.ErrorValue(Crc))
                raise ValidationException("SNP Position Error!", fr)
        else:
            final += ">"
        final += Allele
        return final

    @staticmethod
    def ProcessInsertion(Ref, Allele, Crc):
        """Process the insetion in format: Tins234
        If Crc is valid
        If not append whatever is in Crc as _error: Crc Value

        Args:
            Ref (string): Reference
            Allele (string): Allele
            Crc (string): Coding Region Change

        Returns:
            string: Formatted Insertion

        Raises:
            ValidationException: If Crc Validation Fails
        """
        final = Allele + "ins"
        if Crc:
            coded = Crc.split(":c.")[1]
            if not TableFormatter.ContainsIllegal(coded, ["[", ";"]):
                # Extract the position
                final += TableFormatter.GetIntFromString(coded.split("_")[1])
            else:
                # If it's not Valid raise Validation Exception
                fr = "{}{}".format(
                    final, TableFormatter.ErrorValue(Crc))
                raise ValidationException("Insertion Position Error!", fr)
        return final

    @staticmethod
    def ProcessDeletion(Ref, Allele, Crc):
        """Process the deletion in format: Tdel213

        Args:
            Ref (string): Reference
            Allele (string): Allele
            Crc (string): Coding Region Change

        Returns:
            string: Formatted Deletion

        Raises:
            ValidationException: If Crc Validation Fails
        """
        final = Ref + "del"
        if Crc:
            coded = Crc.split(":c.")[1]
            if not TableFormatter.ContainsIllegal(coded, ["[", ";"]):
                # Extract the position
                final += TableFormatter.GetIntFromString(coded)
            else:
                # If it's not Valid raise Validation Exception
                fr = "{}{}".format(
                    final, TableFormatter.ErrorValue(Crc))
                raise ValidationException("Deletion Position Error!", fr)
        return final

    @staticmethod
    def CodonPos(fd):
        """Gets Codon Position from Formatted Data

        Args:
            fd (string): Formatted Data

        Returns:
            string: Formatted Data
        """
        final = ""
        if fd:
            temp = TableFormatter.GetIntFromString(fd)
            if temp:
                codon_pos = int(temp) % 3
                if codon_pos == 0:
                    return "3"
                else:
                    return str(codon_pos)

        return final

# TODO: Change implementation so that it returns error value not raising
# exception

    @staticmethod
    def AminoAcidChange(aac):
        """Get Amino Acid Change if it exists Ser35Tyr


        Args:
            aac (string): Amino Acid Change value

        Returns:
            string: Represent the amino acid change
        """
        final = ""
        if aac:
            coded = aac.split(":p.")[1]
            if not TableFormatter.ContainsIllegal(coded, ["[", ";"]):
                final += coded
            else:
                # Raise Exception and return the whole Amino Acid Change string
                fr = "{}{}".format(
                    final, TableFormatter.ErrorValue(aac))
                raise ValidationException(
                    "Couldn't Extract Amino Acid Change!",
                    fr)
        return final
