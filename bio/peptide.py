import re
import bio
from bio.iterators import chunker
from string import maketrans

peptide_translation_table = {
    'AAA': 'K',
    'AAC': 'N',
    'AAG': 'K',
    'AAU': 'N',
    'ACA': 'T',
    'ACC': 'T',
    'ACG': 'T',
    'ACU': 'T',
    'AGA': 'R',
    'AGC': 'S',
    'AGG': 'R',
    'AGU': 'S',
    'AUA': 'I',
    'AUC': 'I',
    'AUG': 'M',
    'AUU': 'I',
    'CAA': 'Q',
    'CAC': 'H',
    'CAG': 'Q',
    'CAU': 'H',
    'CCA': 'P',
    'CCC': 'P',
    'CCG': 'P',
    'CCU': 'P',
    'CGA': 'R',
    'CGC': 'R',
    'CGG': 'R',
    'CGU': 'R',
    'CUA': 'L',
    'CUC': 'L',
    'CUG': 'L',
    'CUU': 'L',
    'GAA': 'E',
    'GAC': 'D',
    'GAG': 'E',
    'GAU': 'D',
    'GCA': 'A',
    'GCC': 'A',
    'GCG': 'A',
    'GCU': 'A',
    'GGA': 'G',
    'GGC': 'G',
    'GGG': 'G',
    'GGU': 'G',
    'GUA': 'V',
    'GUC': 'V',
    'GUG': 'V',
    'GUU': 'V',
    'UAA': '',
    'UAC': 'Y',
    'UAG': '',
    'UAU': 'Y',
    'UCA': 'S',
    'UCC': 'S',
    'UCG': 'S',
    'UCU': 'S',
    'UGA': '',
    'UGC': 'C',
    'UGG': 'W',
    'UGU': 'C',
    'UUA': 'L',
    'UUC': 'F',
    'UUG': 'L',
    'UUU': 'F'
}


class Peptide(str):
    """ Silly Peptide class """
    def __new__(cls, content):
        if type(content) is bio.RNA:
            return str.__new__(cls, Peptide.from_rna(content))
        else:
            return str.__new__(cls, re.sub('[^a-zA-Z]', '', content))

    @staticmethod
    def from_rna(rna):
        if type(rna) is bio.RNA:
            return ''.join(map(lambda chunk: peptide_translation_table[chunk], chunker(str(rna).upper(), 3)))
        else:
            raise ValueError('Expected instance of bio.RNA but got %s' % type(rna))


class Translator:
    __rna_to_peptide = None
    __dna_to_peptide = None
    __peptide_to_rna = None
    __peptide_to_dna = None

    @staticmethod
    def rna_to_peptide(table=None):
        """
        @param table: dict set translation table
        @return: dict
        """
        if table is not None:
            Translator.reset()
            Translator.__rna_to_peptide = table
        elif Translator.__rna_to_peptide is None:
            Translator.__rna_to_peptide = peptide_translation_table

        return Translator.__rna_to_peptide

    @staticmethod
    def dna_to_peptide():
        if Translator.__dna_to_peptide is None:
            translation = maketrans('uU', 'tT')
            Translator.__dna_to_peptide = dict(
                map(lambda item: (item[0].translate(translation), item[1]), Translator.rna_to_peptide().iteritems())
            )

        return Translator.__dna_to_peptide

    @staticmethod
    def peptide_to_rna():
        pass

    @staticmethod
    def peptide_to_dna():
        pass

    @staticmethod
    def reset():
        Translator.__rna_to_peptide = None
        Translator.__dna_to_peptide = None
        Translator.__peptide_to_rna = None
        Translator.__peptide_to_dna = None
