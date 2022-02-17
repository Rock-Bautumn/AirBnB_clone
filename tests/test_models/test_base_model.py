#!/usr/bin/python3
"""
This module is the unittest file for the class: BaseModel.
"""
from genericpath import exists
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import pep8
from models import storage


class TestBaseClass(unittest.TestCase):
    """
    This class is for testing BaseModel.
    """
    def setUp(self):
        """
        Setup method.
        """
        self.BaseModel1 = BaseModel()
        self.BaseModel2 = BaseModel()
        BaseModel3_dict = self.BaseModel1.to_dict()
        self.BaseModel3 = BaseModel(**BaseModel3_dict)

    def tearDown(self):
        """
        Teardown method.
        """
        del self.BaseModel1
        del self.BaseModel2
        del self.BaseModel3
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
        self.assertTrue(len(BaseModel.__doc__) >= 1)
        # Method docstrings
        self.assertTrue(len(BaseModel.__init__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.save.__doc__) >= 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) >= 1)

    def test_init(self):
        """
        Tests the init method.
        """
        # Test IDs
        self.assertTrue(self.BaseModel1.id, exists)
        self.assertTrue(type(self.BaseModel1.id) is str)
        self.assertNotEqual(self.BaseModel1.id, self.BaseModel2.id)
        # Test created datetime
        self.assertTrue(self.BaseModel1.created_at, exists)
        self.assertNotEqual(
            self.BaseModel1.created_at, self.BaseModel2.created_at)
        # Test updated datetime
        self.assertEqual(
            self.BaseModel1.created_at, self.BaseModel1.updated_at)
        # Test using kwargs
        self.assertEqual(self.BaseModel3.id, self.BaseModel1.id)
        self.assertEqual(
            self.BaseModel3.created_at, self.BaseModel1.created_at)
        self.assertEqual(
            self.BaseModel3.updated_at, self.BaseModel1.updated_at)
        self.assertEqual(self.BaseModel3.__class__, self.BaseModel1.__class__)

    def test_str(self):
        """
        Testing __str__.
        """
        expected_display = "[{}] ({}) {}".format(
                self.BaseModel1.__class__.__name__,
                self.BaseModel1.id,
                self.BaseModel1.__dict__)
        self.assertEqual(self.BaseModel1.__str__(), expected_display)

    def test_save(self):
        """
        Testing save.
        """
        self.BaseModel1.save()
        self.assertNotEqual(
            self.BaseModel1.created_at, self.BaseModel1.updated_at)

    def test_to_dict(self):
        """
        Testing to_dict.
        """
        BaseModel1_dict = self.BaseModel1.to_dict()
        self.assertEqual(BaseModel1_dict['__class__'], 'BaseModel')
        self.assertEqual(BaseModel1_dict['created_at'],
                         self.BaseModel1.created_at.isoformat())
        self.assertEqual(BaseModel1_dict['updated_at'],
                         self.BaseModel1.updated_at.isoformat())
        self.assertEqual(BaseModel1_dict['id'], self.BaseModel1.id)
        # test looking for attr that doesn't exist
        with self.assertRaises(AttributeError):
            getattr(self.BaseModel1, 'NonExistentKey')
        # set attr and test it
        self.BaseModel1.Job = "Code Monkey"
        self.assertTrue(self.BaseModel1.Job, exists)

if __name__ == "__main__":
    unittest.main()
