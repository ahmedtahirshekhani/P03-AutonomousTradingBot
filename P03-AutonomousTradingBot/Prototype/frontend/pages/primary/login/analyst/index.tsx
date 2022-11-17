import type { NextPage } from 'next';
import Link from 'next/link';
import React from 'react';
//import {login} from './services/auth';

const Home: NextPage = () => {
    const [email, setEmail] = React.useState("");
    const [password, setPassword] = React.useState("");

	return (
		<div className="hero min-h-screen">
			<div className="hero-content text-center">
				<div className="max-w-xl">
					<h1 className="text-5xl font-bold">
						Autonomous Trading Bot
					</h1>
					<p className="py-6">
						
					</p>
                        <div className="flex flex-col space-y-10 ...">
                            <div className="midnight text-tahiti">
                                <div className="flex flex-col w-full border-opacity-50">
                                    <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
                                        <div className="form-control">
                                            <label className="input-group">
                                                <span>Email</span>
                                                <input type="text" placeholder="example@example.com" className="input input-bordered" onChange = {(e)=>setEmail(e.target.value)}/>
                                            </label>
                                        </div>
                                    </div>

                                    <div className="divider"></div>
                                    
                                    <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
                                    
                                        <div className="form-control">
                                            <label className="input-group">
                                                <span>Password</span>
                                                <input type="password" placeholder="Enter Password Here" className="input input-bordered" onChange = {(e)=>setPassword(e.target.value)}/>
                                            </label>
                                        </div>
                                    </div>
                                </div>

                                <label className="label">
                                    <div  className='underline underline-offset-1 ... link link-warning'>
                                        <a href="#" className="text-base ">
                                            Forgot password?
                                        </a>
                                    </div>
                                </label>

                                <div className="pt-6 ...">
                                    <Link href="/primary/dashboard">
                                        {/* <button className="btn btn-warning" onClick={()=>login(email, password, "analyst")}>Login</button> */}
                                        <button className="btn btn-warning">Login</button>
                                    </Link>
                                </div>


                                <div style={{ position: "static", bottom: 5, width:"100%" }} className="text-sm breadcrumbs">
                                    <ul>
                                        <li>
                                            <Link href="/">
                                                <a>Home</a>
                                            </Link>
                                        </li> 
                                        <li>
                                            <Link href="/primary">
                                                <a>Login/Signup</a>
                                            </Link>
                                        </li> 
                                        <li>
                                            <Link href="/primary/login">
                                                <a>Login</a>
                                            </Link>
                                        </li>
                                        <li>
                                            <p>Analyst</p>
                                        </li>

                                        
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