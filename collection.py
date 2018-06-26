import ref


class Collection:
    def __init__(self, *recipes):
        if recipes is None:
            self.recipes = []
        else:
            self.recipes = recipes
            print('%d recipes added!' % len(recipes))

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def compare(self):
        for kind in ref.kinds:
            for recipe in self.recipes:
                print('new recipe')
                ingredients = [ingredient for ingredient in recipe.ingredients if ingredient.kind == kind]
                for ingredient in ingredients:
                    print(ingredient.text())
