from flask import Flask, request
app = Flask(__name__)

def save_update(user, msg):
    """Process the incoming updates and save them to the database.
    """
    pass

def get_updates():
    output = "[{}]"
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
