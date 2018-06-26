from ingredient import Ingredient
import ref


class Recipe:
    def __init__(self):
        self.ingredients = []

    def new_ingredient(self, name, qty, unit):
        self.ingredients.append(Ingredient(name, qty, unit, ref.kinds, ref.aliases))

    def display(self):
        for kind in ref.kinds:
            ingredients = [ingredient for ingredient in self.ingredients if ingredient.kind == kind]
            for ingredient in ingredients:
                print(ingredient.text())
