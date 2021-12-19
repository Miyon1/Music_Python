class Recipe(object):

    def __init__(self, title, ingredients=[], directions=[], notes=""):
        self.title = title
        self.ingredients = ingredients
        self.directions = directions
        self.notes = notes

    def __str__(self):
        return self.title

    def print_recipe(self):
        print(self.title)
        print("Ingredients: ")
        for ingredient in self.ingredients:
            print(ingredient)
        print("Directions: ")
        n = 1
        for direction in self.directions:
            print(n, "-", direction)
            n +=1
        if self.notes:
            print("Special note:")
            print(self.note)
