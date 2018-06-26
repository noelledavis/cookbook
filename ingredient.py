class Ingredient:

    def __init__(self, name, qty, unit, kinds, aliases):
        self.name = name
        self.quantity = qty
        self.unit = unit

        self.kind = kinds[-1]
        for k in kinds[::-1]:
            for a in aliases[k]:
                if a in name:
                    self.kind = k
                    break

    def text(self):
        return '%s:\t %.2f - %s - %s' % (self.kind, self.quantity, self.unit, self.name)
