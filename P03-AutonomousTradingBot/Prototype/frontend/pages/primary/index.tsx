import type { NextPage } from "next";
import Link from "next/link";

const Home: NextPage = () => {
  return (
    <div className="hero min-h-screen">
      <div className="hero-content text-center">
        <div className="max-w-xl">
          <h1 className="text-5xl font-bold">Autonomous Trading Bot</h1>
          <p className="py-6"></p>
          <div className="w-full border-opacity-50">
            <div className="dropdown ">
              <label tabIndex={0} className="btn m-1 btn-primary">
                Login As:
              </label>
              <ul
                tabIndex={0}
                className="dropdown-content menu p-2 shadow bg-base-100 rounded-box"
              >
                <li>
                  <Link href="/primary/login/analyst">Analyst</Link>
                </li>
                <li>
                  <Link href="/primary/login/investor">Investor</Link>
                </li>
              </ul>
            </div>

            <div
              style={{ bottom: 5, width: "100%" }}
              className="text-sm breadcrumbs"
            >
              <ul>
                <li>
                  <Link href="/">
                    <a>Home</a>
                  </Link>
                </li>
                <li>Login</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
