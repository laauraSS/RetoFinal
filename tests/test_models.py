import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(current_dir, '..')
sys.path.append(app_dir)

from app import create_app, db
from app.models import Data


class TestModels(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_data_model(self):
        with self.app.app_context():
            data = Data(name="test")
            db.session.add(data)
            db.session.commit()
            # Verificar si el objeto se ha guardado en la base de datos
            retrieved_data = Data.query.filter_by(name="test").first()
            self.assertIsNotNone(retrieved_data)
            self.assertEqual(retrieved_data.name, "test")


if __name__ == '__main__':
    unittest.main()
