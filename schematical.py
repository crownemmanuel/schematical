from __future__ import with_statement
import sqlite3
import json
from contextlib import closing
from flask import Flask, request, g

app = Flask(__name__)

DATABASE = '/tmp/flaskr.db'

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()



def save_update(user, msg):
    """Process the incoming updates and save them to the database.
    """
    g.db.execute('insert into updates (user, msg) values (?, ?)',
                 [user, msg])
    g.db.commit()


def get_updates():
    cur = g.db.execute('select user, msg from updates')
    entries = [dict(user=row[0], msg=row[1]) for row in cur.fetchall()]
    output = json.dumps(entries)
    return output


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/updates",  methods=['POST', 'GET'])
def updates():
    if request.method == 'POST':
        user = request.form['user']
        msg = request.form['msg']
        save_update(user, msg)
        return "" + user + ": " + msg, 201
    elif request.method == 'GET':
        return get_updates()

if __name__ == "__main__":
    app.run()
