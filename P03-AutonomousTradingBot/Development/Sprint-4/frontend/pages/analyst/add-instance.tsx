import type { NextPage } from 'next';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';
import BotCard from '../../components/cards/BotCard';
import AnalystLayout from '../../components/layouts/AnalystLayout';
import { getAllInvestors } from '../../services/auth';


interface Investor {
	id: string;
	name: string;
	email: string;
	phone_number: string;
}

const getInvestorNameById = (investorId: string, investors: Investor[]): string => {
	const investor = investors.find((i: Investor) => i.id === investorId);
	return investor?.name ?? 'Unknown';
  };

const AddInstance: NextPage = () => {

	

	
	const router = useRouter();
	const [investors, setInvestors] = useState<Investor[]>([]);

	useEffect(() => {
		getAllInvestors().then(data => {
		  setInvestors(data.investors);
		});
	  }, []);

	  const investorId = router.query.investor_id as string;
const investorName = getInvestorNameById(investorId, investors);
	

	return (
		<AnalystLayout>
			<div className='hero min-h-screen'>
				<div className='hero-content text-center'>
					<div className='max-w-xl'>
					<h1 className='text-5xl font-bold text-primary mb-4'>
            Investor: {investorName}
          </h1>
					</div>

					<div className='grid grid-cols-1 gap-8 md:grid-cols-2'>
						<div className='px-8'>
							<BotCard
                desc={`Add a trading instance for ${investorName} and enter the required information to start running the bot for the investor.`}
				label='Add Trading Instance'
								pathname={'/analyst/instance-params'}
								investor_id={router.query.investor_id as string}
							/>
						</div>
						<div className='px-8'>
							<BotCard
                desc={`View all currently running bots for ${investorName}.`}
								label='View Instances'
								pathname={'/analyst/view-instances'}
								investor_id={router.query.investor_id as string}
							/>
						</div>
					</div>
				</div>
			</div>
		</AnalystLayout>
	);
};

export default AddInstance;