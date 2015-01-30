from flask import Flask
from flask.ext.testing import TestCase
from flask.ext.xstatic import FlaskXStatic


class XStaticTestCase(TestCase):

    def create_app(self):
        return Flask('XStaticTestCase')

    def test_use_jquery(self):
        xs = FlaskXStatic(self.app)
        xs.add_module('jquery')
        r = self.client.get('/xstatic/jquery/jquery.min.js')
        self.assert200(r)
