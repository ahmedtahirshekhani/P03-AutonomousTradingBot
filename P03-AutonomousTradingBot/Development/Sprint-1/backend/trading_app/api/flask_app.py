import datetime
from flask import Flask, request, jsonify
from ..entrypoint import commands, unit_of_work, queries
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity


app = Flask(__name__)
app.config["JWT_SECRET_KEY"]= "super-secret"
jwt = JWTManager(app)
prefix = "/api/v1"

@app.route(prefix)
def hello():
    return "Welcome to the autonomous trading bot!", 200


@app.route(prefix+"/create-analyst", methods=["POST"])
def create_analyst():
    try:
        commands.create_analyst(
            request.json["name"],
            request.json["address"],
            request.json["email"],
            request.json["phone_number"],
            request.json["password"],
            unit_of_work.UnitOfWork(),
        )
        responseData = {"success": True, "message": "Analyst created successfully!"}
        return jsonify(responseData), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 400
    


@app.route(prefix+"/auth/login", methods=["POST"])
def login():
    email = request.json["email"]
    password = request.json["password"]
    ret = {}
    try:
        ret = commands.analyst_login(
            email,
            password,
            uow=unit_of_work.UnitOfWork(),
        )
        
    except Exception as e:
        try:
            ret = commands.investor_login(
                email,
                password,
                uow=unit_of_work.UnitOfWork(),
            )
        except Exception as e:
            return jsonify({"success": False, "message": str(e)}), 401

    # expires in 1hr
    access_token = create_access_token(identity=email, expires_delta=datetime.timedelta(hours=1))
    retObj = ret.__dict__
    retObj["access_token"] = access_token
    retObj["token_type"] = "bearer"
    retObj["expires_in"] = 3600
    
    return jsonify(retObj), 200




@app.route(prefix+"/analyst-login", methods=["POST"])
def analyst_login():
    email = request.json["email"]
    password = request.json["password"]
    try:
        ret = commands.analyst_login(
            email,
            password,
            uow=unit_of_work.UnitOfWork(),
        )
        # expires in 1hr
        access_token = create_access_token(identity=email, expires_delta=datetime.timedelta(hours=1))
        retObj = ret.__dict__
        retObj["access_token"] = access_token
        retObj["token_type"] = "bearer"
        retObj["expires_in"] = 3600
        
        return jsonify(retObj), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 401


@app.route(prefix+"/analyst-logout", methods=["POST"])
@jwt_required()
def analyst_logout():
    email = get_jwt_identity()
    
    commands.analyst_logout(
        email,
        uow=unit_of_work.UnitOfWork(),
    )
    retObj = {"success": True, "message": "Analyst logged out successfully!"}
    return jsonify(retObj), 200


@app.route(prefix+"/register-investor", methods=["POST"])
@jwt_required()
def register_investor():
    try:
        ret = commands.register_investor(
            request.json["name"],
            request.json["address"],
            request.json["investor_email"],
            request.json["phone_number"],
            request.json["analyst_email"],
            unit_of_work.UnitOfWork(),
        )
        return jsonify(ret), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 400


@app.route(prefix + "/investor-login", methods=["POST"])
def investor_login():
    email = request.json["email"]
    try:
        ret = commands.investor_login(
            email,
            request.json["password"],
            uow=unit_of_work.UnitOfWork(),
        )
        access_token = create_access_token(identity=email, expires_delta=datetime.timedelta(hours=1))
        retObj = ret.__dict__
        retObj["access_token"] = access_token
        retObj["token_type"] = "bearer"
        retObj["expires_in"] = 3600
        return jsonify(retObj), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 401


@app.route(prefix + "/investor-logout", methods=["POST"])
@jwt_required()
def investor_logout():
    email = get_jwt_identity()
    commands.investor_logout(
        email,
        uow=unit_of_work.UnitOfWork(),
    )
    retObj = {"success": True, "message": "Investor logged out successfully!"}
    return jsonify(retObj), 200


# """
# Bot module
# """


@app.route(prefix + "/add-bot", methods=["POST"])
@jwt_required()
def add_bot():
    analyst_email = get_jwt_identity()
    # get analyst id   
    analyst = commands.get_analyst(analyst_email, uow=unit_of_work.UnitOfWork()) 
    analyst_id = analyst.id

    commands.add_bot(
        analyst_id,
        request.json["investor_id"],
        request.json["trades"],
        request.json["assigned_model"],
        request.json["risk_appetite"],
        request.json["target_return"],
        request.json["duration"],
        uow=unit_of_work.UnitOfWork(),
    )

    retObj = {"success": True, "message": "Bot added successfully!"}
    return jsonify(retObj), 200


@app.route(prefix + "/get-bots", methods=["GET"])
@jwt_required()
def get_bots():
    analyst_email = get_jwt_identity()
    analyst = commands.get_analyst(analyst_email, uow=unit_of_work.UnitOfWork())
    analyst_id = analyst.id
    investor_id = request.json["investor_id"]
    bots = queries.view_all_bots(analyst_id, investor_id, uow=unit_of_work.UnitOfWork())
    retObj = {"success": True, "bots": bots, "message": "Bots fetched successfully!"}
    return jsonify(retObj), 200

@app.route(prefix + "/initiate-bot-execution", methods=["PUT"])
def initiate_bot_execution():
    try:
        commands.initiate_bot_execution(
        request.json["bot_id"],
        uow=unit_of_work.UnitOfWork(),
    )
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 400
    return jsonify({"success": True, "message": "Bot execution initiated successfully!"}), 200


@app.route(prefix + "/terminate-bot", methods=["PUT"])
def terminate_bot():
    try:
        commands.terminate_bot(
        request.json["bot_id"],
        uow=unit_of_work.UnitOfWork(),
    )
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 400
    return jsonify({"success": True, "message": "Bot execution terminated successfully!"}), 200


@app.route(prefix + "/handle-execution", methods=["PUT"])
def handle_execution():
    try:
        bots = commands.handle_execution(uow=unit_of_work.UnitOfWork())
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 400

    return jsonify({"success": True, "message": "Bot execution handled successfully!", "bots":bots}), 200
    