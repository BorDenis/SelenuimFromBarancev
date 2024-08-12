def test_remove_items_from_cart(app):
    app.add_first_item_to_cart_n_times(3)
    app.remove_all_items_in_cart()