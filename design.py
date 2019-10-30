import sys
#import json

# Recipe is a representation of a cooking recipe
recipe_dict = {}
class Recipe:
    def __init__(self):
        self.ingredients = []
        self.instructions = []
        self.name = ""

#Save/Store it into dictionary, Test it
def create():
    recipe = Recipe()

    print("Create a recipe!")
    recipe.name = input("Recipe Name: ")


    while True:
        ingredients = input("Ingredients: ")  
        if ingredients == 'exit':
            break
        recipe.ingredients.append(ingredients)


    while True:
        instructions = input("Instructions: ")
        if instructions == 'exit':
            break
        recipe.instructions.append(instructions)
    
    recipe_dict[recipe.name] = recipe

    recipe_file_write = open('recipe.txt','w')
    recipe_file_write.write(str(recipe_dict))
    recipe_file_write.close()

    #with open('recipe.txt', 'w') as json_file:
        #json.dump(recipe_dict, json_file)

    #open a file, change recipe dict into json
    #write something to that file, check it (read)

    return
    #recipedict = recipe_dict[recipe.name]
    #print(recipedict)
    #print(recipedict.ingredients)
    #print(recipedict.instructions)

# The list recipe function should be able to take a recipe name
# and print out just that recipe.
#1. Get recipe name
#2. Find recipe name in dict
#3. Print out that recipe
def listrecipe():
    recipe_file_read = open('recipe.txt','r')
    print(recipe_file_read.read())
    #with open('recipe.txt', 'r') as recipecheck:
        #data = json.load(recipecheck)
    #recipe = Recipe()

    #print("Your recipe!")
    #recipe.name = input("Name of Created recipe: ")

    #if recipe.name in recipe_dict:
        #recipe_test = recipe_dict[recipe.name]
        #print(recipe_test.name)

    #else:
        #print("you're terrible shane") or print("you suck shane")

def update():
    print("update")

def delete():
    print("delete")

def main():
    # check if user has entered enough arguments
    if len(sys.argv) != 2:
        print("Usage: recipe <Action> [args]")
        sys.exit(1)

    #argv stores arguments to your program
    action = sys.argv[1]
    
    if "create" == action:
        create()
    elif "list" == action:
        listrecipe()
    elif "update" == action:
        update()
    elif "delete" == action:
        delete()
    else:
        print("command not found")
        sys.exit(1)
main()