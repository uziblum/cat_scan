import unittest
from run import fetchSingleBreed

class TestSingleBreed(unittest.TestCase):

    def test_id_parsed_ok(self):
        item_dict = {'weight': {'imperial': '6 - 15', 'metric': '3 - 7'}, 'id': 'char', 'name': 'Chartreux', 'cfa_url': 'http://cfa.org/Breeds/BreedsCJ/Chartreux.aspx', 'vetstreet_url': 'http://www.vetstreet.com/cats/chartreux', 'vcahospitals_url': 'https://vcahospitals.com/know-your-pet/cat-breeds/chartreux', 'temperament': 'Affectionate, Loyal, Intelligent, Social, Lively, Playful', 'origin': 'France', 'country_codes': 'FR', 'country_code': 'FR', 'description': 'The Chartreux is generally silent but communicative. Short play sessions, mixed with naps and meals are their perfect day. Whilst appreciating any attention you give them, they are not demanding, content instead to follow you around devotedly, sleep on your bed and snuggle with you if you’re not feeling well.', 'life_span': '12 - 15', 'indoor': 0, 'lap': 1, 'alt_names': '', 'adaptability': 5, 'affection_level': 5, 'child_friendly': 4, 'dog_friendly': 5, 'energy_level': 2, 'grooming': 1, 'health_issues': 2, 'intelligence': 4, 'shedding_level': 3, 'social_needs': 5, 'stranger_friendly': 5, 'vocalisation': 1, 'experimental': 0, 'hairless': 0, 'natural': 0, 'rare': 0, 'rex': 1, 'suppressed_tail': 0, 'short_legs': 0, 'wikipedia_url': 'https://en.wikipedia.org/wiki/Chartreux', 'hypoallergenic': 1}
        result_list = fetchSingleBreed(item_dict)
        self.assertEqual(result_list[0], "char", "Should be char")

    def test_name_parsed_ok(self):
        item_dict = {'weight': {'imperial': '6 - 15', 'metric': '3 - 7'}, 'id': 'char', 'name': 'Chartreux', 'cfa_url': 'http://cfa.org/Breeds/BreedsCJ/Chartreux.aspx', 'vetstreet_url': 'http://www.vetstreet.com/cats/chartreux', 'vcahospitals_url': 'https://vcahospitals.com/know-your-pet/cat-breeds/chartreux', 'temperament': 'Affectionate, Loyal, Intelligent, Social, Lively, Playful', 'origin': 'France', 'country_codes': 'FR', 'country_code': 'FR', 'description': 'The Chartreux is generally silent but communicative. Short play sessions, mixed with naps and meals are their perfect day. Whilst appreciating any attention you give them, they are not demanding, content instead to follow you around devotedly, sleep on your bed and snuggle with you if you’re not feeling well.', 'life_span': '12 - 15', 'indoor': 0, 'lap': 1, 'alt_names': '', 'adaptability': 5, 'affection_level': 5, 'child_friendly': 4, 'dog_friendly': 5, 'energy_level': 2, 'grooming': 1, 'health_issues': 2, 'intelligence': 4, 'shedding_level': 3, 'social_needs': 5, 'stranger_friendly': 5, 'vocalisation': 1, 'experimental': 0, 'hairless': 0, 'natural': 0, 'rare': 0, 'rex': 1, 'suppressed_tail': 0, 'short_legs': 0, 'wikipedia_url': 'https://en.wikipedia.org/wiki/Chartreux', 'hypoallergenic': 1}
        result_list = fetchSingleBreed(item_dict)
        self.assertEqual(result_list[1], "Chartreux", "Should be Chartreux")

if __name__ == '__main__':
    unittest.main()