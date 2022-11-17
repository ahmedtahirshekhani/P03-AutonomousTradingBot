import type { NextPage } from 'next';
import Link  from 'next/link';

const Home: NextPage = () => {
	return (

        <div>
            <div style={{ position:"absolute", top:"20px", right:"50px" }} className="dropdown text-yellow-500">
            <label tabIndex={0} className="btn btn-primary">Profile</label>
                <ul tabIndex={0} className="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52">
                    <li>
                        <a>
                            <Link href="#">
                                Settings
                            </Link>
                        </a>
                    </li>
                    <li>
                        <a>
                            <Link href="/">
                                Logout
                            </Link>
                        </a>
                    </li>
                </ul>
            </div>

            





        </div>

        



        
	);
};

export default Home;

