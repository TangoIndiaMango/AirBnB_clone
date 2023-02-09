import unittest
from datetime import datetime
from uuid import uuid4

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_init(self):
        self.assertEqual(type(self.base_model.id), str)
        self.assertEqual(type(self.base_model.created_at), datetime)
        self.assertEqual(type(self.base_model.updated_at), datetime)

    def test_str(self):
        self.assertEqual(str(self.base_model), f'[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}')

    def test_save(self):
        updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        self.assertEqual(type(self.base_model.to_dict()), dict)
        self.assertEqual(self.base_model.to_dict()['__class__'], 'BaseModel')
        self.assertEqual(type(self.base_model.to_dict()['created_at']), str)
        self.assertEqual(type(self.base_model.to_dict()['updated_at']), str)


