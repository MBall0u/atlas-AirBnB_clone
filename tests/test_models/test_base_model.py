import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.id, uuid.UUID)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {{id: {}, created_at\
                        : {}, updated_at: {} }}".format(model.id, model.id,\
                         model.created_at.isoformat(), model.updated_at.isoformat())
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict_method(self):
        model = BaseModel()
        dict_repr = model.to_dict()
        self.assertIn('id', dict_repr)
        self.assertIn('created_at', dict_repr)
        self.assertIn('updated_at', dict_repr)
        self.assertIn('__class__', dict_repr)
        self.assertEqual(dict_repr['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
