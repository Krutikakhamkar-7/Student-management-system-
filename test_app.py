
import unittest
from app import validate_email, validate_student


class TestStudentValidation(unittest.TestCase):

    def test_valid_student(self):
        self.assertTrue(
            validate_student("Rahul", 20, "rahul@example.com")
        )

    def test_empty_name(self):
        self.assertFalse(
            validate_student("", 20, "rahul@example.com")
        )

    def test_invalid_age(self):
        self.assertFalse(
            validate_student("Rahul", -1, "rahul@example.com")
        )

    def test_invalid_email(self):
        self.assertFalse(validate_email("invalid-email"))

    def test_valid_email(self):
        self.assertTrue(validate_email("rahul@example.com"))

    def test_email_with_spaces(self):
        self.assertFalse(validate_email("rahul @example.com"))


if __name__ == "__main__":
    unittest.main()
