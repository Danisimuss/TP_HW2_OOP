from main import Ingredient, Recipe
import pytest

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

def test_init_Recipe_title():
    title = "Шарлотка"
    recipe = Recipe(title, [Ingredient("Соль", 2, "кг")])
    assert recipe.title == title

def test_init_Recipe_ingredients():
    ingredients = [Ingredient("Соль", 2, "кг")]
    recipe = Recipe("Шарлотка", ingredients)
    assert recipe.ingredients == [Ingredient("Соль", 2, "кг")]

def test_add_new_ingredient():
    recipe = Recipe("Шарлотка", [Ingredient("Соль", 2, "кг")])
    recipe.add_ingredient(Ingredient("Перец", 3, "кг"))
    assert recipe.ingredients == [Ingredient("Соль", 2, "кг"), Ingredient("Перец", 3, "кг")]

def test_add_same_ingredient():
    recipe = Recipe("Шарлотка", [Ingredient("Соль", 2, "кг")])
    recipe.add_ingredient(Ingredient("Соль", 3, "кг"))
    assert recipe.ingredients[0].quantity == 5

def test_scale_return():
    recipe1 = Recipe("Шарлотка", [Ingredient("Соль", 2, "кг")])
    recipe2 = recipe1.scale(3)
    assert recipe1 != recipe2

def test_scale_work():
    recipe1 = Recipe("Шарлотка", [Ingredient("Соль", 2, "кг")])
    recipe2 = recipe1.scale(3)
    assert recipe2.ingredients[0].quantity == 6

@pytest.mark.parametrize(
    "ratio", [0, -1, -10],
)
def test_error_value_ratio(ratio):
    with pytest.raises(ValueError):
        recipe1 = Recipe("Шарлотка", [Ingredient("Соль", 2, "кг")])
        recipe2 = recipe1.scale(ratio)

def test_correct_len():
    recipe1 = Recipe("Шарлотка", [Ingredient("Соль", 2, "кг"), Ingredient("Колбаса", 2, "кг"), Ingredient("Соль", 4, "кг"), Ingredient("Колбаса", 2, "г")])
    assert len(recipe1) == 3