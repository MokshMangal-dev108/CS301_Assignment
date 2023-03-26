import unittest
from cultural_destination import CulturalDestination, Talent

class TestRegression(unittest.TestCase):
    def test_cultural_destination_creation(self):
        # create a new cultural destination
        cultural_destination = CulturalDestination("Test Cultural Destination", "Test Location", "Test Description")

        # check if the cultural destination is created successfully
        self.assertEqual(cultural_destination.name, "Test Cultural Destination")
        self.assertEqual(cultural_destination.location, "Test Location")
        self.assertEqual(cultural_destination.description, "Test Description")
        self.assertEqual(len(cultural_destination.talents), 0)

    def test_talent_creation(self):
        # create a new talent
        talent = Talent("Test Talent", "Test Talent Description")

        # check if the talent is created successfully
        self.assertEqual(talent.name, "Test Talent")
        self.assertEqual(talent.description, "Test Talent Description")

    def test_add_talent(self):
        # create a new cultural destination
        cultural_destination = CulturalDestination("Test Cultural Destination", "Test Location", "Test Description")

        # add a new talent to the cultural destination
        talent = Talent("Test Talent", "Test Talent Description")
        cultural_destination.add_talent(talent)

        # check if the talent is added successfully
        self.assertEqual(len(cultural_destination.talents), 1)
        self.assertIn(talent, cultural_destination.talents)

    def test_remove_talent(self):
        # create a new cultural destination
        cultural_destination = CulturalDestination("Test Cultural Destination", "Test Location", "Test Description")

        # add a new talent to the cultural destination
        talent = Talent("Test Talent", "Test Talent Description")
        cultural_destination.add_talent(talent)

        # remove the talent from the cultural destination
        cultural_destination.remove_talent(talent)

        # check if the talent is removed successfully
        self.assertEqual(len(cultural_destination.talents), 0)
        self.assertNotIn(talent, cultural_destination.talents)

if __name__ == '__main__':
    unittest.main()
