from flask_testing import TestCase
from dummyAPI.app import app


class DummyApiUnitTest(TestCase):

    def create_app(self):
        return app

    @classmethod
    def setUpClass(cls):

        cls.headers = {
            'Accept': 'application/json',
            's-Type': 'application/json'
        }