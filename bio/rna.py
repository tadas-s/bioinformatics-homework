import re
from string import maketrans
import bio


class RNA(str):
    """ Silly RNA sequence class """
    def __new__(cls, content):
        if type(content) is bio.DNA:
            return str.__new__(cls, RNA.from_genome(content))
        else:
            return str.__new__(cls, re.sub('[^cuagCUAG]', '', content))

    def transcribe(self):
        return bio.Peptide(self)

    @staticmethod
    def from_genome(genome):
        if type(genome) is bio.DNA:
            translation = maketrans('tT', 'uU')
            return str(genome).translate(translation)
        else:
            raise ValueError('Expected instance of bio.DNA but got %s' % type(genome))