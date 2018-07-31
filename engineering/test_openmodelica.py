import unittest


class TestArticleItemPage(unittest.TestCase):
    def setUp(self):
        from OMPython import OMCSessionZMQ
        self.session = OMCSessionZMQ()

    def test_open_modelica_session(self):
        self.assertIn("OpenModelica", self.session.sendExpression("getVersion()"))




