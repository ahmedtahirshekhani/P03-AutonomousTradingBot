import type { NextPage } from 'next';
import Link from 'next/link';
import AnalystLayout from '../../components/layouts/AnalystLayout';

const AnalystDashboard: NextPage = () => {
	return (
		<AnalystLayout>
			<div className='hero min-h-screen bg-base-200'>
				<div className='hero-content text-center'>
					<div className='max-w-md flex flex-col'>
						<div className='btn btn-primary'>
							<Link href='/analyst/view-investors'>
								View Investors
							</Link>
						</div>

						<div className='h-4'></div>

						<div className='btn btn-primary'>
							<Link href='/analyst/register-investor'>
								Register Investor
							</Link>
						</div>
					</div>
				</div>
			</div>
		</AnalystLayout>
	);
};

export default AnalystDashboard;
