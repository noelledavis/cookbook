import re
from fuzzywuzzy import fuzz, process

import ref
from util import string2num


class Ingredient:

    def __init__(self, line):

    # def parse_line(self, line):
        """
        Parses one line of recipe, extracting ingredient name, quantity, and unit.
        :param line: string describing one ingredient of recipe
        :return: ingredient name, quantity, and unit
        """

        line = re.sub(r'\([^)]+\)', '', line)               # remove parentheticals

        line = line.split()                                 # split by whitespace into "words"

        # find index of first word containing alphabetical character
        index_qty_unit = 0
        for i in range(len(line)):                          # loop thru words until find one with alphabetical char
            if re.search(r'[a-zA-Z]', line[i]):             # check if word contains a-z or A-Z
                index_qty_unit = i                          # word index of end of quantity / start of unit
                break                                       # if so, split at that index

        # process ingredient quantity

        if index_qty_unit > 0:                              # if ingredient has a quantity
            amount_str = ' '.join(line[:index_qty_unit])    # rejoin all words describing quantity
            quantity = string2num(amount_str)               # convert string with integers and/or fractions to number

        else:                                               # no quantity
            quantity = 0

        # process ingredient unit

        raw_unit = line[index_qty_unit]                     # get possible unit
        unit_key = raw_unit.lower().strip('.').strip('s')   # lowercase, strip periods and plural s

        if unit_key in ref.units:                               # if one of standard units
            unit = ref.units[unit_key]                          # replace with desired form of unit
            index_unit_name = index_qty_unit + 1            # index of end of unit / start of name
        else:
            unit = None                                     # otherwise no unit
            index_unit_name = index_qty_unit                # index of end of unit / start of name

        # process ingredient name

        if line[index_unit_name] == 'of':                   # skip over initial "of" if present
            index_unit_name += 1
        raw_name = ' '.join(line[index_unit_name:])         # compile name string

        """
        FIX THIS SECTION
        """

        name = None
        matches = []
        for k in ref.kinds:
            for a in ref.aliases[k]:
                score = fuzz.partial_token_set_ratio(name, a)
                if score == 100:
                    matches.append(a)
                    break

        name = process.extractOne(name, matches, scorer=fuzz.token_set_ratio)

        kind = ref.kinds[-1]
        for k, a in ref.aliases.items():
            if a == name:
               kind = k
               break

        self.quantity = quantity
        self.unit = unit
        self.name = name
        self.kind = kind

    def text(self):
        return '%s:\t %.2f - %s - %s' % (self.kind, self.quantity, self.unit, self.name)
