import unittest
from cultural_destination import CulturalDestination, Talent

class TestTextAnalytics(unittest.TestCase):
    def test_cultural_destination_description(self):
        # create a new cultural destination
        cultural_destination = CulturalDestination("Test Cultural Destination", "Test Location", "This is a test cultural destination that celebrates the heritage of India and provides a platform for emerging talents using digital technology solutions.")

        # check if the cultural destination description is analyzed correctly
        self.assertEqual(cultural_destination.description_word_count(), 19)
        self.assertEqual(cultural_destination.description_character_count(), 104)
        self.assertEqual(cultural_destination.description_sentiment(), "Positive")

    def test_talent_description(self):
        # create a new talent
        talent = Talent("Test Talent", "This is a test talent description that showcases the skills and abilities of an emerging artist.")

        # check if the talent description is analyzed correctly
        self.assertEqual(talent.description_word_count(), 14)
        self.assertEqual(talent.description_character_count(), 79)
        self.assertEqual(talent.description_sentiment(), "Positive")

if __name__ == '__main__':
    unittest.main()
