from sgm.survivor import Survivor
import unittest

class TestSurvivor(unittest.TestCase):
    default_int = 0

    def test_constructs_with_health(self):
        expected_health_value = 100
        sut = Survivor(expected_health_value, self.default_int)
        self.assertEqual(expected_health_value, sut.health)

    def test_constructs_with_hunger(self):
        expected_hunger_value = 100
        sut = Survivor(self.default_int, expected_hunger_value)
        self.assertEqual(expected_hunger_value, sut.hunger)

    def test_hunger_decreases_by_10_at_end_of_day(self):
        starting_hunger = 100
        sut = Survivor(self.default_int, starting_hunger)
        sut.next_day()
        self.assertEqual(starting_hunger - 10, sut.hunger)

    def test_health_decreases_by_10_at_end_of_day_if_hunger_under_thirty(self):
        starting_health = 100
        hunger_under_thirty = 20
        sut = Survivor(starting_health, hunger_under_thirty)
        sut.next_day()
        self.assertEqual(starting_health - 10, sut.health)

if __name__ == '__main__':
    unittest.main()