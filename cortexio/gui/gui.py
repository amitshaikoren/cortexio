import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("index.html")

@app.route("/user_page/<id>")
def user_page(id):


@app.route("/404_user_not_found")
def user_not_found():
    return flask.render_template("404")