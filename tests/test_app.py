from flask_testing import TestCase
from flask import current_app
from app import app


class PositionTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_app_exist(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
