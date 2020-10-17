import flask
import os
from cortexio import DEFAULT_API_URL, DEFAULT_GUI_URL

url_of_api = DEFAULT_API_URL
url_of_gui = DEFAULT_GUI_URL

app = flask.Flask(__name__)


def run_gui_server(host, port, api_url):
    global url_of_api
    global url_of_gui
    url_of_api = api_url
    url_of_gui = f'http://{host}:{port}'

    app.run(host=host, port=port)


@app.route("/")
def home():
    return flask.render_template("index.html", api_url=url_of_api, gui_url=url_of_gui)


@app.route("/user_page/<user_id>")
def user_page(user_id):
    return flask.render_template("user_page.html", api_url=url_of_api, user_id=user_id)


@app.route("/404_user_not_found")
def user_not_found():
    return flask.render_template("404.html")


@app.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    run_gui_server("0.0.0.0", 9000, DEFAULT_API_URL)
