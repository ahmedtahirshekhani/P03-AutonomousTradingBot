import { NextPage } from "next";
import React, { useEffect, useState } from "react";
// import { Line } from 'react-chartjs-2';


const trades = [
  {
    id: "1",
    amount: 1000,
    start_price: 20.5,
    started_at: "2022-03-31 16:30:00.000",
    trade_type: "CALL",
    ended_at: "2022-03-31 17:30:00.000",
    end_price: 25.0,
    is_profit: true,
  },
  {
    id: "2",
    amount: 500,
    start_price: 30.2,
    started_at: "2022-03-30 15:00:00.000",
    trade_type: "PUT",
    ended_at: "2022-03-30 16:00:00.000",
    end_price: 27.5,
    is_profit: false,
  },
  {
    id: "3",
    amount: 2000,
    start_price: 50.0,
    started_at: "2022-03-29 10:30:00.000",
    trade_type: "CALL",
    ended_at: "2022-03-29 11:00:00.000",
    end_price: 55.0,
    is_profit: true,
  }
];



const data = trades.map((trade, index) => {
  const profit = trade.is_profit ? "Yes" : "No";
  return {
    trade_number: index + 1,
    start_price: trade.start_price,
    end_price: trade.end_price,
    amount: trade.amount,
    trade_type: trade.trade_type,
    bot_id: trade.id,
    stock_name: "HBL",
    profit: profit
  };
});
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ScatterChart,
  Scatter,
} from "recharts";
import AnalystDashboard from "..";
import AnalystLayout from "../../../components/layouts/AnalystLayout";
import Link from "next/link";

const Home: NextPage = () => {
  const CustomTooltip = ({
    active,
    payload,
  }: {
    active: boolean;
    payload?: any[];
  }) => {
    if (active && payload && payload.length) {
      const trade = payload[0].payload;
      return (
        <div className="tooltip">
          <p>{`Bot ID: ${trade.bot_id}`}</p>
          <p>{`Stock Name: ${trade.stock_name}`}</p>
          {/* <p>{`Profit: ${trade.profit}`}</p> */}
          <p>{`Amount: ${trade.amount}`}</p>
          <p>{`Trade Type: ${trade.trade_type}`}</p>
          <p>{`Start Price: ${trade.start_price}`}</p>
          <p>{`End Price: ${trade.end_price}`}</p>
          <p>{`Profit: ${trade.profit}`}</p>
        </div>
      );
    }
    return null;
  };

  return (
    <AnalystLayout>
      <div
          className="text-5xl font-bold font-serif text-primary"
          style={{ textAlign: "center" }}
        >
          <h1>Trading History Graph</h1>
        </div>
    <div className="max-w-4xl ">
      {/* <h1 className="text-5xl font-bold font-serif mb-8 text-primary">
            Trading History Graph
          </h1> */}
      <div className="py-6" style={{ width: "100%", height: 500 }}>
        
      <LineChart
  width={1500}
  height={600}
  data={data}
  margin={{ top: 50, right: 30, bottom: 50, left: 80 }}
>
  <CartesianGrid strokeDasharray="3 3" />
  <XAxis dataKey="trade_number" label={{ value: "Trade Number", position: "insideBottom", dy: 10 }} />
  <YAxis dataKey="end_price" domain={[0, "dataMax"]} label={{ value: "Price", angle: -90, position: "insideLeft" }} />
  <Legend layout="vertical" align="right" verticalAlign="middle" />
  <Tooltip content={<CustomTooltip active={false} />} />
          <Line
            type="monotone"
            dataKey="start_price"
            stroke="#8884d8"
            name="Start Price"
            dot={{ r: 4 }}
          />
          <Line
            type="monotone"
            dataKey="end_price"
            stroke="#82ca9d"
            name="End Price"
            dot={{ r: 4 }}
          />
        </LineChart>
        
      </div>
      
    </div>

    
    </AnalystLayout>
  );
};

export default Home;