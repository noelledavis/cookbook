# ingredient kinds
FLOUR, SWEETENER, LEAVENING, OIL, LIQUID, FLAVOR, OTHER \
    = ['flour', 'sweetener', 'leavening', 'oil', 'liquid', 'flavor', 'other']

kinds = [FLOUR, SWEETENER, LEAVENING, OIL, LIQUID, FLAVOR, OTHER]

aliases = {FLOUR: ['flour', 'all-purpose flour', 'whole-wheat flour', 'oats', 'cocoa'],
           SWEETENER: ['sugar', 'honey', 'syrup'],
           LEAVENING: ['baking soda', 'baking powder', 'egg'],
           OIL: ['oil', 'butter', 'tahini'],
           LIQUID: ['milk', 'water', 'juice'],
           FLAVOR: ['salt', 'vanilla', 'almond'],
           OTHER: []}

# display units
# volumetric
TSP = 'tsp'
TBSP = 'Tbsp'
CUP = 'cup'
PT = 'pint',
QT = 'quart',
# mass
LB = 'lb'
OZ = 'oz'
G = 'g'
# other
PINCH = 'pinch'

# standard units
units = {'teaspoon': TSP, 'tsp': TSP,
         'tablespoon': TBSP, 'tbsp': TBSP,
         'cup': CUP, 'c': CUP,
         'pint': PT, 'pt': PT,
         'quart': QT, 'qt': QT,
         'pound': LB, 'lb': LB,
         'ounce': OZ, 'oz': OZ,
         'gram': G, 'g': G,
         'pinch': PINCH}