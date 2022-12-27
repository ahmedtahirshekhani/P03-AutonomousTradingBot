import type { NextPage } from "next";
import Link from "next/link";
import AssignBot from "../../../components/assign_bot";

const Home: NextPage = () => {
  return (
    <div className="hero min-h-screen">
      <div className="hero-content text-center">
        <div className="max-w-xl">
          <h1 className="text-5xl font-bold">Autonomous Trading Bot</h1>
          <h1 className="text-xl font-bold pt-6 ">Assign Bots to Investor</h1>
          
          <p className="py-6"></p>
          <div className="">
            <table className="table w-full">
              <thead>
                <tr className="text-primary">
                  <th></th>
                  <th>Name </th>
                  <th>Email Address</th>
                  <th>Phone Number</th>
                  <th>Assign Bots</th>
                </tr>
              </thead>
              <tbody>
                <AssignBot name="Ali" email="ali@gmail.com" phone="02135526879"  />
                <AssignBot name="Sheikhani" email="sheikhani@gmail.com" phone="02135526879"  />
                <AssignBot name="Suleiman" email="suleiman@gmail.com" phone="02135526879"  />
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
