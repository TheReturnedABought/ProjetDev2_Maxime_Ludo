import unittest
from Item import Item

class TestItem(unittest.TestCase):
    def setUp(self):
        # Set up various items to test
        self.sword = Item(name="Sword", damage_power=10, health_add=0, slot="main", equiped=False)
        self.helmet = Item(name="Helmet", damage_power=0, health_add=5, slot="head", equiped=False)

    def test_equip(self):
        # Test equipping an item
        self.sword.equip()
        self.assertTrue(self.sword.equiped)

    def test_equip_already_equipped(self):
        # Test equipping an already equipped item
        self.sword.equip()
        with self.assertRaises(RuntimeError):
            self.sword.equip()

    def test_equip_no_slot(self):
        # Test equipping an item with no valid slot
        item_no_slot = Item(name="Invalid", damage_power=0, health_add=0, slot=None, equiped=False)
        with self.assertRaises(RuntimeError):
            item_no_slot.equip()

    def test_unequip(self):
        # Test unequipping an item
        self.sword.equip()
        self.sword.unequip()
        self.assertFalse(self.sword.equiped)
        self.assertIsNone(self.sword.slot)

    def test_unequip_not_equipped(self):
        # Test unequipping an item that is not equipped
        with self.assertRaises(RuntimeError):
            self.sword.unequip()

if __name__ == "__main__":
    unittest.main()
