from flask import Flask, request, jsonify
from ..entrypoint import commands, unit_of_work

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to the autonomous trading bot!", 200


@app.route("/create-analyst")
def create_analyst():
    commands.create_analyst(
        "Shekhani",
        "Lumsu",
        "shekhani@lums.edu.pk",
        "+92 333 3333333",
        "strong_password",
        unit_of_work.UnitOfWork(),
    )
    return "OK", 200


@app.route("/analyst-login", methods=['POST'])
def analyst_login():
    ret = commands.analyst_login(
        request.json["email"],
        request.json["password"],
        uow=unit_of_work.UnitOfWork(),
    )
    if ret.success == True:
        return jsonify(ret), 202
    else:
        return jsonify(ret), 401


@app.route("/analyst-logout")
def analyst_logout():
    pass


@app.route("/register-investor")
def register_investor():
    pass


@app.route("/investor-login")
def investor_login():
    pass


@app.route("/investor-logout")
def investor_logout():
    pass
