import type { NextPage } from "next";
import Link from "next/link";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { logout } from "../services/auth";

const Home: NextPage = () => {
  const router = useRouter();
  const [username, setUsername] = useState<string | undefined>("");
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

  useEffect(() => {
    if (localStorage.getItem("token") === null) {
      router.push("/primary/login");
    } else {
      const email = localStorage.getItem("email");
      const username = email?.split("@")[0];
      setUsername(username);
    }
  }, []);

  return (
    <div>
      <div className="text-4xl font-bold place-content-center p-8 mx-auto">
        Welcome {username}!
      </div>
      <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
        <Link href="/primary/signup/investor">
          <button className="btn btn-primary">Register Investor</button>
        </Link>
      </div>
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
  );
};

export default Home;
