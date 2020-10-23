import unittest
from hello import app
from hello.formater import SUPPORTED

class FTestCase(unittest.TestCase):
    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data

    def test_name_output(self):
        rv = self.app.get('/formaty?name=Anna')
        op = 'Anna'
        self.assertEquals(op, rv.data.split(" ")[0])

    def test_msg_with_output_json(self):
        rv = self.app.get('/formaty?output=json')
        op = '{"imie": "Krzysiek", "msg": "Aplikacja testowa!"}'
        self.assertEquals(op, rv.data)

    def test_msg_with_output_xml(self):
        rv = self.app.get('/formaty?output=xml')
        op = '<greetings>\n  <name>Krzysiek</name>\n  <msg>Aplikacja testowa!</msg>\n</greetings>\n'
        self.assertEquals(op, rv.data)

