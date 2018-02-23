import requests
import argparse
import pytest

@pytest.fixture
def test_app(host, appname, port=None):
    return requests.get('http://{}:{}'.format(host, port)).content == ('Hello World from {}!'.format(appname))

def create_parser():
    parser = argparse.ArgumentParser(
        description='Assert the content returned by an app'
    )
    parser.add_argument(
        '-p', '--port', type=str, required=False,
        help='Port the app runs on'
    )
    parser.add_argument(
        '-H', '--host', type=str, required=True,
        help='Host the app runs on'
    )
    parser.add_argument(
        '-a', '--appname', type=str, required=True,
        help='The app name'
    )
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    test_app(args.host, args.appname, args.port)

if __name__ == '__main__':
    main()
