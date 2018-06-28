import codecs

from ingredient import Ingredient
import ref


class Recipe:
    def __init__(self, path):
        self.ingredients = []
        f = codecs.open(path, 'r', 'utf-8')
        for line in f:
            if line.strip():                                # if line not empty
                self.ingredients.append(Ingredient(line))   # parse line to extract ingredient info

    def display(self):
        for kind in ref.kinds:
            ingredients = [ingredient for ingredient in self.ingredients if ingredient.kind == kind]
            for ingredient in ingredients:
                print(ingredient.text())
