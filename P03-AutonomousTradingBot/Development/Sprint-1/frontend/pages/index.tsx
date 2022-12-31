import type { NextPage } from 'next';
import Link from 'next/link';

const Home: NextPage = () => {
	return (
		<div className='hero min-h-screen'>
			<div className='hero-content text-center'>
				<div className='max-w-xl'>
					<h1 className='text-5xl font-bold'>
						Autonomous Trading Bot
					</h1>
					<p className='py-6'>
						With recent advancements in deep learning frameworks and
						access to faster gpus, training complex models that can
						predict on time series data has opened new avenues to
						explore stock market trading. We plan on using models
						that have a memory component in them, such as LSTM (Long
						Short Term Memory) to make predictions and trades on the
						stock market.
					</p>
					<Link href='/login'>
						<button className='btn btn-primary'>
							Start investing!
						</button>
					</Link>
				</div>
			</div>
		</div>
	);
};

export default Home;
