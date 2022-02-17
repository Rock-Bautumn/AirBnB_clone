#!/usr/bin/python3
"""
This module is the unittest file for the class: Place.
"""
from genericpath import exists
import unittest
from models.place import Place
from models.engine.file_storage import FileStorage
import pep8
from models import storage


class TestBaseClass(unittest.TestCase):
    """
    This class is for testing Place.
    """
    def setUp(self):
        """
        Setup method.
        """
        self.Place1 = Place()
        self.Place2 = Place()
        Place3_dict = self.Place1.to_dict()
        self.Place3 = Place(**Place3_dict)

    def tearDown(self):
        """
        Teardown method.
        """
        del self.Place1
        del self.Place2
        del self.Place3
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
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_init(self):
        """
        Tests the init method.
        """
        self.assertEqual(self.Place1.city_id, "")
        self.assertEqual(self.Place1.user_id, "")
        self.assertEqual(self.Place1.name, "")
        self.assertEqual(self.Place1.description, "")
        self.assertEqual(self.Place1.number_rooms, 0)
        self.assertEqual(self.Place1.number_bathrooms, 0)
        self.assertEqual(self.Place1.max_guest, 0)
        self.assertEqual(self.Place1.price_by_night, 0)
        self.assertEqual(self.Place1.latitude, 0.0)
        self.assertEqual(self.Place1.longitude, 0.0)
        self.assertEqual(self.Place1.amenity_ids, [])

if __name__ == "__main__":
    unittest.main()
