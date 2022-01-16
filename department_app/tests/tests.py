"""

"""
from datetime import datetime, timedelta
import unittest
from department_app import app, db
from config import Config, TestingConfig
# from department_app.models import Department, Employee

# client = app.test_client()


class BaseCase(unittest.TestCase):
    """

    """
    def setUp(self):
        """
        Execute before every test case
        :return:
        """
        app.config.from_object(TestingConfig)
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        """
        Execute after every test case
        :return:
        """
        db.session.remove()
        db.drop_all()

    def test_department_add(self):
        res = self.client.get('/departments')

        assert res.status_code == 200
