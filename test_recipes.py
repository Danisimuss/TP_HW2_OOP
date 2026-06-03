from main import Ingredient
def test_init_Ingredient_name():
    name = "Соль"
    ingredient = Ingredient(name, 2, "кг")
    assert ingredient.name == name

def test_init_Ingredient_quantity():
    quantity = 2
    ingredient = Ingredient("Соль", quantity, "кг")
    assert ingredient.quantity == quantity

def test_init_Ingredient_unit():
    unit = "кг"
    ingredient = Ingredient("Соль", 2, unit)
    assert ingredient.unit == unit

def test_str_format():
    name = "Соль"
    quantity = 2
    unit = "кг"
    ingredient = Ingredient(name, quantity, unit)
    assert str(ingredient) == f"{name}: {quantity} {unit}"

def test_eq_same_ingredients():
    name1 = "Соль"
    quantity1 = 2
    unit1 = "кг"
    ingredient1 = Ingredient(name1, quantity1, unit1)
    name2 = "Соль"
    quantity2 = 3
    unit2 = "кг"
    ingredient2 = Ingredient(name2, quantity2, unit2)
    assert ingredient1 == ingredient2

def test_eq_not_same_name():
    name1 = "Перец"
    quantity1 = 2
    unit1 = "кг"
    ingredient1 = Ingredient(name1, quantity1, unit1)
    name2 = "Соль"
    quantity2 = 2
    unit2 = "кг"
    ingredient2 = Ingredient(name2, quantity2, unit2)
    assert ingredient1 != ingredient2

def test_eq_not_same_unit():
    name1 = "Соль"
    quantity1 = 2
    unit1 = "кг"
    ingredient1 = Ingredient(name1, quantity1, unit1)
    name2 = "Соль"
    quantity2 = 2
    unit2 = "т"
    ingredient2 = Ingredient(name2, quantity2, unit2)
    assert ingredient1 != ingredient2