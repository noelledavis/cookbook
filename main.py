from recipe import Recipe
from collection import Collection

recipe1 = Recipe('data/recipe1.txt')
print('-- RECIPE 1 --')
recipe1.display()

recipe2 = Recipe('data/recipe2.txt')
print('-- RECIPE 2 --')
recipe2.display()

my_collection = Collection(recipe1, recipe2)
my_collection.compare()
