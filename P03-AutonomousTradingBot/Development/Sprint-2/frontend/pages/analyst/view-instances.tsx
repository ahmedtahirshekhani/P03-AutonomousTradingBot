import type { NextPage } from "next";
import Link from "next/link";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
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
  duration: string;
}

const Home: NextPage = () => {
  const router = useRouter();
  const investor_id = router.query.investor_id;

  const [bots, setBots] = useState<Array<Bot>>([]);

  useEffect(() => {
    if (!investor_id) return;

    getAllBots(investor_id).then((res) => {
      setBots(res.bots);
    });
  }, [investor_id]);

  const handleStartClick = async (bot_id: string) => {
    const response = await initiateBotExecution(bot_id);
    Swal.fire(response.message);
    setBots((prevBots) =>
      prevBots.map((bot) =>
        bot.id === bot_id ? { ...bot, state: "Started" } : bot
      )
    );
  };

  const handleTerminateClick = async (bot_id: string) => {
    const response = await terminateBot(bot_id);
    Swal.fire(response.message);
    setBots((prevBots) =>
      prevBots.map((bot) =>
        bot.id === bot_id ? { ...bot, state: "Terminated" } : bot
      )
    );
  };

  return (
    <AnalystLayout>
      <div className="hero min-h-screen bg-base-200">
        <div className="hero-content text-center">
          <div className="max-w-2xl mx-auto">
            <h1 className="text-5xl font-bold">Current Instances</h1>
            <p className="py-6"></p>

            <div className="grid gap-4 md:grid-cols-2">
              {bots.map((b, i) => (
                <div
                  key={i}
                  className="p-4 card w-96 bg-neutral text-neutral-content"
                >
                  <div className="card-body items-center text-center">
                    <h2 className="card-title font-bold">{b.id}</h2>
                    <p className="font-bold">Configuration Parameters</p>
                    <ul>
                      <li className="text-info">State: {b.state}</li>
                      <li>Risk Appetite: {b.risk_appetite}</li>
                      <li>Target Return: {b.target_return}</li>
                      <li>Duration: {b.duration}</li>
                    </ul>
                    <div className="card-actions justify-end">
  <div className="btn-container">
    <button
      onClick={() => handleStartClick(b.id)}
      className="btn btn-primary mr-2"
    >
      Start
    </button>
    <button
      onClick={() => handleTerminateClick(b.id)}
      className="btn btn-error mr-2"
    >
      Terminate
    </button>
    <Link href="/analyst/graph">
      <button className="btn btn-accent">View Graph</button>
    </Link>
  </div>
</div>
                    </div>
                  </div>
                
              ))}
            </div>
          </div>
        </div>
      </div>
    </AnalystLayout>
  );
};

export default Home;
