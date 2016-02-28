#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matchText import *
import unittest


a = u'1 12.43.78 hei du'
b = u'3 hei dU'
c = u'5 Det var en gang'
d = u'5 I dag'
e = u'5 i dag h \" \. \" \@ 3'
f = u'5 I ALLØ dager er DETTE Foor'
g = u'5 Hei7 re8.8 hmmm '
h = u'5 I a 8 2 o'
i = u'5 123.234324.32434 23432. 334.h 434324 hei 53'
j = u'5 I 1857 1958 kom en mann på 1800-tallet 12343 123 12.34'

class Test_MatchText(unittest.TestCase):
    def test_startWithSequence(self):
        self.assertEqual(MatchText(a[2:]).startWithSequence(), True)
        self.assertEqual(MatchText(b[2:]).startWithSequence(), False)
    def test_startWithAWord(self):
        self.assertEqual(MatchText(a[2:]).startWithAWord(), False)
        self.assertEqual(MatchText(b[2:]).startWithAWord(), False)
        self.assertEqual(MatchText(c[2:]).startWithAWord(), True)
        self.assertEqual(MatchText(d[2:]).startWithAWord(), True)
        self.assertEqual(MatchText(g[2:]).startWithAWord(), False)
    def test_nrOf1CharacterWords(self):
        self.assertEqual(MatchText(e[2:]).nrOf1CharacterWords(), 3)
    def test_nrOfWords(self):
        self.assertEqual(MatchText(e[2:]).nrOfWords(), 8)
    def test_nrOfUpperCaseWords(self):
        self.assertEqual(MatchText(f[2:]).nrOfUpperCaseWords(), 3)
    def test_nrOfNumbers(self):
        self.assertEqual(MatchText(i[2:]).nrOfNumbers(), 4)
    def test_nrOfYear(self):
        self.assertEqual(MatchText(j[2:]).nrOfYears(), 3)
    def test_nrOfWordsWithUpperCase(self):
        self.assertEqual(MatchText(f[2:]).nrOfWordsWithUpperCase(), 4)
    def test_nrOfMixedWords(self):
        self.assertEqual(MatchText(g[2:]).nrOfMixedWords(), 2)
    def test_hasNrOf1000CommonNorwegianWords(self):
        self.assertEqual(MatchText(c[2:]).hasNrOf1000CommonNorwegianWords(4), True)
        self.assertEqual(MatchText(c[2:]).hasNrOf1000CommonNorwegianWords(3), True)
    
        
if __name__ == '__main__':
    unittest.main()