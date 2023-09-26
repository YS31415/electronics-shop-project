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