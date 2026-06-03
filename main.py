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

