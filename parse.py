import codecs
import re

from recipe import Recipe
from util import stringtonum

VULGAR_FRACTIONS = {}


def parse_recipe(path):

    recipe = Recipe()

    f = codecs.open(path, 'r', 'utf-8')

    for line in f:
        if line.strip():  # if line not empty
            name, qty, unit = parse_line(line)  # parse ingredient and amount
            recipe.new_ingredient(name, qty, unit)

    return recipe


def parse_line(line):
    """
    Parses one line of recipe, extracting ingredient name, quantity, and unit.
    :param line: string describing one ingredient of recipe
    :return: ingredient name, quantity, and unit
    """

    # remove parentheticals
    line = re.sub(r'\([^)]+\)', '', line)

    """
    new pseudocode:
    take first word of line and try to parse as number
        if this works, repeat with second word              1 1/4 cups       
        if neither method works, set quantity to None       pinch of salt
    take next word and see if it's a standard unit          1 cup
        if not, set unit to None
    strip "of" from outside if present                      pinch of salt, oil of bergamont 
    """

    # split at first instance of word containing alphabetical character
    words = line.split()                            # split by whitespace into "words"
    for i in range(len(words)):                     # loop thru words until find one with alphabetical char
        if re.search(r'[a-zA-Z]', words[i]):        # check if word contains a-z or A-Z
            break                                   # if so, split at that index

    if i > 0:                                       # if ingredient has a quantity
        amount_str = ' '.join(words[:i])            # rejoin all words describing quantity
        unit_str = ' '.join(words[i:i+1])           # rejoin all words describing unit
        name = ' '.join(words[i+1:])

        # process amount
        # convert fractions to decimals

        quantity = stringtonum(amount_str)

        # process units

        # display units
        TBSP = 'Tbsp'
        TSP = 'tsp'
        CUP = 'cup'
        LB = 'lb'
        OZ = 'oz'
        G = 'g'

        # standard units
        units = {'tablespoon': TBSP, 'tbsp': TBSP,
                 'teaspoon': TSP, 'tsp': TSP,
                 'cup': CUP, 'c': CUP,
                 'pound': LB, 'lb': LB,
                 'ounce': OZ, 'oz': OZ,
                 'gram': G, 'g': G}

        unit_key = unit_str.lower().strip('.').strip('s')   # lowercase, strip periods and plural s

        if unit_key in units:                               # if one of standard units
            unit = units[unit_key]                          # replace with desired form of unit
        else:
            unit = unit_str                                 # otherwise leave as given

    else:                                                   # no quantity, so put whole line as ingredient name
        name = line.strip()                                 # but strip any outer whitespace first
        quantity = 0
        unit = ''

    return [name, quantity, unit]