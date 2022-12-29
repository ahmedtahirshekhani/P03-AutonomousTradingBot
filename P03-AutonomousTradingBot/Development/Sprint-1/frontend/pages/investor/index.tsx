import type { NextPage } from 'next';
import InvestorLayout from '../../components/layouts/InvestorLayout';

const InvestorDashboard: NextPage = () => {
	return (
		<InvestorLayout>
			<div className='hero min-h-screen bg-base-200'>
				<div className='hero-content text-center'>
					<div className='max-w-md'></div>
				</div>
			</div>
		</InvestorLayout>
	);
};

export default InvestorDashboard;
