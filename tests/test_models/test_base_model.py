import unittest
from datetime import datetime
from uuid import UUID
from models import storage
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_init_without_args(self):
        self.assertIsInstance(self.base_model.id, UUID)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_init_with_args(self):
        custom_data = {'name': 'Test', 'age': 30}
        model = BaseModel(**custom_data)
        self.assertEqual(model.name, 'Test')
        self.assertEqual(model.age, 30)
        self.assertIsInstance(model.id, UUID)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict(self):
        expected_dict = {
            'id': str(self.base_model.id),
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

    def test_from_dict(self):
        test_dict = {
            'id': '12345678-1234-5678-1234-567812345678',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-02T00:00:00',
            'name': 'Test User'
        }
        deserialized = BaseModel.from_dict(test_dict)
        self.assertIsInstance(deserialized, BaseModel)
        self.assertEqual(deserialized.__dict__, test_dict)

    def test_save(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_str_representation(self):
        self.assertTrue(isinstance(str(self.base_model), str))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            BaseModel(1, 2, 3)

if __name__ == '__main__':
    unittest.main()
