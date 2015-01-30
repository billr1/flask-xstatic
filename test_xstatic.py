from flask import Flask
from flask.ext.testing import TestCase
from flask.ext.xstatic import FlaskXStatic


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
