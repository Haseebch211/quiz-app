import unittest
from quiz_utils import check_answer

class TestPakistanQuiz(unittest.TestCase):
    def test_independence_day(self):
        try:
            self.assertTrue(check_answer("August 14, 1947", "August 14, 1947"))
        except Exception as e:
            self.fail(f"Exception raised in test_independence_day: {e}")

    def test_first_governor_general(self):
        try:
            self.assertTrue(check_answer("Muhammad Ali Jinnah", "Muhammad Ali Jinnah"))
        except Exception as e:
            self.fail(f"Exception raised in test_first_governor_general: {e}")

    def test_national_language(self):
        try:
            self.assertTrue(check_answer("Urdu", "Urdu"))
        except Exception as e:
            self.fail(f"Exception raised in test_national_language: {e}")

    def test_mountain_range(self):
        try:
            self.assertTrue(check_answer("Himalayas", "Himalayas"))
        except Exception as e:
            self.fail(f"Exception raised in test_mountain_range: {e}")

    def test_largest_province(self):
        try:
            self.assertTrue(check_answer("Balochistan", "Balochistan"))
        except Exception as e:
            self.fail(f"Exception raised in test_largest_province: {e}")

    def test_national_anthem_writer(self):
        try:
            self.assertTrue(check_answer("Hafeez Jalandhari", "Hafeez Jalandhari"))
        except Exception as e:
            self.fail(f"Exception raised in test_national_anthem_writer: {e}")

    def test_lahore_resolution_year(self):
        try:
            self.assertTrue(check_answer("1940", "1940"))
        except Exception as e:
            self.fail(f"Exception raised in test_lahore_resolution_year: {e}")

    def test_capital_city(self):
        try:
            self.assertTrue(check_answer("Islamabad", "Islamabad"))
        except Exception as e:
            self.fail(f"Exception raised in test_capital_city: {e}")

    def test_desert_in_sindh(self):
        try:
            self.assertTrue(check_answer("Thar Desert", "Thar Desert"))
        except Exception as e:
            self.fail(f"Exception raised in test_desert_in_sindh: {e}")

    def test_national_animal(self):
        try:
            self.assertTrue(check_answer("Markhor", "Markhor"))
        except Exception as e:
            self.fail(f"Exception raised in test_national_animal: {e}")

if __name__ == '__main__':
    unittest.main()
