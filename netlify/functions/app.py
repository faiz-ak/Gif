import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
import serverless_wsgi


def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)