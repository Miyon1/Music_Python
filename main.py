from classes.ingredients import Ingredient
from classes.recipes import Recipe

def main():
    i = Ingredient(title="egg")

    r = Recipe(title="scrambled eggs", ingredients=[i], directions=["Break egg", "Beat egg", "Cook egg"])
    
    r.print_recipe()



if __name__ == "__main__":
    main()
