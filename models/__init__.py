#!/usr/bin/python3


app = Flask(__name__)

@app.route('/0-hbnb/')
def hbnb():
    cache_id = uuid.uuid4()
    return render_template('0-hbnb.html', cache_id=cache_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
"""
initialize the models package
"""

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage 
from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
from flask import Flask, render_template
import uuid
    storage = FileStorage()
storage.reload()
