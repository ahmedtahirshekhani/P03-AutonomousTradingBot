import type { NextPage } from 'next';
import Link from 'next/link';
import AnalystLayout from '../../components/layouts/AnalystLayout';

const AnalystDashboard: NextPage = () => {
	return (
		<AnalystLayout>
			<div className='hero min-h-screen bg-base-200'>
				<div className='hero-content text-center'>
					<div className='max-w-md flex flex-col'>
						<Link href='/analyst/view-investors'>
							<button className='btn btn-primary'>
								View Investors
							</button>
						</Link>

						<div className='h-4'></div>

						<Link href='/analyst/register-investor'>
							<button className='btn btn-primary'>
								Register Investor
							</button>
						</Link>
					</div>
				</div>
			</div>
		</AnalystLayout>
	);
};

export default AnalystDashboard;
