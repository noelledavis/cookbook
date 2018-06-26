from parse import parse_recipe
from collection import Collection

recipe1 = parse_recipe('data/recipe1.txt')
print('-- RECIPE 1 --')
recipe1.display()

recipe2 = parse_recipe('data/recipe2.txt')
print('-- RECIPE 2 --')
recipe2.display()

my_collection = Collection(recipe1, recipe2)
my_collection.compare()
