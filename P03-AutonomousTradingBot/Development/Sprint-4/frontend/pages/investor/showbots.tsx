import { NextPage } from "next";
import InvestorLayout from "../../components/layouts/InvestorLayout";
import jwt from "jsonwebtoken";
import { useEffect, useState } from "react";
import axios from "axios";
import Link from "next/link";
import { useRouter } from "next/router";
import Swal from "sweetalert2";
import AnalystLayout from "../../components/layouts/AnalystLayout";
import {
  getAllBots,
  initiateBotExecution,
  terminateBot,
} from "../../services/auth";



interface Bot {
    id: string;
    state: string;
    risk_appetite: string;
    target_return: string;
    stocks_ticker: string;
    initial_balance: string
  }




const Home: NextPage = () => {
  const investor_id = "f30a39b9-76e6-4752-b4e6-00715442ddbf"

  const [bots, setBots] = useState<Array<Bot>>([]);

  useEffect(() => {
    if (!investor_id) return;

    getAllBots(investor_id).then((res) => {
      setBots(res.bots);
    });
  }, [investor_id]);



  return (
    <InvestorLayout>
      <div className="hero min-h-screen bg-base-200">
        <div className="hero-content text-center">
          <div className="max-w-4xl mx-auto ">
            <h1 className="text-5xl font-bold mb-6 text-primary">Current Instances</h1>

            {bots.length > 0 ? (
              <div className="grid gap-4 grid-cols-1 md:grid-cols-2 justify-items-start">
              {bots.map((b, i) => (
                <div
                  key={i}
                  className="p-4 card w-96 bg-blue text-neutral-content border-primary"
                >
                  <div className="card-body items-center text-center">
                    <h2 className="card-title font-bold text-primary">Bot ID: {b.id}</h2>
                    <p className="font-bold">Configuration Parameters:</p>
                    <ul>
                      <li className="text-info">State: {b.state}</li>
                      <li>Amount Invested: {b.initial_balance}</li>
                      <li>Risk Appetite: {b.risk_appetite}</li>
                      <li>Target Return: {b.target_return}%</li>
                      <li>Stock: {b.stocks_ticker}</li>
                    </ul>
                    <div className="card-actions justify-end">
                      <div className="btn-container">
                      <div className="flex justify-end">
                        
                        <Link href="/investor/graph/table">
                          <button className="btn btn-accent">View Trades</button>
                        </Link>
                        </div>
                      </div>
                    </div>
                  </div>

                </div>
              ))}
            </div>
            ) : (
              <p>No bot instances currently found for this investor.</p>
            )}
          </div>
        </div>
      </div>
    </InvestorLayout>
  );
};

export default Home;