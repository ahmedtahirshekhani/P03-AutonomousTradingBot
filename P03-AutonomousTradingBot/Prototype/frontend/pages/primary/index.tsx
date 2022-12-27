import type { NextPage } from 'next';
import Link from 'next/link';

const Home: NextPage = () => {
	return (
		<div className="hero min-h-screen">
			<div className="hero-content text-center">
				<div className="max-w-xl">
					<h1 className="text-5xl font-bold">
						Autonomous Trading Bot
					</h1>
					<p className="py-6">
						
					</p>
                    <div className="flex flex-col w-full border-opacity-50">
                        <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
                            <Link href="/primary/login">
                                <button className="btn btn-primary">
                                    Already Registered - Login
                                </button>
                            </Link>
                        </div>
                        <div className="divider">OR</div>
                        <div className="grid h-20 card bg-base-300 rounded-box place-items-center">
                            <Link href="/primary/signup">
                                <button className="btn btn-primary">
                                    New User - Signup
                                </button>
                            </Link>
                        </div>

                        
                        <div style={{ position: "static", bottom: 5, width:"100%" }} className="text-sm breadcrumbs">
                                <ul>
                                    <li>
                                        <Link href="/">
                                            <a>Home</a>
                                        </Link>
                                    </li> 
                                    <li><p>Login/Signup</p></li> 
                                </ul>
                        </div>
                    </div>
				</div>
			</div>
		</div>
	);
};

export default Home;