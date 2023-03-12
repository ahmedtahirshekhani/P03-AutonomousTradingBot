import type { NextPage } from "next";
import { useRouter } from "next/router";
import { useState } from "react";
import Swal from "sweetalert2";
import AnalystLayout from "../../components/layouts/AnalystLayout";
import { addBot } from "../../services/auth";

const Home: NextPage = () => {
  const router = useRouter();

  const [amount, setAmount] = useState("");
  const [risk, setRisk] = useState("");
  const [roi, setRoi] = useState("");
  const [duration, setDuration] = useState("");

  const handleSubmit = async () => {
    const response = await addBot(router.query.investor_id, risk, roi, amount);
    Swal.fire(response.message);
    router.push("/analyst");
  };

  return (
    <AnalystLayout>
      <div className="hero min-h-screen bg-base-200">
        <div className="hero-content text-center">
          <div className="max-w-md">
            <h1 className="mb-6 text-5xl font-bold">Instance Parameters</h1>

            <div className="form-control">
              <label className="label">
                <span className="label-text">Amount to invest ?</span>
              </label>
              <input
                type="number"
                placeholder="Amount"
                className="input input-primary"
                onChange={(e) => setAmount(e.target.value)}
              />

              {/* <label className="label">
                <span className="label-text">Duration Till ?</span>
              </label>
              <input
                type="date-local"
                placeholder="Date"
                className="input input-primary"
                onChange={(e) => setDuration(e.target.value)}
              /> */}

              <label className="label"></label>

              <label className="label">
                <span className="label-text">Maximum Drawdown(%) ?</span>
              </label>
              <div className="dropdown dropdown-right">
                <label
                  tabIndex={0}
                  className="btn btn-wide rounded button text-primary"
                >
                  Risk Apetite: {risk}
                </label>
                <ul
                  tabIndex={0}
                  className="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52"
                >
                  <li onClick={() => setRisk("LOW")}>
                    <a>Low Risk - 5%</a>
                  </li>
                  <li onClick={() => setRisk("MEDIUM")}>
                    <a>Medium Risk - 10%</a>
                  </li>
                  <li onClick={() => setRisk("HIGH")}>
                    <a>High Risk - 15%</a>
                  </li>
                </ul>
              </div>

              <label className="label">
                <span className="label-text">Minimum Target Returns(%) ?</span>
              </label>
              <div className="dropdown dropdown-right">
                <label
                  tabIndex={0}
                  className="btn btn-wide rounded button text-primary"
                >
                  ROI: {roi}
                </label>
                <ul
                  tabIndex={0}
                  className="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52"
                >
                  <li onClick={() => setRoi("5")}>
                    <a>5%</a>
                  </li>
                  <li onClick={() => setRoi("10")}>
                    <a>10%</a>
                  </li>
                  <li onClick={() => setRoi("15")}>
                    <a>15%</a>
                  </li>
                </ul>
              </div>

              <label className="label"></label>
            </div>
            <button onClick={handleSubmit} className="btn btn-primary">
              Submit
            </button>
          </div>
        </div>
      </div>
    </AnalystLayout>
  );
};

export default Home;
