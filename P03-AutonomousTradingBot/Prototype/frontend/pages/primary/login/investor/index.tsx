import type { NextPage } from "next";
import Link from "next/link";
import React from "react";
import { login } from "../../../../services/auth";
import { useRouter } from "next/router";
const Home: NextPage = () => {
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [displayErr, setDisplayErr] = React.useState(false);
  const router = useRouter();

  const loginAuth = () => {
    if (email != null && password != null) {
      login(email, password, "investor")
        .then((res) => {
          // console.log("Status", res.stat);
          if (res.status === 202 && res.data.success === true) {
            router.push("/primary/dashboard");
            localStorage.setItem("email", email);
          } else {
            setDisplayErr(true);
          }
        })
        .catch((err) => {
          console.log("Error", err);
          setDisplayErr(true);
        });
    }
  };

  return (
    <div className="hero min-h-screen">
      <div className="hero-content text-center">
        <div className="max-w-xl">
          <h1 className="text-5xl font-bold">Autonomous Trading Bot</h1>
          <p className="py-6"></p>
          <div className="flex flex-col space-y-10 ...">
            {displayErr ? (
              <div className="alert alert-error shadow-lg">
                <div>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="stroke-current flex-shrink-0 h-6 w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  <span>Error! Incorrect Login Credentials.</span>
                </div>
              </div>
            ) : null}
            <div className="midnight text-tahiti">
              <div className="flex flex-col w-full border-opacity-50">
                <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
                  <div className="form-control">
                    <label className="input-group">
                      <span>Email</span>
                      <input
                        type="text"
                        placeholder="example@example.com"
                        className="input input-bordered"
                        onChange={(e) => setEmail(e.target.value)}
                      />
                    </label>
                  </div>
                </div>

                <div className="divider"></div>

                <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
                  <div className="form-control">
                    <label className="input-group">
                      <span>Password</span>
                      <input
                        type="password"
                        placeholder="Enter Password Here"
                        className="input input-bordered"
                        onChange={(e) => setPassword(e.target.value)}
                      />
                    </label>
                  </div>
                </div>
              </div>

              <label className="label">
                <div className="underline underline-offset-1 ... link link-warning">
                  <a href="#" className="text-base ">
                    Forgot password?
                  </a>
                </div>
              </label>

              <div className="pt-6 ...">
                <button className="btn btn-warning" onClick={() => loginAuth()}>
                  Login
                </button>
              </div>

              <div
                style={{ position: "static", bottom: 5, width: "100%" }}
                className="text-sm breadcrumbs"
              >
                <ul>
                  <li>
                    <Link href="/">Home</Link>
                  </li>
                  <li>
                    <Link href="/primary">Login</Link>
                  </li>

                  <li>Investor</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
