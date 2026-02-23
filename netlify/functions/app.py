import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
from serverless_wsgi import handle


def handler(event, context):
    return handle(app, event, context)