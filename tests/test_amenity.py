#!/usr/bin/python3
"""
This module is the unittest file for the class: Amenity.
"""
from genericpath import exists
import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import pep8
from models import storage


class TestBaseClass(unittest.TestCase):
    """
    This class is for testing Amenity.
    """
    def setUp(self):
        """
        Setup method.
        """
        self.Amenity1 = Amenity()
        self.Amenity2 = Amenity()
        Amenity3_dict = self.Amenity1.to_dict()
        self.Amenity3 = Amenity(**Amenity3_dict)

    def tearDown(self):
        """
        Teardown method.
        """
        del self.Amenity1
        del self.Amenity2
        del self.Amenity3
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
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_init(self):
        """
        Tests the init method.
        """
        self.assertEqual(self.Amenity1.name, "")

if __name__ == "__main__":
    unittest.main()
