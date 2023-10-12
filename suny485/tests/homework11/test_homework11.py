import pytest
from suny485.projects.homework11.fruit_formal import get_formal_name

# Parametrize the test for valid fruit names
@pytest.mark.parametrize("fruit_name, formal_name", [
    ('apple', 'Malus domestica'),
    ('banana', 'Musa acuminata'),
    ('orange', 'Citrus × sinensis'),
    ('strawberry', 'Fragaria × ananassa'),
    ('grape', 'Vitis vinifera'),
    ('pineapple', 'Ananas comosus'),
    ('mango', 'Mangifera indica'),
    ('blueberry', 'Vaccinium corymbosum'),
    ('peach', 'Prunus persica'),
    ('watermelon', 'Citrullus lanatus'),
    ('cherry', 'Prunus avium'),
    ('pear', 'Pyrus'),
    ('plum', 'Prunus domestica'),
    ('raspberry', 'Rubus idaeus'),
    ('kiwi', 'Actinidia deliciosa'),
    ('lemon', 'Citrus limon'),
    ('avocado', 'Persea americana'),
    ('pomegranate', 'Punica granatum'),
    ('cranberry', 'Vaccinium macrocarpon'),
    ('grapefruit', 'Citrus × paradisi'),

])
def test_valid_fruit(fruit_name, formal_name):
    assert get_formal_name(fruit_name) == formal_name

# Parametrize the test for invalid fruit names
@pytest.mark.parametrize("fruit_name", [
    'boba',
    'cucumbers',
    'durian',
    '',
    '!',

])
def test_invalid_fruit(fruit_name):
    assert get_formal_name(fruit_name) == 'Unknown'

if __name__ == "__main__":
    pytest.main()