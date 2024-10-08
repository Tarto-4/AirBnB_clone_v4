#!/usr/bin/python3
"""Initialize Flask app and register blueprints"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """Close storage"""
    storage.close()

if __name__ == "__main__":
    from os import getenv
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
