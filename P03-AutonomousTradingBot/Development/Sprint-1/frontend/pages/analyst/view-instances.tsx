import type { NextPage } from 'next';
import AnalystLayout from '../../components/layouts/AnalystLayout';

const Home: NextPage = () => {
	return (
		<AnalystLayout>
			<div className='hero min-h-screen bg-base-200'>
				<div className='hero-content text-center'>
					<div className='max-w-md'>
						<h1 className='text-5xl font-bold'>
							Current Instances
						</h1>
						<p className='py-6'></p>
					</div>
				</div>
			</div>
		</AnalystLayout>
	);
};

export default Home;
