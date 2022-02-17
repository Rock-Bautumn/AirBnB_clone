#!/usr/bin/python3
"""
This module is the unittest file for the class: User.
"""
from genericpath import exists
import unittest
from models.user import User
from models.engine.file_storage import FileStorage
import pep8
from models import storage


class TestBaseClass(unittest.TestCase):
    """
    This class is for testing User.
    """
    def setUp(self):
        """
        Setup method.
        """
        self.User1 = User()
        self.User2 = User()
        User3_dict = self.User1.to_dict()
        self.User3 = User(**User3_dict)

    def tearDown(self):
        """
        Teardown method.
        """
        del self.User1
        del self.User2
        del self.User3
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
        self.assertTrue(len(User.__doc__) >= 1)

    def test_init(self):
        """
        Tests the init method.
        """
        self.assertEqual(self.User1.email, "")
        self.assertEqual(self.User1.password, "")
        self.assertEqual(self.User1.first_name, "")
        self.assertEqual(self.User1.last_name, "")

if __name__ == "__main__":
    unittest.main()
