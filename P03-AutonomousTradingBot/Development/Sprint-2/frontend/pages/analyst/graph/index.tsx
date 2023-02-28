import { NextPage } from 'next';
import React, { useEffect, useState } from "react";
// import { Line } from 'react-chartjs-2';
import data from '../graph/tradeData.json'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ScatterChart , Scatter } from 'recharts';







const Home: NextPage = () => {
    
    const CustomTooltip = ({ active, payload }: { active: boolean, payload?: any[] }) => {
        if (active && payload && payload.length) {
          const trade = payload[0].payload;
          return (
            <div className="tooltip">
              <p>{`Bot ID: ${trade.bot_id}`}</p>
              <p>{`Stock Name: ${trade.stock_name}`}</p>
              <p>{`Profit: ${trade.profit}`}</p>
              <p>{`Trade Type: ${trade.trade_type}`}</p>
              <p>{`Start Price: ${trade.start_price}`}</p>
              <p>{`End Price: ${trade.end_price}`}</p>
            </div>
          );
        }
        return null;
      };

    return (
       
        <div className="max-w-xl">
          {/* <h1 className="text-5xl font-bold font-serif mb-8 text-primary">
            Trading History Graph
          </h1> */}
          <div className="py-6" style={{ width: '100%', height: 500 }}>
          <div className="text-5xl font-bold font-serif text-primary" style={{ textAlign: 'center' }}>
          <h1>Trading History Graph</h1>
          </div>
          <LineChart width={1300} height={600} data={data} margin={{ top: 50, right: 30, bottom: 50, left: 30 }}>

              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="trade_number" label={'Trade Number'} />
              <YAxis dataKey="amount" />
              <Legend />
              <Tooltip content={<CustomTooltip active={false} />} />
              <Line type="monotone" dataKey="start_price" stroke="#8884d8" name="Start Price" dot={{ r: 4 }} />
              <Line type="monotone" dataKey="end_price" stroke="#82ca9d" name="End Price" dot={{ r: 4 }} />
    </LineChart>
    </div>
            </div>
       
    
  );
}

export default Home ;

