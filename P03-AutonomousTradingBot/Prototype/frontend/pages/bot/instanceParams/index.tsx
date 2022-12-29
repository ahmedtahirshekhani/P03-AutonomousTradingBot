import type { NextPage } from "next";

const Home: NextPage = () => {
  return (
    <div className="hero min-h-screen bg-base-200">
      <div className="hero-content text-center">
        <div className="max-w-md">
          <h1 className="text-5xl font-bold">Instance Parameters</h1>
          <p className="py-6"></p>
          <div className="form-control w-full max-w-xs">
            <label className="label">
              <span className="label-text">Amount to invest ?</span>
            </label>
            <input
              type="text"
              placeholder="Amount"
              className="input input-primary w-full max-w-xs"
            />

            <label className="label"></label>

            <label className="label">
              <span className="label-text">Maximum Drawdown(%) ?</span>
            </label>
            <div className="dropdown dropdown-right">
              <label tabIndex={0} className="btn btn-wide rounded button text-primary">
                Risk Apetite
              </label>
              <ul
                tabIndex={0}
                className="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52"
              >
                <li>
                  <a>Low Risk - 5%</a>
                </li>
                <li>
                  <a>Medium Risk - 10%</a>
                </li>
                <li>
                  <a>High Risk - 15%</a>
                </li>
              </ul>
            </div>


            <label className="label">
              <span className="label-text">Minimum Target Returns(%) ?</span>
            </label>
            <div className="dropdown dropdown-right">
              <label tabIndex={0} className="btn btn-wide rounded button text-primary">
                ROI
              </label>
              <ul
                tabIndex={0}
                className="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52"
              >
                <li>
                  <a>5%</a>
                </li>
                <li>
                  <a>10%</a>
                </li>
                <li>
                  <a>15%</a>
                </li>
              </ul>
            </div>


            <label className="label"></label>
          </div>
          <button className="btn btn-primary">Submit</button>
        </div>
      </div>
    </div>
  );
};

export default Home;
