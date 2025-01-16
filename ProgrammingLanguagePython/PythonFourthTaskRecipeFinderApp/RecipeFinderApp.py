# Recipe Finder Application.

'''Problem Statement:
Create a recipe finder app that lets users:

1. Search Recipes:
    ○ Type ingredients into an input field and press Enter.
    ○ Fetch matching recipes stored as an array of objects.
2. Bonus Features:
    ○ Allow recipe filtering by type (e.g., Lunch, Breakfast) using a dropdown menu.'''


recipes=[{'name':'poha','ingredients':['poha','oil','spices','vegetables'],'type':'breakfast'},
         {'name':'masala dosa','ingredients':['rice flour','mainda','spices','vegetables','coconut cold sauce'],'type':'breakfast'},
         {'name':'angara panner','ingredients':['panner','oil','spices','tomatos','angar'],'type':'lunch'},
         {'name':'non-veg-biryani','ingredients':['rice','oil','spices','vegetables','chicken'],'type':'dinner'}]

def search_recipes_by_ingredients():
    ingredients=input("Enter ingredients separated by comma").lower().split(",")
    ingredients=[item.strip() for item in ingredients]
    for recipe in recipes:
        if all(item in recipe['ingredients'] for item in ingredients):
            print ("found")
def filtering_by_type():
    recipe_type=input("Enter recipe type (e.g. breakfast,lunch,dinner) : ").lower()
    for recipe in recipes:
        if recipe['type']==recipe_type:
            print()

def option():
    while True:
        print("\t\t\t\t\t\t\tWelcome to Recipe Finder App !\n\n")
        print("which task you want to perform, choice from these options- \n")
        print(" 1. Search Recipe by Ingredient. \n 2. Filter Recipe by Type. \n")
        task=input("Enter Your Task: ")
        if task=='1':
            search_recipes_by_ingredients()
        elif task=='2':
            filtering_by_type()
        elif task=='3':
            print("\n\t\t\t\t\t\t\tExiting from the app......\n")
            break
        else:
            print("\nInvalid Input, Please enter valid option. \n")
            option()
        continue_task=input("Do you want to perform another task (yes/no) : ").lower()
        if continue_task!='yes':
            print("\n\t\t\t\t\t\tYour are successfully exit from the app..\n")
            break

option()