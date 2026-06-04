class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit


    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        value = float(value)
        self._quantity = value


    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        if not(isinstance(Ingredient, other)):
            return False
        return self.name == other.name and self.unit == other.unit



class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient: Ingredient):
        for some_ingredient in self.ingredients:
            if ingredient == some_ingredient:
                some_ingredient.quantity += ingredient.quantity
            else:
                self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if (type(ratio) == int or type(ratio) == float) and ratio > 0:
            return True
        else:
            return False

    def scale(self, ratio: float):
        new_ingredients = []
        for ingred in self.ingredients:
            new_ingred = Ingredient(ingred.name, ingred.quantity * ratio, ingred.unit)
            new_ingredients.append(new_ingred)
        return Recipe(self.title, new_ingredients)
    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        return f"Название блюда: {self.title}, список ингредиентов: {' '.join([str(i) for i in self.ingredients])}"



class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        new_recipe = recipe.scale(portions)
        for ingredient in new_recipe.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str):
        self._items = [item for item in self._items if item[1] != title]

    def get_list(self):
        dict_ingred = {}
        for ingred in self._items:
            ingredient = ingred[0]
            if (ingredient.name, ingredient.unit) not in dict_ingred:
                dict_ingred[(ingredient.name, ingredient.unit)] = ingredient.quantity
            else:
                dict_ingred[(ingredient.name, ingredient.unit)] += ingredient.quantity
        list_ingredients = []
        for ing in dict_ingred:
            list_ingredients.append(Ingredient(ing[0], dict_ingred[ing], ing[1]))
        list_ingredients = sorted(list_ingredients, key=lambda x: x.name)
        return list_ingredients

        def __add__(self, other: 'ShoppingList'):
            shop_list1 = self._items
            shop_list2 = other._items
            new_shop_list = ShoppingList()
            new_shop_list._items = shop_list1 + shop_list2
            return new_shop_list



class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        if ingredients is None:
            ingredients = []
        self.diet_type = diet_type
        super().__init__(title, ingredients)

    def scale(self, ratio: float):
        new_recipe = super().scale(ratio)
        return DietaryRecipe(new_recipe.title, self.diet_type, new_recipe.ingredients)

    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"
