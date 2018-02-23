from test_output import create_parser, test_app
from unittest import TestCase

class CommandLineCase(TestCase):
    """
    Base TestCase class, sets up a CLI parser
    """
    @classmethod
    def setUpClass(cls):
        parser = create_parser()
        cls.parser = parser

class TestAppCase(CommandLineCase):
    def testing_app1(self):
        """
        Test the output from app1
        """
        args = self.parser.parse_args(['-H', '127.0.0.1', '-a', 'app1', '-p', '8888'])
        result = test_app(args.host, args.appname, args.port)
        self.assertTrue(result)

    def testing_app2(self):
        """
        Test the output from app1
        """
        args = self.parser.parse_args(['-H', '127.0.0.1', '-a', 'app2', '-p', '8889'])
        result = test_app(args.host, args.appname, args.port)
        self.assertTrue(result)
