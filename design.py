import sys

#Save/Store it into dictionary
def create():
    recipe_name = ''

    print("Create a recipe!")
    recipe_name = input("Recipe Name: ")

    instructions = []
    instruction = ""

    while True:
        instruction = input("Instructions: ")
        if instruction == 'exit':
            break
        instructions.append(instruction)

    ingredients = []
    ingredient = ''

    while True:
        ingredient = input("Ingredients: ")  
        if ingredient == 'exit':
            break
        ingredients.append(ingredient)


#Step1: define the class
#Step2: Init the class
#Step3: Insert data into new class object
#Step4: key(recipe_name) -> class
#Step5: use dictionary to retrieve recipes objects and manipulate their contents


#animalDictionary = {}

#class Animal:
    #speak = ""

#name = input("What is your animal?: ")
#sound = input("What does it say?: ")
#user_input == "meow"

#some_animal = new Animal();
#some_animal.speak = sound
#key(animal name) -> value("a new animal")
#animalDictionary[name] = some_animal

#-----

#animal = animalDictionary["wowzers"]
#animal.speak #meow
#animal.speak = "mooo"
#animalDictionary["wowzers"] = animal

#    "some_string_here" -> "wow"

#    "apple_pie" -> apple_pie

#    class recipe:
#        name: string
#        instructions: []string
#        ingredients: []string


#     apple_pie = new recipe();
#     apple_pie.name = "apple pie merg"
#     apple_pie.instruction = []string
#     apple_pie.ingredients = []string

#     someRecipe = recipeDict["apple_pie"]
#     apple_pie

#     apple_pie.open = False 
#     print(apple_pie.open)



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
