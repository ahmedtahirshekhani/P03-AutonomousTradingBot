import { NextPage } from 'next';
import React, { useEffect, useState } from "react";
// import { Line } from 'react-chartjs-2';
import { Chart } from 'chart.js';
import data from '../graph/tradeData.json'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';







const Home: NextPage = () => {


    return (
        <div className="hero min-h-screen">
        <div className="hero-content text-center">
            <div className="max-w-xl">
                <h1 className="text-5xl font-bold">
                    Trading History Graph
                </h1>
                <p className="py-6">
                <LineChart width={800} height={500} data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="trade_number" label={'Trade Number'}/>
      <YAxis dataKey="amount"/>
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="bot_id" name="Bot ID" />
      <Line type="monotone" dataKey="profit" stroke="#8884d8" name="Profit" />
      <Line type="monotone" dataKey="start_price" stroke="#8884d8" name="Start Price" />
      <Line type="monotone" dataKey="end_price" stroke="#82ca9d" name="End Price" />
      <Line type="monotone" dataKey="trade_type" name="Trade Type" />
      <Line type="monotone" dataKey="stock_name" name="Stock Name" />
    </LineChart>
    </p>
            </div>
        </div>
    </div> 
    
  );
}

export default Home ;

