# To Do
- [x] unicode fractions
- [ ] ingredient class vs ingredient name
- [ ] webpage integration
- [ ] only pick up on standard units (cup, lb, tsp, g, etc.) and make option for no unit & measure
- [ ] framework for ingredient type
    - class ingredients: check if one name entirely contained in the other, if no commas, then group together
    - determine ingredient type when creating the *collection*. speed cost probably negligible.
    - note: adding ingredient to recipe after creating collection may not update the collection...
    - fuzzywuzzy string matching? see http://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/
- [ ] scale recipes by "flour" content - or by carb count?
- [ ] google for sugar/carb/fat/liquid? content of ingredients and compute ratios
    - e.g. sugar to bulk, bulk to leavening, liquid to bulk
    - have a conversion btwn baking soda + baking powder
- [ ] brainstorm on display formatting
    - table?


# Plan
- input: pumpkin muffins; emphasize: strong pumpkin flavor, low sugar, ww flour
- emphases: maybe order a list in priority order? toggle switches?
  possible emphases: low (/no) refined sugar, low fat, light, dense, whole-wheat, chewy/crumbly, moist/dry
  learns user's preferences for each type of baked good and tunes recipes to those? (for things like chewy-crumbly, moist-dry; for others, still asks for choice)

# Resources

http://justinmklam.com/posts/2018/04/python-flask-heroku-tutorial/

full code: https://github.com/justinmklam/recipe-converter/blob/master/recipeConverter.py

USDA API: fZyrrP9ayB7j8LWVLHLz63sI8vW2vXOJHrdyJVxD

Edamam API
