import http
from datetime import datetime, timedelta
import unittest
from department_app import app, db
from department_app import service
from config import Config, TestingConfig
from department_app.models import Department, Employee


class BaseCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config.from_object(TestingConfig)
        self.client = app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
