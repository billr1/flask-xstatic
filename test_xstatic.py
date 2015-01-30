import unittest

from flask import Flask
from flask.ext.testing import TestCase
from flask.ext.xstatic import FlaskXStatic


class InitTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask('InitTestCase')

    def test_ctor_app(self):
        xs = FlaskXStatic(self.app)

    def test_init_app(self):
        xs = FlaskXStatic()
        xs.init_app(self.app)


class XStaticTestCase(TestCase):

    def create_app(self):
        return Flask('XStaticTestCase')

    def setUp(self):
        self.xs = FlaskXStatic(self.app)
        self.xs.add_module('jquery')

    def test_get(self):
        r = self.client.get('/xstatic/jquery/jquery.min.js')
        self.assert200(r)

    def test_path_for(self):
        path = self.xs.path_for('jquery')
        self.assertIn('xstatic/pkg/jquery/data', path)
