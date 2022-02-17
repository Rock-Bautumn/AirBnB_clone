#!/usr/bin/python3
"""
This module is the unittest file for the class: Review.
"""
from genericpath import exists
import unittest
from models.review import Review
from models.engine.file_storage import FileStorage
import pep8
from models import storage


class TestBaseClass(unittest.TestCase):
    """
    This class is for testing Review.
    """
    def setUp(self):
        """
        Setup method.
        """
        self.Review1 = Review()
        self.Review2 = Review()
        Review3_dict = self.Review1.to_dict()
        self.Review3 = Review(**Review3_dict)

    def tearDown(self):
        """
        Teardown method.
        """
        del self.Review1
        del self.Review2
        del self.Review3
        storage.save()

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        # Class docstring
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_init(self):
        """
        Tests the init method.
        """
        self.assertEqual(self.Review1.place_id, "")
        self.assertEqual(self.Review1.user_id, "")
        self.assertEqual(self.Review1.text, "")

if __name__ == "__main__":
    unittest.main()
