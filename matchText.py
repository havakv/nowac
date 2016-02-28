#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Small library for matching text. It is primarily used to ensure a string fulfills certain properties.
"""


import re
import pandas as pd

# Set up encodings
import codecs #used to set utf-8 enconding, so we get unicode strings
import locale
locale.setlocale(locale.LC_ALL, 'no_NO') #so \w, \W, etc. contains norwegian letters


def mostCommonNorwegianWords(nr):
    """
    Returns a set of the 'nr' most common norwegian words.
    """
    return set(pd.read_table('ord10k_utf-8.txt', sep=r'\s+', header=None, 
                             skiprows=5, nrows = nr,  encoding='utf-8', 
                            )[4].values)


class MatchText(object):
    """Small class for doing doing the subsetting... Write sething"""
    # Some usefull sets of letters.
    uc = ur'[A-ZÆØÅ]'
    lc = ur'[a-zæøå]'
    alp = ur'[a-zA-ZæøåÆØÅ]'
    #
    # 1000 most common norwegian words
    mostCommonWords1000 = mostCommonNorwegianWords(1000)
    #
    # Patterns used in the class.
    nrSeq = re.compile(r'\A\d+\.\d+')
    startWord = re.compile(r'\A'+uc+alp+ur'+\s|\A[IÅ]\s', re.U)
    oneCharacterWords = re.compile(r'(?=((?:\A|\s)\w(?:\s|$)))', re.U)
    ucWords = re.compile(r'(?=((?:\A|\s)'+uc+r'+(?:\s|$)))', re.U)
    allNumbers = re.compile(r'(?=((?:\A|\s)'+r'\d+(?:\.\d*)*'+r'(?:\s|$)))')
    wordsWithUc = re.compile(r'\w*'+uc+r'+\w*', re.U)
    mixedWords = re.compile(alp+ur'+[^a-zA-ZæøåÆØÅ\s]+'+
                            ur'|[^a-zA-ZæøåÆØÅ\s]+'+alp+r'+', re.U)
    years = re.compile(r'(?=((?:\A|\s)'+r'\d{4}'+r'(?:-|\s|$)))')
    #
    def __init__(self, text):
        self.text = text
    def startWithSequence(self):
        """
        Checks if the text start with a number sequence with a '.'.
        """
        return len(self.nrSeq.findall(self.text)) > 0
    def startWithAWord(self):
        """
        Retruns True if the text start with an uppercase letter,
        followed by one or more letters. Exeptions I and Å.
        """
        return len(self.startWord.findall(self.text)) > 0
    def nrOf1CharacterWords(self):
        """
        Returns number of words that only contain one character.
        This does not count sings like . " ' $ @.
        """
        return len(self.oneCharacterWords.findall(self.text))
    def nrOfWords(self):
        """
        Numer of words in text. Separated by whitespace.
        This counts everything separated by a whitespace.
        """
        return len(self.text.split())
    def nrOfUpperCaseWords(self):
        """
        Numer of words that only contains uppercase letters.
        """
        return len(self.ucWords.findall(self.text))
    def nrOfNumbers(self):
        """
        Number of numbers in text. They can be separated by one or more '.'.
        """
        return len(self.allNumbers.findall(self.text))
    def nrOfYears(self):
        """
        Number of years in text. 1957, 1800-tallet.
        """
        return len(self.years.findall(self.text))
    def nrOfWordsWithUpperCase(self):
        """
        Number of words with one or more upper case letters. 
        The word can only contain alphanumberic characters.
        """
        return len(self.wordsWithUc.findall(self.text))
    def nrOfMixedWords(self):
        """
        Number of words that are a mix between letters and non-letters.
        """
        return len(self.mixedWords.findall(self.text))
    def hasNrOf1000CommonNorwegianWords(self, Nr):
        """
        Returns True if at least Nr words in the text are in the set of
        the 1000 most common norwegian words.
        """
        n = 0
        for word in self.text.split():
            n += (word.lower() in self.mostCommonWords1000)
            if n == Nr:
                return True
        return False
          
    
        
        
    

