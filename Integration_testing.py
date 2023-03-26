import unittest
from cultural_destination import CulturalDestination, Talent

class TestIntegration(unittest.TestCase):
    def test_cultural_destination_with_talents(self):
        # create a new cultural destination
        cultural_destination = CulturalDestination("Test Cultural Destination", "Test Location", "Test Description")

        # add some talents
        talent1 = Talent("Talent 1", "Test Talent 1")
        talent2 = Talent("Talent 2", "Test Talent 2")
        cultural_destination.add_talent(talent1)
        cultural_destination.add_talent(talent2)

        # check if the talents are added successfully
        self.assertEqual(len(cultural_destination.talents), 2)
        self.assertIn(talent1, cultural_destination.talents)
        self.assertIn(talent2, cultural_destination.talents)

        # remove one talent and check if it is removed successfully
        cultural_destination.remove_talent(talent1)
        self.assertEqual(len(cultural_destination.talents), 1)
        self.assertNotIn(talent1, cultural_destination.talents)
        self.assertIn(talent2, cultural_destination.talents)

        # add a new talent and check if it is added successfully
        talent3 = Talent("Talent 3", "Test Talent 3")
        cultural_destination.add_talent(talent3)
        self.assertEqual(len(cultural_destination.talents), 2)
        self.assertIn(talent2, cultural_destination.talents)
        self.assertIn(talent3, cultural_destination.talents)

if __name__ == '__main__':
    unittest.main()

