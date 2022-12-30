import type { NextPage } from 'next';
import BotCard from '../../components/cards/BotCard';

const AddInstance: NextPage = () => {
	return (
		<div className='hero min-h-screen'>
			<div className='hero-content text-center'>
				<div className='max-w-xl'>
					<h1 className='text-5xl font-bold'>
						Autonomous Trading Bot
					</h1>
				</div>

				<p className='py-6'></p>
				<div className='flex items-start ...'>
					{/* <div className="flex flex-row  ... "> */}
					<div className=' px-8'>
						<BotCard
							desc='Add a trading instance to the selected investor and enter the required information to start running the bot for the investor.'
							label='Add Trading Instance'
						/>
					</div>
					<div className='col-sm-6 '>
						<BotCard
							desc='View all currently running bots for the selected investor.'
							label='View Instances'
						/>
					</div>
				</div>
			</div>
		</div>
	);
};

export default AddInstance;
