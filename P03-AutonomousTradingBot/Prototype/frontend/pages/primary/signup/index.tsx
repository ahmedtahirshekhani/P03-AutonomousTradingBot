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

                    <div className="mt-9 ...">
                        <div className="flex flex-col space-y-10 ...">
                            <div className="dropdown ">
                                <label tabIndex={0} className="btn m-1">Sign Up As:</label>
                                <ul tabIndex={0} className="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52">
                                    <li>
                                        <Link href="/primary/signup/analyst">
                                            <a>Analyst</a>
                                        </Link>
                                    </li>
                                    <li>
                                        <Link href="/primary/signup/investor">
                                            <a>Investor</a>
                                        </Link>
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

