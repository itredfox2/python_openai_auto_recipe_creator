#########################
# IMPORTS               #
#########################

from recipe import RecipeGenerator

from dalle import Dish2Image

#########################
# MAIN               	#
#########################

# create an instance of the RecipeGenerator class

gen = RecipeGenerator()

# ask the user for input and create the recipe

recipe = gen.generate_recipe()

# print the recipe

print(recipe)

# create an instance of the Dish2Image class

dalle = Dish2Image(recipe)

# visualize the dish

dalle.generate_image()

# store the recipe in a text file

gen.store_recipe(recipe, f"{dalle.title}.txt")

