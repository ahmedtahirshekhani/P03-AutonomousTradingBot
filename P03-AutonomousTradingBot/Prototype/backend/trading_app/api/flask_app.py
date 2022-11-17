from flask import Flask, request, jsonify
from ..entrypoint import commands, unit_of_work

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to the autonomous trading bot!", 200


@app.route("/create-analyst", methods=["POST"])
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


@app.route("/analyst-login", methods=["POST"])
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


@app.route("/analyst-logout", methods=["POST"])
def analyst_logout():
    commands.analyst_logout(
        request.json["email"],
        uow=unit_of_work.UnitOfWork(),
    )
    return "OK", 200


@app.route("/register-investor", methods=["POST"])
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


@app.route("/investor-login", methods=["POST"])
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


@app.route("/investor-logout", methods=["POST"])
def investor_logout():
    commands.investor_logout(
        request.json["email"],
        uow=unit_of_work.UnitOfWork(),
    )
    return "OK", 200


"""
Bot module
"""


@app.route("/add-bot", methods=["POST"])
def add_bot():
    commands.add_bot(
        request.json["analyst_id"],
        request.json["investor_id"],
        request.json["state"],
        request.json["trades"],
        request.json["assigned_model"],
        request.json["risk_appetite"],
        request.json["target_return"],
        request.json["duration"],
        uow=unit_of_work.UnitOfWork(),
    )
    return "OK", 200


@app.route("/initiate-bot-execution", methods=["POST"])
def initiate_bot_execution():
    commands.initiate_bot_execution(
        request.json["bot_id"],
        uow=unit_of_work.UnitOfWork(),
    )
    return "OK", 200


@app.route("/terminate-bot", methods=["POST"])
def terminate_bot():
    commands.terminate_bot(
        request.json["bot_id"],
        uow=unit_of_work.UnitOfWork(),
    )
    return "OK", 200
