import unittest
from cultural_destination import CulturalDestination, Talent

class TestCulturalDestination(unittest.TestCase):
    def setUp(self):
        self.cultural_destination = CulturalDestination("Test Cultural Destination", "Test Location", "Test Description")

    def test_add_talent(self):
        talent = Talent("Test Talent", "Test Talent Description")
        self.cultural_destination.add_talent(talent)
        self.assertIn(talent, self.cultural_destination.talents)

    def test_remove_talent(self):
        talent = Talent("Test Talent", "Test Talent Description")
        self.cultural_destination.add_talent(talent)
        self.cultural_destination.remove_talent(talent)
        self.assertNotIn(talent, self.cultural_destination.talents)

if __name__ == '__main__':
    unittest.main()
