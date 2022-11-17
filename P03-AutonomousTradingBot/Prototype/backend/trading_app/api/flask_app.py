from flask import Flask, request, jsonify
from ..entrypoint import commands, unit_of_work

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to the autonomous trading bot!", 200


@app.route("/create-analyst")
def create_analyst():
    commands.create_analyst(
        request.json["name"],
        request.json["address"],
        request.json["email"],
        request.json["phone_number"],
        request.json["password"],
        unit_of_work.UnitOfWork(),
    )
    return "OK", 200


@app.route("/analyst-login")
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
    commands.analyst_logout(
        request.json["email"],
        uow=unit_of_work.UnitOfWork(),
    )
    return "OK", 200


@app.route("/register-investor")
def register_investor():
    ret = commands.register_investor(
        request.json["name"],
        request.json["address"],
        request.json["investor_email"],
        request.json["phone_number"],
        request.json["password"],
        request.json["analyst_email"],
        unit_of_work.UnitOfWork(),
    )
    return jsonify(ret), 200


@app.route("/investor-login")
def investor_login():
    ret = commands.investor_login(
        request.json["email"],
        request.json["password"],
        uow=unit_of_work.UnitOfWork(),
    )
    if ret.success == True:
        return jsonify(ret), 202
    else:
        return jsonify(ret), 401


@app.route("/investor-logout")
def investor_logout():
    commands.investor_logout(
        request.json["email"],
        uow=unit_of_work.UnitOfWork(),
    )
    return "OK", 200
