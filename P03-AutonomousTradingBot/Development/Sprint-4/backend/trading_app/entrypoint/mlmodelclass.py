import psx
import numpy as np
import pandas as pd
import keras
import scipy as sp
import sklearn
from sklearn.preprocessing import MinMaxScaler
from keras.utils import to_categorical
import matplotlib.pyplot as plt
from datetime import date
from dateutil.relativedelta import relativedelta


class TrainModel:
    def __init__(self, ticker):
        self.ticker = ticker
        self.sc = None

    def get_train_data(self):
        now = date.today()
        five_year_earlier = now + relativedelta(years=-5)
        end_date = now + relativedelta(months=-2)
        data = psx.stocks(self.ticker, start=five_year_earlier, end=date.today())

        return data

    def get_test_data(self, till=date.today()):
        three_months_earlier = till + relativedelta(months=-3)

        data = None
        # Loop until no exception occurs
        while True:
            try:
                data = psx.stocks(self.ticker, start=three_months_earlier, end=till)
                break
            except:
                print("Exception occured when fetching data from psx stocks")

        return data

    def atr_col(self, df):
        high_low = df["High"] - df["Low"]
        high_prev_close = np.abs(df["High"] - df["Close"].shift())
        low_prev_close = np.abs(df["Low"] - df["Close"].shift())
        atr_df = pd.concat([high_low, high_prev_close, low_prev_close], axis=1)
        true_range = np.max(atr_df, axis=1)
        atr = true_range.rolling(14).mean()
        atr_df = atr.to_frame(name="ATR")
        ndf = pd.concat([df, atr_df], axis=1)
        ndf = ndf.dropna()
        return ndf

    def train(self):
        regressor = self.model()
        X_train, y_train, X_test, y_test = self.data_preprocess()
        regressor.fit(x=X_train, y=y_train, batch_size=32, epochs=100)
        regressor.save(f"../../../ML/{self.ticker}.h5")

    def model(self):
        regressor = keras.Sequential()
        regressor.add(
            keras.layers.LSTM(units=100, return_sequences=True, input_shape=(15, 6))
        )
        regressor.add(keras.layers.Dropout(rate=0.2))
        regressor.add(keras.layers.LSTM(units=100, return_sequences=True))
        regressor.add(keras.layers.Dropout(rate=0.2))
        regressor.add(keras.layers.LSTM(units=100, return_sequences=True))
        regressor.add(keras.layers.Dropout(rate=0.2))
        regressor.add(keras.layers.LSTM(units=100, return_sequences=True))
        regressor.add(keras.layers.Dropout(rate=0.2))
        regressor.add(keras.layers.LSTM(units=100, return_sequences=True))
        regressor.add(keras.layers.Dropout(rate=0.2))
        regressor.add(keras.layers.LSTM(units=100, return_sequences=False))
        regressor.add(keras.layers.Dropout(rate=0.2))
        regressor.add(keras.layers.Dense(units=6))
        regressor.compile(optimizer="adam", loss="mean_squared_error")
        return regressor

    def predict(self, model, till=date.today()):

        pred_model = keras.models.load_model(model)
        sc = MinMaxScaler(feature_range=(0, 1))
        df = self.get_test_data(till=till)
        ndf = self.atr_col(df)
        pred_X = ndf.iloc[-15:].values
        pred_scaled = sc.fit_transform(pred_X)
        pred_scaled = pred_scaled.reshape(1, 15, 6)
        predicted_stock_price = pred_model.predict(pred_scaled)
        predicted_stock_price = sc.inverse_transform(predicted_stock_price)
        Open = predicted_stock_price[:, 0][0]
        High = predicted_stock_price[:, 1][0]
        Low = predicted_stock_price[:, 2][0]
        Close = predicted_stock_price[:, 3][0]
        ATR = predicted_stock_price[:, 5][0]
        return Open, High, Low, Close, ATR

    def data_preprocess(self):
        df = self.get_train_data()
        ndf = self.atr_col(df)
        all_data_values = ndf.values
        train_X = all_data_values[: int(all_data_values.shape[0] * 0.85), :]
        test_X = all_data_values[int(all_data_values.shape[0] * 0.85) :, :]
        print(train_X.shape, test_X.shape)
        self.sc = MinMaxScaler(feature_range=(0, 1))
        training_scaled = self.sc.fit_transform(train_X)
        testing_scaled = self.sc.fit_transform(test_X)
        X_train = []
        y_train = []
        for i in range(15, len(training_scaled) - 7):
            X_train.append(training_scaled[i - 15 : i, :])
            y_train.append(training_scaled[i + 7, :])
        X_train, y_train = np.array(X_train).astype(np.float64), np.array(
            y_train
        ).astype(np.float64)
        print(X_train.shape, y_train.shape)
        X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 6)).astype(
            np.float64
        )
        print(train_X.shape, test_X.shape)
        temp = np.vstack((train_X, test_X))
        inputs = temp[len(temp) - len(test_X) - 7 :]
        inputs = inputs.reshape(-1, 6)
        inputs.shape
        inputs = self.sc.transform(inputs)
        X_test = []
        y_test = []
        for i in range(15, len(inputs) - 7):
            X_test.append(inputs[i - 15 : i, :])
            y_test.append(i + 7)

        X_test = np.array(X_test).astype(np.float64)
        X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 6))
        return X_train, y_train, X_test, y_test
