import { NextPage } from "next";
import React, { useEffect, useState } from "react";
// import { Line } from 'react-chartjs-2';


const APIdata = {
  "data": {
      "analyst_id": "3cd03aea-22a4-4d59-9578-0af8f6073f33",
      "assigned_model": 0,
      "current_balance": "953.5599999999997",
      "end_time": "Fri, 31 Dec 9999 18:59:59 GMT",
      "id": "e16dfe33-4f87-431c-ab40-b9e46583e729",
      "in_trade": true,
      "initial_balance": "1000.0",
      "investor_id": "7385969d-492d-4f18-bcac-e0eb55eaaf5a",
      "prices": {
          "1648515600": 267.6,
          "1648861200": 266.13,
          "1648947600": 265.82,
          "1649034000": 271.89,
          "1649120400": 269.98,
          "1649206800": 272.05,
          "1649466000": 279.65,
          "1649552400": 278.96,
          "1649638800": 279.82,
          "1649725200": 287.92,
          "1649811600": 291.58,
          "1650070800": 289.32,
          "1650157200": 296.23,
          "1650243600": 294.77,
          "1650330000": 286.62,
          "1650416400": 284.69,
          "1650675600": 289.58,
          "1650762000": 290.76,
          "1650848400": 278.13,
          "1650934800": 277.75,
          "1651626000": 275.18,
          "1651885200": 269.92,
          "1651971600": 272.31,
          "1652058000": 269.9,
          "1652144400": 268.0,
          "1652230800": 270.01,
          "1652490000": 267.12,
          "1652576400": 267.98,
          "1652662800": 266.51,
          "1652749200": 268.4,
          "1652835600": 267.2,
          "1653094800": 264.21,
          "1653181200": 264.1,
          "1653267600": 265.17,
          "1653354000": 266.6,
          "1653440400": 265.22,
          "1653699600": 266.37,
          "1653786000": 268.08,
          "1653958800": 264.33,
          "1654045200": 262.13,
          "1654304400": 262.76,
          "1654390800": 262.47,
          "1654477200": 261.31,
          "1654563600": 261.29,
          "1654650000": 263.83,
          "1654909200": 260.84,
          "1654995600": 261.02,
          "1655082000": 261.2,
          "1655168400": 261.3,
          "1655254800": 264.27,
          "1655514000": 263.05,
          "1655600400": 264.5,
          "1655686800": 262.85,
          "1655773200": 263.9,
          "1655859600": 253.81,
          "1656118800": 256.98,
          "1656205200": 257.38,
          "1656291600": 255.76,
          "1656378000": 257.09,
          "1656723600": 254.06,
          "1656810000": 253.68,
          "1656896400": 252.3,
          "1656982800": 251.96,
          "1657501200": 252.79,
          "1657587600": 257.4,
          "1657674000": 256.73,
          "1657933200": 251.97,
          "1658019600": 244.7,
          "1658106000": 243.75,
          "1658192400": 241.57,
          "1658278800": 245.17,
          "1658538000": 242.42,
          "1658624400": 241.54,
          "1658710800": 238.83,
          "1658797200": 236.95,
          "1658883600": 234.62,
          "1659229200": 235.54,
          "1659315600": 238.03,
          "1659402000": 237.11,
          "1659488400": 238.92,
          "1659920400": 242.23,
          "1660006800": 240.46,
          "1660093200": 243.01,
          "1660352400": 248.05,
          "1660438800": 252.13,
          "1660525200": 253.65,
          "1660611600": 251.86,
          "1660698000": 251.71,
          "1660957200": 250.26,
          "1661043600": 254.78,
          "1661130000": 259.35,
          "1661216400": 245.23,
          "1661302800": 242.85,
          "1661562000": 242.77,
          "1661648400": 239.31,
          "1661734800": 238.36,
          "1661907600": 237.99,
          "1662166800": 234.04,
          "1662253200": 232.94,
          "1662339600": 230.98,
          "1662426000": 231.13,
          "1662512400": 230.9,
          "1662771600": 230.82,
          "1662858000": 232.14,
          "1662944400": 230.58,
          "1663030800": 227.64,
          "1663117200": 229.42,
          "1663376400": 233.36,
          "1663462800": 233.17,
          "1663549200": 233.02,
          "1663635600": 234.25,
          "1663722000": 229.91,
          "1663981200": 233.56,
          "1664067600": 231.32,
          "1664154000": 231.81,
          "1664240400": 230.65,
          "1664326800": 231.52,
          "1664586000": 230.84,
          "1664672400": 232.99,
          "1664758800": 232.43,
          "1664845200": 236.41,
          "1664931600": 239.6,
          "1665190800": 237.55,
          "1665277200": 238.69,
          "1665363600": 237.51,
          "1665450000": 237.12,
          "1665536400": 237.43,
          "1665795600": 236.08,
          "1665882000": 235.86,
          "1665968400": 242.21,
          "1666054800": 243.82,
          "1666141200": 246.57,
          "1666400400": 247.15,
          "1666486800": 248.06,
          "1666573200": 245.17,
          "1666659600": 245.54,
          "1666746000": 234.62,
          "1667005200": 235.2,
          "1667178000": 239.15,
          "1667264400": 239.99,
          "1667350800": 239.76,
          "1667610000": 241.57,
          "1667696400": 244.03,
          "1667869200": 244.94,
          "1667955600": 245.0,
          "1668214800": 241.96,
          "1668301200": 244.52,
          "1668387600": 258.91,
          "1668474000": 257.55,
          "1668560400": 257.33,
          "1668819600": 254.73,
          "1668906000": 260.38,
          "1668992400": 262.06,
          "1669078800": 264.28,
          "1669165200": 268.3,
          "1669424400": 262.46,
          "1669510800": 260.42,
          "1669597200": 262.99,
          "1669770000": 265.74,
          "1670029200": 261.78,
          "1670115600": 261.36,
          "1670202000": 261.67,
          "1670288400": 262.93,
          "1670374800": 262.01,
          "1670634000": 260.61,
          "1670720400": 269.2,
          "1670806800": 269.02,
          "1670893200": 276.72,
          "1670979600": 275.67,
          "1671238800": 272.52,
          "1671325200": 264.97,
          "1671411600": 260.11,
          "1671498000": 262.88,
          "1671584400": 259.19,
          "1671843600": 264.69,
          "1671930000": 261.26,
          "1672016400": 256.18,
          "1672102800": 260.79,
          "1672189200": 262.01,
          "1672448400": 270.07,
          "1672534800": 269.36,
          "1672621200": 270.31,
          "1672707600": 277.5,
          "1672794000": 284.68,
          "1673053200": 280.24,
          "1673139600": 283.04,
          "1673226000": 281.6,
          "1673312400": 279.48,
          "1673398800": 278.17,
          "1673658000": 274.05,
          "1673744400": 264.8,
          "1673830800": 269.56,
          "1673917200": 267.34,
          "1674003600": 265.88,
          "1674262800": 264.23,
          "1674349200": 273.12,
          "1674435600": 286.15,
          "1674522000": 296.73,
          "1674608400": 289.63,
          "1674867600": 285.29,
          "1674954000": 298.16,
          "1675126800": 305.72,
          "1675213200": 300.14,
          "1675472400": 299.28,
          "1675558800": 295.96,
          "1675645200": 296.75,
          "1675731600": 298.37,
          "1675818000": 294.03,
          "1676077200": 298.31,
          "1676163600": 297.7,
          "1676250000": 298.32,
          "1676336400": 300.02,
          "1676422800": 301.08,
          "1676682000": 300.01,
          "1676768400": 299.94,
          "1676854800": 299.42,
          "1676941200": 298.62,
          "1677027600": 299.0,
          "1677286800": 298.51,
          "1677373200": 300.13,
          "1677546000": 304.48,
          "1677632400": 301.43,
          "1677891600": 300.09,
          "1677978000": 299.93,
          "1678064400": 299.69,
          "1678150800": 299.59,
          "1678237200": 298.51,
          "1678496400": 298.3,
          "1678582800": 298.09,
          "1678669200": 294.99,
          "1678755600": 293.19,
          "1678842000": 292.15,
          "1679101200": 286.85,
          "1679187600": 286.57,
          "1679274000": 283.98,
          "1679446800": 284.02,
          "1679706000": 282.29,
          "1679792400": 282.15,
          "1679878800": 280.01,
          "1679965200": 279.99,
          "1680051600": 276.78
      },
      "risk_appetite": "LOW",
      "start_time": "Sun, 02 Apr 2023 22:16:58 GMT",
      "state": "2",
      "stocks_ticker": "ENGRO",
      "target_return": "5.0",
      "trades": [
          {
              "amount": "100",
              "end_price": "284.69",
              "ended_at": "Wed, 20 Apr 2022 01:00:00 GMT",
              "id": "be0a6fa2-9f6c-4df6-9485-e52a9ba02d4c",
              "is_profit": false,
              "start_price": "271.89",
              "started_at": "Mon, 04 Apr 2022 01:00:00 GMT",
              "trade_type": "2"
          },
          {
              "amount": "100",
              "end_price": "268.08",
              "ended_at": "Sun, 29 May 2022 01:00:00 GMT",
              "id": "521038be-178c-4a28-90d4-0eef5569753e",
              "is_profit": false,
              "start_price": "275.18",
              "started_at": "Wed, 04 May 2022 01:00:00 GMT",
              "trade_type": "1"
          },
          {
              "amount": "100",
              "end_price": "257.09",
              "ended_at": "Tue, 28 Jun 2022 01:00:00 GMT",
              "id": "88e3a23a-7b73-43df-af42-41a1041de7e6",
              "is_profit": true,
              "start_price": "253.81",
              "started_at": "Wed, 22 Jun 2022 01:00:00 GMT",
              "trade_type": "1"
          },
          {
              "amount": "100",
              "end_price": "257.4",
              "ended_at": "Tue, 12 Jul 2022 01:00:00 GMT",
              "id": "86d319b4-41dc-4c26-8aa6-5a5985332d56",
              "is_profit": true,
              "start_price": "252.3",
              "started_at": "Mon, 04 Jul 2022 01:00:00 GMT",
              "trade_type": "1"
          },
          {
              "amount": "100",
              "end_price": "242.23",
              "ended_at": "Mon, 08 Aug 2022 01:00:00 GMT",
              "id": "9c0933d0-0d77-4b11-afa1-dc22754260ca",
              "is_profit": false,
              "start_price": "251.97",
              "started_at": "Sat, 16 Jul 2022 01:00:00 GMT",
              "trade_type": "1"
          },
          {
              "amount": "100",
              "end_price": "245.23",
              "ended_at": "Tue, 23 Aug 2022 01:00:00 GMT",
              "id": "80419e74-f664-41e0-886f-d47beb19d563",
              "is_profit": false,
              "start_price": "243.01",
              "started_at": "Wed, 10 Aug 2022 01:00:00 GMT",
              "trade_type": "2"
          },
          {
              "amount": "100",
              "end_price": "234.25",
              "ended_at": "Tue, 20 Sep 2022 01:00:00 GMT",
              "id": "f2fdba31-6cd0-4520-bf7a-a196c5a7b3a4",
              "is_profit": false,
              "start_price": "242.85",
              "started_at": "Wed, 24 Aug 2022 01:00:00 GMT",
              "trade_type": "1"
          },
          {
              "amount": "100",
              "end_price": "234.62",
              "ended_at": "Wed, 26 Oct 2022 01:00:00 GMT",
              "id": "e86a0099-9c7e-4396-9cfe-3eff2e48a4af",
              "is_profit": true,
              "start_price": "236.41",
              "started_at": "Tue, 04 Oct 2022 01:00:00 GMT",
              "trade_type": "2"
          },
          {
              "amount": "100",
              "end_price": "239.76",
              "ended_at": "Wed, 02 Nov 2022 01:00:00 GMT",
              "id": "2cc77fe6-0c1a-4459-a667-599ab015c649",
              "is_profit": true,
              "start_price": "234.62",
              "started_at": "Wed, 26 Oct 2022 01:00:00 GMT",
              "trade_type": "1"
          },
          {
              "amount": "100",
              "end_price": "264.97",
              "ended_at": "Sun, 18 Dec 2022 01:00:00 GMT",
              "id": "7cf09d87-3525-435b-ac42-f81fab421224",
              "is_profit": false,
              "start_price": "244.03",
              "started_at": "Sun, 06 Nov 2022 01:00:00 GMT",
              "trade_type": "2"
          },
          {
              "amount": "100",
              "end_price": "270.07",
              "ended_at": "Sat, 31 Dec 2022 01:00:00 GMT",
              "id": "0a1615ab-ca83-4172-a397-295615a1552c",
              "is_profit": true,
              "start_price": "260.11",
              "started_at": "Mon, 19 Dec 2022 01:00:00 GMT",
              "trade_type": "1"
          },
          {
              "amount": "100",
              "end_price": "274.05",
              "ended_at": "Sat, 14 Jan 2023 01:00:00 GMT",
              "id": "634af4b9-80cf-4569-8cf0-2b7eedbe239a",
              "is_profit": false,
              "start_price": "269.36",
              "started_at": "Sun, 01 Jan 2023 01:00:00 GMT",
              "trade_type": "2"
          },
          {
              "amount": "100",
              "end_price": "273.12",
              "ended_at": "Sun, 22 Jan 2023 01:00:00 GMT",
              "id": "c8565546-32dd-48f2-b5da-0a4fc415ce53",
              "is_profit": true,
              "start_price": "264.8",
              "started_at": "Sun, 15 Jan 2023 01:00:00 GMT",
              "trade_type": "1"
          },
          {
              "amount": "100",
              "end_price": "300.09",
              "ended_at": "Sat, 04 Mar 2023 01:00:00 GMT",
              "id": "2b162aa5-701c-484d-be10-1b26e4fabb67",
              "is_profit": false,
              "start_price": "286.15",
              "started_at": "Mon, 23 Jan 2023 01:00:00 GMT",
              "trade_type": "2"
          },
          {
              "amount": "100",
              "end_price": "275",
              "ended_at": "Fri, 31 Dec 9999 18:59:59 GMT",
              "id": "46a75109-5016-4dbc-80e1-89bd44be5168",
              "is_profit": false,
              "start_price": "294.99",
              "started_at": "Mon, 13 Mar 2023 01:00:00 GMT",
              "trade_type": "1"
          }
      ]
  },
  "message": "Bot successfully fetched!",
  "success": true
}

const trades = APIdata['data']['trades']



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
import InvestorLayout from "../../../components/layouts/InvestorLayout";

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
    <InvestorLayout>
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

    
    </InvestorLayout>
  );
};

export default Home;