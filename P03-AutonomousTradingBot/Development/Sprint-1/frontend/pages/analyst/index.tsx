import type { NextPage } from 'next';
import { useRouter } from 'next/router';
import AnalystLayout from '../../components/layouts/AnalystLayout';

const AnalystDashboard: NextPage = () => {
	const router = useRouter();

	const handleRegisterInvestor = () => {
		router.push('/analyst/register-investor');
	};

	return (
		<AnalystLayout>
			<div className='hero min-h-screen bg-base-200'>
				<div className='hero-content text-center'>
					<div className='max-w-md'>
						<button
							className='btn btn-primary'
							onClick={handleRegisterInvestor}
						>
							Register Investor
						</button>
					</div>
				</div>
			</div>
		</AnalystLayout>
	);
};

export default AnalystDashboard;
