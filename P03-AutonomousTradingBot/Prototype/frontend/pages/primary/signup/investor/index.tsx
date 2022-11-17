import type { NextPage } from "next";
import Link from "next/link";
import { useState, useEffect } from "react";
import { useRouter } from "next/router";
import { registerInvestor } from "../../services/auth";

import Swal from "sweetalert2";

const Home: NextPage = () => {
  const [NTN, setNTN] = useState(0);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [address, setAddress] = useState("");
  const [analyst_email, setAnalystEmail] = useState("");
  const router = useRouter();

  const regInvestor = () => {
    registerInvestor(NTN, email, analyst_email, name, phone, address)
      .then((res) => {
        Swal.fire({
          title: "Investor successfully registered",
          text:
            "Email: " +
            res.investor.email +
            " Password: " +
            res.plain_text_password,
          icon: "success",
          confirmButtonText: "Return to Dashboard",
        }).then((result) => {
          if (result.isConfirmed) {
            router.push("/primary/dashboard");
          }
        });
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    const email = localStorage.getItem("email")!;
    setAnalystEmail(email);
  }, []);
  return (
    <div className="hero min-h-screen">
      <div className="hero-content text-center">
        <div className="max-w-xl">
          <h1 className="text-5xl font-bold">Autonomous Trading Bot</h1>
          <div className="flex flex-col space-y-10 ...">
            <div className="midnight text-tahiti">
              <div className="flex flex-col w-full border-opacity-50">
                <div className="mt-6 ...">
                  <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
                    <div className="form-control">
                      <label className="input-group">
                        <span>NTN</span>
                        <input
                          type="number"
                          placeholder="0123456"
                          className="input input-bordered"
                          onChange={(e) => {
                            const NTN = e.target.value;

                            setNTN(parseInt(NTN));
                          }}
                        />
                      </label>
                    </div>
                  </div>
                </div>

                <div className="divider"></div>

                <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
                  <div className="form-control">
                    <label className="input-group">
                      <span>Name</span>
                      <input
                        type="text"
                        placeholder="Enter Name Here"
                        className="input input-bordered"
                        onChange={(e) => setName(e.target.value)}
                      />
                    </label>
                  </div>
                </div>
                <div className="divider"></div>

                <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
                  <div className="form-control">
                    <label className="input-group">
                      <span>Email Address</span>
                      <input
                        type="text"
                        placeholder="abc@gmail.com"
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
                      <span>Phone Number</span>
                      <input
                        type="text"
                        placeholder="02131234567"
                        className="input input-bordered"
                        onChange={(e) => setPhone(e.target.value)}
                      />
                    </label>
                  </div>
                </div>

                <div className="divider"></div>

                <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
                  <div className="form-control">
                    <label className="input-group">
                      <span>Residential Address</span>
                      <input
                        type="text"
                        placeholder="1234, Main St. Avenue"
                        className="input input-bordered"
                        onChange={(e) => setAddress(e.target.value)}
                      />
                    </label>
                  </div>
                </div>
              </div>

              <div className="pt-6 ...">
                <button
                  className="btn btn-primary"
                  onClick={() => regInvestor()}
                >
                  Register
                </button>
              </div>

              <div
                style={{ position: "static", bottom: 0, width: "100%" }}
                className="text-sm breadcrumbs"
              >
                <ul>
                  <li>
                    <Link href="/primary/dashboard">Dashboard</Link>
                  </li>
                  <li>Register Investor</li>
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
