"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

@pytest.fixture()
def item():
    return Item('Шляпа', 500, 3)

def test_calculate_total_price(item):
    assert item.calculate_total_price() == 1500

# def test_calculate_total_price():
#     product_1 = Item('Шляпа', 500, 3)
#     assert product_1.calculate_total_price() == 1500

def test_apply_discount():
    product_2 = Item('Большая Шляпа', 1500, 2)
    Item.pay_rate = 2
    product_2.apply_discount()
    assert product_2.price == 3000

def test_string_to_number():
    p1 = Item('Product', 300, 3)
    assert p1.string_to_number('7') == 7

def test_item():
    product_3 = Item('Product', 300, 2)
    assert product_3.name == 'Product'
    assert product_3.price == 300
    assert product_3.quantity == 2

def test_setter(item):
    item.name = 'Шляпа678910'
    assert item.name == 'Шляпа67891'

path = '../src/items.csv'
def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5