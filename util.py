#!/usr/bin/python
# -*- coding: utf_8 -*-

from fractions import Fraction
import unicodedata
import codecs
import re


def stringtonum(num_str):
    """
    There are many ways to write 1.5 as a string:
        1 1/2
        1-1/2
        1½
        1 ½

    NOTE: If reading data from a file, open using codecs.open with encoding option UTF-8.

    :param
        num_str: string representing a number, containing digits and/or fractions (whether vulgar or normal form) and
        possibly hyphens or spaces
    :return
        num: numerical form of given string
    """

    # original conversion: num = float(sum(Fraction(unicodedata.numeric(s)) for s in re.findall(r"[\w/]+", s)))

    num = 0
    for s in re.findall(r'[\w/]+', num_str):                            # finds digits and normal fractions
        num += Fraction(s)                                              # add numeric value to running sum

    ufracs = re.compile(ur'[\u2150-\u215E\u00BC-\u00BE]', re.UNICODE)   # regex for vulgar fractions
    for c in ufracs.findall(num_str):                                   # finds vulgar fractions
        num += unicodedata.numeric(c, 'UTF-8')                          # add numeric value to running sum

    return num


def mixed_num(num):
    """
    Format a number as a mixed fraction.

    Examples:
        convert_to_mixed_numeral('-55/10') # '-5 1/2'
        convert_to_mixed_numeral(-55/10) # '-5 1/2'
        convert_to_mixed_numeral(-5.5) # '-5 1/2'

    @:param
        num (int|float|str): The number to format. It is coerced into a string.

    @:return
        str: "num" formatted as a mixed fraction.

    from J.Money on StackOverflow
    https://stackoverflow.com/questions/32085047/converting-an-improper-fraction-to-a-mixed-number-with-python
    """
    num = Fraction(str(num)) # use str(num) to prevent floating point inaccuracies
    n, d = (num.numerator, num.denominator)
    m, p = divmod(abs(n), d)
    if n < 0:
        m = -m
    return '{} {}/{}'.format(m, p, d) if m != 0 and p > 0 \
        else '{}'.format(m) if m != 0 \
        else '{}/{}'.format(n, d)


if __name__ == "__main__":
    f = codecs.open('data/char.txt', 'r', 'utf-8')
    for line in f:
        print(line.strip() + '\t->\t' + str(stringtonum(line)))

"""
working conversion

for line in f:
    print(line)
    ufracs = re.compile(ur'[\u2150-\u215E\u00BC-\u00BE]', re.UNICODE)
    fracs = ufracs.findall(line)
    print('fracs:\t' + str(fracs))
    for frac in fracs:
        print(unicodedata.numeric(frac.strip(), 'UTF-8'))
"""