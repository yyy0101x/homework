import pytest
from cart import ShoppingCart

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50, 2)
    assert cart._items["Apple"]["quantity"] == 2

def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50, 2)
    cart.remove_item("Apple")
    assert "Apple" not in cart._items

def test_apply_discount_and_total():
    cart = ShoppingCart()
    cart.add_item("Shoes", 100.0, 1)
    cart.apply_discount("SAVE20")
    # Note: The buggy cart.py might fail this test!
    assert cart.get_total() == 80.0

def test_clear_cart():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50, 2)
    cart.clear()
    assert len(cart._items) == 0