import sys
#import json
#prompt a user to create a recipe
#Ask for Ingredients
#Ask for Instructions
#Save/Store it into dictionary
def create():
    ask_recipe = ''
    ask_instruction = ''
    ask_ingredients = ''
    recipe_dict = dict()
    #counter = str(1)
    print("Create a recipe! Type 'exit' to leave")

    for ask_recipe in range (1):
        ask_recipe = input("Recipe Name: ")
        recipe_dict.update(ask_recipe = 'Nothing Yet')
        if ask_recipe == 'exit':
            exit(1)

    while ask_instruction != 'exit':
        ask_instruction = input("Instructions: ")
        if ask_instruction == 'exit':
            while ask_ingredients != 'exit':
                ask_ingredients = input("Ingredients: ")  
                if ask_ingredients == 'exit':
                    #recipe_dict.update(ask_recipe = ask_instruction)
                    #recipe_dict.update(ask_recipe, ask_ingredients)
                    for key, value in recipe_dict.items():
                        print(key,':',value)
                        exit(1)



    print("Create a recipe! Enter '0' to exit")
    print(ask_recipe)
    print(ask_instruction)
    print(ask_ingredients)

def listrecipe():
    print("listrecipe")

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
