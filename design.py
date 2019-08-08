import sys
#prompt a user to create a recipe
#Ask for Ingredients
#Ask for Instructions
#Save/Store it into dictionary
def create():
    ask_recipe = input("Recipe Name: ")
    ask_instruction = input("Instructions: ")
    ask_create = input("Ingredients: ") 

    print(ask_recipe)
    print(ask_instruction)
    print(ask_create)

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
