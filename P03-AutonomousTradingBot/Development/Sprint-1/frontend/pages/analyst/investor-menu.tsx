import type { NextPage } from 'next';
import Link from 'next/link';
import AnalystLayout from '../../components/layouts/AnalystLayout';

const InvestorMenu: NextPage = () => {
	return (
		<AnalystLayout>
			<div className='hero min-h-screen'>
				<div className='hero-content text-center'>
					<div className='max-w-xl'>
						<h1 className='text-5xl font-bold'>
							Autonomous Trading Bot
						</h1>
						<p className='py-6'></p>
						<Link href='/analyst/addInstance'>
							<button className='btn btn-primary'>
								Add Bot Instance
							</button>
						</Link>

						<p className='py-6'></p>
						<Link href='/primary'>
							<button className='btn btn-primary'>
								Show currently running bots
							</button>
						</Link>
					</div>
				</div>
			</div>
		</AnalystLayout>
	);
};

export default InvestorMenu;
