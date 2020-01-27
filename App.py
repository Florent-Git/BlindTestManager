from flask import Flask, render_template
from pprint import pprint
from controller import HomeController, Controller

app = Flask(__name__, static_folder='static', template_folder='views')


@app.route("/")
def hello_world():
    controller = HomeController("Hello")
    return control_template("login_view.html", controller=controller)


def control_template(view, controller=None):

    return render_template(view, **controller.__dict__)


if __name__ == "__main__":
    app.run(debug=True)
