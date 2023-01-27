import datetime
from flask import Flask, request, jsonify
from ..entrypoint import commands, unit_of_work, queries
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
)
import numpy as np
import pandas as pd
import keras
import sklearn
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from keras.utils import to_categorical
from .utils import successMessage, errorMessage

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)
prefix = "/api/v1"


@app.route(prefix)
def hello():
    return "Welcome to the autonomous trading bot!", 200


@app.route(prefix + "/create-analyst", methods=["POST"])
def create_analyst():
    if request.json is None:
        msg = "payload missing in request"
        return jsonify({"success": False, "message": msg}), 400

    try:
        commands.create_analyst(
            request.json["name"],
            request.json["address"],
            request.json["email"],
            request.json["phone_number"],
            request.json["password"],
            unit_of_work.UnitOfWork(),
        )
        ret_obj = {"success": True, "message": "Analyst created successfully!"}
        return jsonify(ret_obj), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 400


@app.route(prefix + "/register-investor", methods=["POST"])
@jwt_required()
def register_investor():
    email = get_jwt_identity()
    if request.json is None:
        msg = "payload missing in request"
        return jsonify({"success": False, "message": msg}), 400

    try:
        ret = commands.register_investor(
            request.json["name"],
            request.json["address"],
            request.json["investor_email"],
            request.json["phone_number"],
            email,
            unit_of_work.UnitOfWork(),
        )
        return jsonify(ret), 200
    except Exception as e:
        ret_obj = {"success": False, "message": str(e)}
        return jsonify(ret_obj), 400


@app.route(prefix + "/auth/login", methods=["POST"])
def login():
    if request.json is None:
        msg = "payload missing in request"
        return jsonify({"success": False, "message": msg}), 400

    email = request.json["email"]
    password = request.json["password"]
    try:
        commands.analyst_login(
            email,
            password,
            uow=unit_of_work.UnitOfWork(),
        )
        role = "analyst"

    except Exception as e:
        try:
            commands.investor_login(
                email,
                password,
                uow=unit_of_work.UnitOfWork(),
            )
            role = "investor"

        except Exception as e:
            retObj = {"success": False, "message": str(e)}
            return jsonify(retObj), 401

    # expires in 1hr
    access_token = create_access_token(
        identity=email, expires_delta=datetime.timedelta(hours=1)
    )
    retObj = {}
    retObj["success"] = True
    retObj["message"] = "User successfully logged in!"
    retObj["access_token"] = access_token
    retObj["token_type"] = "bearer"
    retObj["expires_in"] = 3600
    retObj["role"] = role

    return jsonify(retObj), 200


@app.route(prefix + "/auth/logout", methods=["POST"])
@jwt_required()
def analyst_logout():
    if request.json is None:
        msg = "payload missing in request"
        return jsonify({"success": False, "message": msg}), 400

    email = get_jwt_identity()

    if request.json["role"] == "investor":
        commands.investor_logout(
            email,
            uow=unit_of_work.UnitOfWork(),
        )
    elif request.json["role"] == "analyst":
        commands.analyst_logout(
            email,
            uow=unit_of_work.UnitOfWork(),
        )
    else:
        retObj = {"success": False, "message": "Role not found!"}
        return jsonify(retObj), 400

    retObj = {"success": True, "message": "Logged out successfully!"}
    return jsonify(retObj), 200


"""
Bot module
"""


@app.route(prefix + "/add-bot", methods=["POST"])
@jwt_required()
def add_bot():

    if request.json is None:
        msg = "payload missing in request"
        return jsonify({"success": False, "message": msg}), 400

    analyst_email = get_jwt_identity()
    analyst = queries.get_analyst(analyst_email, uow=unit_of_work.UnitOfWork())
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


@app.route(prefix + "/get-bots", methods=["POST"])
@jwt_required()
def get_bots():
    if request.json is None:
        msg = "payload missing in request"
        return jsonify({"success": False, "message": msg}), 400

    analyst_email = get_jwt_identity()
    analyst = queries.get_analyst(analyst_email, uow=unit_of_work.UnitOfWork())
    analyst_id = analyst.id
    investor_id = request.json["investor_id"]
    bots = queries.view_all_bots(analyst_id, investor_id, uow=unit_of_work.UnitOfWork())

    retObj = {"success": True, "bots": bots, "message": "Bots fetched successfully!"}
    return jsonify(retObj), 200


@app.route(prefix + "/initiate-bot-execution", methods=["PUT"])
def initiate_bot_execution():
    if request.json is None:
        msg = "payload missing in request"
        return jsonify({"success": False, "message": msg}), 400

    try:
        commands.initiate_bot_execution(
            request.json["bot_id"],
            uow=unit_of_work.UnitOfWork(),
        )
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 400

    retObj = {"success": True, "message": "Bot execution initiated successfully!"}
    return jsonify(retObj), 200


@app.route(prefix + "/terminate-bot", methods=["PUT"])
def terminate_bot():
    if request.json is None:
        msg = "payload missing in request"
        return jsonify({"success": False, "message": msg}), 400

    try:
        commands.terminate_bot(
            request.json["bot_id"],
            uow=unit_of_work.UnitOfWork(),
        )
    except Exception as e:
        retObj = {"success": False, "message": str(e)}
        return jsonify(retObj), 400

    retObj = {"success": True, "message": "Bot execution terminated successfully!"}
    return jsonify(retObj), 200


@app.route(prefix + "/handle-execution", methods=["PUT"])
def handle_execution():
    try:
        bots = commands.handle_execution(uow=unit_of_work.UnitOfWork())
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 400

    retObj = {
        "success": True,
        "message": "Bot execution handled successfully!",
        "bots": bots,
    }
    return jsonify(retObj), 200


@app.route(prefix + "/get-all-investors", methods=["GET"])
@jwt_required()
def get_all_investors():
    investors = queries.get_all_investors(uow=unit_of_work.UnitOfWork())
    retObj = {
        "success": True,
        "message": "All Investors returned!",
        "investors": investors,
    }
    return jsonify(retObj), 200




def atr_col(df):
  high_low = df['High'] - df['Low']
  high_prev_close = np.abs(df['High'] - df['Close'].shift())
  low_prev_close = np.abs(df['Low'] - df['Close'].shift())
  atr_df = pd.concat([high_low,high_prev_close,low_prev_close], axis=1)
  true_range = np.max(atr_df, axis=1)
  atr = true_range.rolling(14).mean()
  atr_df = atr.to_frame(name='ATR')
  ndf = pd.concat([df,atr_df],axis=1)
  ndf = ndf.dropna()
  return ndf

  


def predict(model,csv):
  pred_model = keras.models.load_model(model)
  sc = MinMaxScaler(feature_range = (0, 1))
  df = pd.read_csv(csv)
  ndf = atr_col(df)
  pred_X = ndf.iloc[-60:, 2: ].values
  pred_scaled = sc.fit_transform(pred_X)
  pred_scaled=pred_scaled.reshape(1,60,6)
  predicted_stock_price = pred_model.predict(pred_scaled)
  predicted_stock_price = sc.inverse_transform(predicted_stock_price)


  Open=predicted_stock_price[:,0][0]
  High=predicted_stock_price[:,1][0]
  Low=predicted_stock_price[:,2][0]
  Close=predicted_stock_price[:,3][0]
  # Volume=predicted_stock_price[:,4][0]
  ATR = predicted_stock_price[:,5][0]
  return Open,High,Low,Close,ATR

@app.route(prefix + "/stock/engro", methods=["GET"])
def get_stock_details():
    try:
        Open,High,Low,Close,ATR = predict('../../../ML/Engro.h5','../../../ML/ENGRO.csv')
        retObj = {}
        
        retObj['Open'] = float(Open)
        retObj['High'] = float(High)
        retObj['Low'] = float(Low)
        retObj['Close'] = float(Close)
        retObj['ATR'] = float(ATR)
        ret = successMessage("Stock details fetched successfully!", retObj)
        status = 200
    except Exception as e:
        ret = errorMessage(str(e))
        status = 400

    return ret, status



