NUM_TYPES = 7

FLOUR, SWEETENER, LEAVENING, OIL, LIQUID, FLAVOR, OTHER \
    = ['flour', 'sweetener', 'leavening', 'oil', 'liquid', 'flavor', 'other']

kinds = [FLOUR, SWEETENER, LEAVENING, OIL, LIQUID, FLAVOR, OTHER]

aliases = {FLOUR: ['flour', 'oats', 'cocoa'],
           SWEETENER: ['sugar', 'honey', 'syrup'],
           LEAVENING: ['baking soda', 'baking powder', 'egg'],
           OIL: ['oil', 'butter', 'tahini'],
           LIQUID: ['milk', 'water', 'juice'],
           FLAVOR: ['salt', 'vanilla', 'almond'],
           OTHER: []}