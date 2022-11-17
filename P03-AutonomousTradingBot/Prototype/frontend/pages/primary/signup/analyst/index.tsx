import type { NextPage } from 'next';
import Link  from 'next/link';

const Home: NextPage = () => {
	return (
		<div className="hero min-h-screen">
			<div className="hero-content text-center">
				<div className="max-w-xl">
					<h1 className="text-5xl font-bold">
						Autonomous Trading Bot
					</h1>
					<div className="flex flex-col space-y-10 ...">
                        <div className="midnight text-tahiti">
                            <div className="flex flex-col w-full border-opacity-50">
                                
                                <div className="mt-9 ...">
                                    
                                        <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
                                            <div className="form-control">
                                                <label className="input-group">
                                                    <span>Name</span>
                                                    <input type="text" placeholder="Ali" className="input input-bordered" />
                                                </label>
                                            </div>
                                        </div>
                                </div>

                                <div className="divider"></div>
                                
                                <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
                                
                                    <div className="form-control">
                                        <label className="input-group">
                                            <span>Address</span>
                                            <input type="text" placeholder="LUMS" className="input input-bordered" />
                                        </label>
                                    </div>
                                </div>

                                <div className="divider"></div>

                                <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
                                
                                    <div className="form-control">
                                        <label className="input-group">
                                            <span>Email Address</span>
                                            <input type="text" placeholder="abc@gmail.com" className="input input-bordered" />
                                        </label>
                                    </div>
                                </div>

                                <div className="divider"></div>

                                <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
                                
                                    <div className="form-control">
                                        <label className="input-group">
                                            <span>Phone Number</span>
                                            <input type="text" placeholder="02131234567" className="input input-bordered" />
                                        </label>
                                    </div>
                                </div>
                            </div>

                            <div className="pt-6 ...">
                                <button className="btn btn-warning">Signup</button>
                            </div>

                            <div style={{ position: "static", bottom: 0, width:"100%" }} className="text-sm breadcrumbs">
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
                                        <Link href="/primary/signup">
                                            <a>Signup</a>
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

