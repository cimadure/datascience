import unittest


class TestModelicaIntegration(unittest.TestCase):

    def setUp(self):
        from OMPython import OMCSessionZMQ
        self.session = OMCSessionZMQ()

    def test_open_modelica_session(self):
        self.assertIn("OpenModelica", self.session.sendExpression("getVersion()"))

    def test_load_model(self):
        self.session.sendExpression("loadModel(Modelica)")
        self.session.sendExpression(r'loadFile("BouncingBall.mo")')

    def test_initiate_model(self):
        self.session.sendExpression("loadModel(Modelica)")
        self.session.sendExpression(r'loadFile("BouncingBall.mo")')
        self.session.sendExpression("instantiateModel(BouncingBall)")
        self.assertIn('BouncingBall', self.session.sendExpression("getClassNames()"))
        self.assertIn('Modelica', self.session.sendExpression("getClassNames()"))
