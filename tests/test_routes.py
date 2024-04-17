import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(current_dir, '..')
sys.path.append(app_dir)

# flake8: noqa: E402
from app import create_app, db
from app.models import Data


class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_insert_data(self):
        with self.app.app_context():
            # Insertar datos
            response = self.client.post('/data', json={"name": "test"})
            self.assertEqual(response.status_code, 200)
            data = Data.query.filter_by(name="test").first()
            self.assertIsNotNone(data)

    def test_get_all_data(self):
        with self.app.app_context():
            # Obtener todos los datos
            response = self.client.get('/data')
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json, list)

    def test_delete_data(self):
        with self.app.app_context():
            # Insertar datos para borrar
            data = Data(name="test")
            db.session.add(data)
            db.session.commit()
            # Borrar datos
            response = self.client.delete(f'/data/{data.id}')
            self.assertEqual(response.status_code, 200)
            deleted_data = db.session.get(Data, data.id)
            self.assertIsNone(deleted_data)


if __name__ == '__main__':
    unittest.main()