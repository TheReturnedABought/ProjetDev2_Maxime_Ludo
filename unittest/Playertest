import unittest
from Player import Player


class TestPlayerInventory(unittest.TestCase):
    def setUp(self):
        self.player = Player(name="TestPlayer", health=100, attack_power=10)

    def test_add_to_inventory(self):
        self.player.add_to_inventory("Sword")
        self.assertIn("Sword", self.player.inventory)
        self.assertEqual(len(self.player.inventory), 1)

    def test_remove_from_inventory(self):
        self.player.add_to_inventory("Shield")
        self.player.remove_from_inventory("Shield")
        self.assertNotIn("Shield", self.player.inventory)
        self.assertEqual(len(self.player.inventory), 0)

    def test_remove_from_inventory_not_found(self):
        self.player.add_to_inventory("Potion")
        with self.assertRaises(ValueError):  # `remove` raises ValueError if the item is not found
            self.player.remove_from_inventory("Elixir")

    def test_get_inventory(self):
        self.player.add_to_inventory("Bow")
        self.player.add_to_inventory("Arrow")
        inventory_display = self.player.get_inventory()
        self.assertEqual(inventory_display, "Inventaire : Bow, Arrow")

    def test_get_inventory_empty(self):
        inventory_display = self.player.get_inventory()
        self.assertEqual(inventory_display, "L'inventaire est vide.")

    def test_get_inventory_invalid_type(self):
        self.player.inventory = "Not a list"
        with self.assertRaises(ValueError):
            self.player.get_inventory()


if __name__ == '__main__':
    unittest.main()
