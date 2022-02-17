#!/usr/bin/python3
"""
This module is the unittest file for the class: City.
"""
from genericpath import exists
import unittest
from models.city import City
from models.engine.file_storage import FileStorage
import pep8
from models import storage


class TestBaseClass(unittest.TestCase):
    """
    This class is for testing City.
    """
    def setUp(self):
        """
        Setup method.
        """
        self.City1 = City()
        self.City2 = City()
        City3_dict = self.City1.to_dict()
        self.City3 = City(**City3_dict)

    def tearDown(self):
        """
        Teardown method.
        """
        del self.City1
        del self.City2
        del self.City3
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
        self.assertTrue(len(City.__doc__) >= 1)

    def test_init(self):
        """
        Tests the init method.
        """
        self.assertEqual(self.City1.name, "")
        self.assertEqual(self.City1.state_id, "")

if __name__ == "__main__":
    unittest.main()
