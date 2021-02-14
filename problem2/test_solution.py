import unittest
import solution


class TestSolution(unittest.TestCase):
    def test_afficher_les_3_premiers(self):

        # Given
        runners = [
            {
                'name': "Asafa Poel",
                'speed': 22.3,
                'endurance': 5
            },
            {
                'name': "George Pat",
                'speed': 20.3,
                'endurance': 5
            },
            {
                'name': "Jeremy Garett",
                'speed': 22.4,
                'endurance': 3
            },
            {
                'name': "Kent James",
                'speed': 21.5,
                'endurance': 6
            },
            {
                'name': "Derrick Jones",
                'speed': 24.8,
                'endurance': 2
            }

        ]

        # When
        speeds = solution.evaluate_rank(runners)
        # Then
        self.assertIs(type(runners), list)

        self.assertEqual(speeds, [24.8, 22.4, 22.3])

    def test_afficher_None_quand_runners_est_vide(self):
        runners = []

        self.assertTrue(not runners)

    def test_evaluer_nombre_victoire_de_chaque_atheletes(self):
        pass


if __name__ == "__main__":
    unittest.main()
