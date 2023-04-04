import { NextPage } from "next";
import AnalystLayout from "../../../components/layouts/AnalystLayout";

interface BotPerformance {
  id: string;
  initialInvestment: string;
  currentValue: string;
  profit: boolean;
  percent: string;
  gain: string
}

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
  },
  "message": "Bot successfully fetched!",
  "success": true
};

const botPerformance: BotPerformance = {
  id: APIdata.data.id,
  initialInvestment: APIdata.data.initial_balance,
  currentValue: APIdata.data.current_balance,
  profit: parseFloat(APIdata.data.current_balance) > parseFloat(APIdata.data.initial_balance),
  percent: ((parseFloat(APIdata.data.current_balance) - parseFloat(APIdata.data.initial_balance)) / parseFloat(APIdata.data.initial_balance) * 100).toFixed(2) + '%',
  gain: ((parseFloat(APIdata.data.current_balance) - parseFloat(APIdata.data.initial_balance))).toFixed(2) 
};

const trades = []; // Placeholder for trades data

const TradeTable: React.FC<any> = () => {
  return (
    <div className='hero min-h-screen'>
      <div className='hero-content text-center'>
        <div className=''>
          <h1 className='text-5xl font-bold text-primary'>Bot Performance</h1>

          <p className='py-6'></p>
          <div className=''>
            <table className='table w-full custom-table'>
              <thead>
                <tr className='text-primary'>
                  <th>ID</th>
                  <th>Initial Investment(PKR)</th>
                  <th>Current Value(PKR)</th>
                  <th>In Profit ?</th>
                  <th>{botPerformance.profit ? 'Gain (PKR)' : 'Loss(PKR)'} </th>
                  <th>{botPerformance.profit ? '% Gain' : '% Loss'} </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>{botPerformance.id}</td>
                  <td>{botPerformance.initialInvestment}</td>
                  <td>{botPerformance.currentValue}</td>
                  <td>{botPerformance.profit ? 'Yes' : 'No'}</td>
                  <td>{botPerformance.gain}</td>
                  <td>{botPerformance.percent}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

const Home: NextPage = () => {
  return (
    <AnalystLayout>
      <TradeTable />
    </AnalystLayout>
  );
};

export default Home;
