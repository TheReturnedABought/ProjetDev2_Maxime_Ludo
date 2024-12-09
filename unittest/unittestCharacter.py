import unittest
from unittest.mock import patch
from Character import Character


class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character(name="Hero", health=10, attack_power=5)
        self.target = Character(name="Enemy", health=10, attack_power=3)

    def test_deal_attack(self):
        with patch('random.randint', return_value=3):
            self.character.deal_attack(self.target)
            self.assertEqual(self.target.health, 7)
            self.assertTrue(self.target.is_alive())

    def test_is_alive(self):
        self.assertTrue(self.character.is_alive())
        self.character.health = 0
        self.assertFalse(self.character.is_alive())

    def test_heal(self):
        self.character.health = 5
        self.character.heal(3)
        self.assertEqual(self.character.health, 8)

    def test_heal_full_health(self):
        self.character.health = 10
        self.character.heal(5)
        self.assertEqual(self.character.health, 15)

    def test_heal_dead_character(self):
        self.character.health = 0
        self.character.heal(5)
        self.assertEqual(self.character.health, 0)

    def test_take_damage(self):
        self.character.take_damage(3)
        self.assertEqual(self.character.health, 7)

    def test_take_damage_lethal(self):
        self.character.take_damage(15)
        self.assertEqual(self.character.health, -5)
        self.assertFalse(self.character.is_alive())

    def test_apply_status_effects(self):
        self.character.apply_status_effects("poisoned")
        self.assertIn("poisoned", self.character.status_effects)

    def test_remove_status_effects(self):
        self.character.apply_status_effects("poisoned")
        self.character.remove_status_effects("poisoned")
        self.assertNotIn("poisoned", self.character.status_effects)

    def test_remove_nonexistent_status_effect(self):
        self.character.remove_status_effects("stunned")
        self.assertNotIn("stunned", self.character.status_effects)

if __name__ == '__main__':
    unittest.main()
