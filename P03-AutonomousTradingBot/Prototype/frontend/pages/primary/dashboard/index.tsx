import type { NextPage } from "next";
import Link from "next/link";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { logout } from "../../../services/auth";

const Home: NextPage = () => {
  const router = useRouter();
  const [username, setUsername] = useState("");
  const [role, setRole] = useState("");
  const logoutAuth = () => {
    const email = localStorage.getItem("email")!;
    const role = localStorage.getItem("role")!;
    logout(email, role)
      .then((res) => {
        console.log(res);
        localStorage.removeItem("token");
        localStorage.removeItem("expiry");
        localStorage.removeItem("email");
        router.push("/primary");
      })
      .catch((err) => {
        console.log(err);
      });
  };

  // useEffect(() => {
  //   if (localStorage.getItem("token") === null) {
  //     router.push("/primary/login");
  //   } else {
  //     const email = localStorage.getItem("email")!;
  //     const role = localStorage.getItem("role")!;
  //     const username = email?.split("@")[0];
  //     setRole(role)!;
  //     setUsername(username);
  //   }
  // }, []);

  return (
    <div>
      <div className="drawer drawer-mobile drop-shadow-lg">
        {/* <input id="my-drawer" type="checkbox" className="drawer-toggle" /> */}
        <input id="my-drawer-2" type="checkbox" className="drawer-toggle" />
        <div className="drawer-content flex flex-col items-center justify-center">
          {/* <!-- Page content here --> */}
          <label
            htmlFor="my-drawer-2"
            className="btn btn-primary drawer-button lg:hidden"
          >
            Open drawer
          </label>
          <div className="text-4xl font-bold place-content-center p-8 mx-auto">
            Welcome {username}!
          </div>
          {role === "analyst" ? (
            <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
              <Link href="/primary/signup/investor">
                <button className="btn btn-primary">Register Investor</button>
              </Link>
            </div>
          ) : null}
          <div
            style={{ position: "absolute", top: "20px", right: "50px" }}
            className="dropdown text-yellow-500"
          >
            <label tabIndex={0} className="btn btn-primary">
              Profile
            </label>
            <ul
              tabIndex={0}
              className="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52"
            >
              <li>
                <Link href="#">Settings</Link>
              </li>
              <li>
                <a onClick={() => logoutAuth()}>Logout</a>
              </li>
            </ul>
          </div>
        </div>
        <div className="drawer-side">
          <label htmlFor="my-drawer-2" className="drawer-overlay" />
          <ul className="menu p-4 w-80 bg-base-100 text-base-content">
            {/* <!-- Sidebar content here --> */}
            <li>
              <a>Logo Here</a>
            </li>
            <hr className="color-white" />
            <li>
              <a>Trading History</a>
            </li>
            <li>
              <a>Initiate Trading</a>
            </li>
            <li>
              <a>Exit Trading</a>
            </li>
            <li>
              <a>Analyst List</a>
            </li>
            <li>
              <a>Investor</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Home;
