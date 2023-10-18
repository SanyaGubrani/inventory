from project import add_item, delete_item, search_item, clear_inventory

def test_add_item(tmp_path):
    """Test for the add_item function by adding
       an item to the inventory."""
    inventory_file = tmp_path / "test_inventory.data"
    item_name = "Test Item"
    item_qty = 5

    add_item(inventory_file, item_name, item_qty)

    with open(inventory_file, 'r') as f:
        lines = f.readlines()
        assert item_name + '\n' in lines
        assert str(item_qty) + '\n' in lines


def test_delete_item(tmp_path):
    """Test for the delete_item function by deleting
       an item from the inventory."""
    inventory_file = tmp_path / "test_inventory.data"
    item_name = "Item2"

    with open(inventory_file, 'w') as f:
        f.write("Item1\n5\nItem2\n10\nItem3\n3\n")

    delete_item(inventory_file, item_name)

    with open(inventory_file, 'r') as f:
        lines = f.readlines()
        assert item_name + '\n' not in lines
        assert "10\n" not in lines


def test_search_item(tmp_path, capsys):
    """Test for the search_item function by searching
       for an item in the inventory."""
    inventory_file = tmp_path / "test_inventory.data"
    item_name = "Item2"

    with open(inventory_file, 'w') as f:
        f.write("Item1\n5\nItem2\n10\nItem3\n3\n")

    search_item(inventory_file, item_name)

    captured = capsys.readouterr()
    assert "Item" in captured.out
    assert "Quantity" in captured.out



def test_clear_inventory(tmp_path, capsys):
    """Test for the clear_inventory function by clearing
       all items from the inventory."""
    inventory_file = tmp_path / "test_inventory.data"

    with open(inventory_file, 'w') as f:
        f.write("Item1\n5\nItem2\n10\nItem3\n3\n")

    clear_inventory(inventory_file)

    captured = capsys.readouterr()
    assert "All items have been deleted from the inventory." in captured.out

    with open(inventory_file, 'r') as f:
        assert not f.read()