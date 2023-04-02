import { NextPage } from "next";
import React from "react";
import AnalystLayout from "../../../components/layouts/AnalystLayout";
import Link from "next/link";

interface Trade {
  id: string;
  amount: number;
  start_price: number;
  started_at: string;
  trade_type: string;
  ended_at: string;
  end_price: number;
  is_profit: boolean;
}

interface TradeTableProps {
  trades: Trade[];
}


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


const TradeTable: React.FC<TradeTableProps> = ({ trades }) => {
  return (
    <div className='hero min-h-screen'>
				<div className='hero-content text-center'>
					<div className='max-w-4xl'>
						<h1 className='text-5xl font-bold text-primary'>Trade History</h1>

						<p className='py-6'></p>
						<div className=''>
						{trades.length ? (
							<><table className='table w-full'>
                <thead>
                  <tr className='text-primary'>
                    <th>ID</th>
                    <th>Amount</th>
                    <th>Start Price</th>
                    <th>Started At</th>
                    <th>Trade Type</th>
                    <th>Ended At</th>
                    <th>End Price</th>
                    <th>Profit ?</th>
                  </tr>
                </thead>
                <tbody>
                  {trades.map((trade) => (
                    <tr key={trade.id}>
                      <td>{trade.id}</td>
                      <td>{trade.amount}</td>
                      <td>{trade.start_price}</td>
                      <td>{trade.started_at}</td>
                      <td>{trade.trade_type}</td>
                      <td>{trade.ended_at}</td>
                      <td>{trade.end_price}</td>
                      <td>{trade.is_profit ? "Yes" : "No"}</td>
                    </tr>
                  ))}
                </tbody>
              </table><div className="text-center text-xl py-8">
                  <Link href="../analyst">
                    <button className="btn btn-wide btn-primary"><h1>
                      View Graph</h1>
                    </button></Link>
                </div></>
              ) : (
                <p>No trades found.</p>
              )}
              </div>
              </div>
            </div>
          </div>
  );
};


const Home: NextPage = () => {
  

  return (
    <AnalystLayout>
    <TradeTable trades={trades} />
    </AnalystLayout>
  );

};

export default Home;
