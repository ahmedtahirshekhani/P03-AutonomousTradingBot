import axios from 'axios';
import { NextPage } from 'next';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';
import AnalystLayout from '../../../components/layouts/AnalystLayout';
import InvestorLayout from '../../../components/layouts/InvestorLayout';

interface BotPerformance {
	id: string;
	initialInvestment: string;
	currentValue: string;
	profit: boolean;
	percent: string;
	gain: string;
}

const TradeTable: React.FC<{}> = () => {
	const router = useRouter();

	const [botPerformance, setBotPerformance] = useState<BotPerformance>();

	useEffect(() => {
		let data = JSON.stringify({
			bot_id: router.query.bot_id,
		});

		let config = {
			method: 'post',
			maxBodyLength: Infinity,
			url: '/api/v1/get-bot',
			headers: {
				Authorization: `Bearer ${localStorage.getItem('access_token')}`,
				'Content-Type': 'application/json',
			},
			data: data,
		};

		axios
			.request(config)
			.then((response) => {
				const data = response.data;
				setBotPerformance({
					id: data.data.id,
					initialInvestment: data.data.initial_balance,
					currentValue: data.data.current_balance,
					profit:
						parseFloat(data.data.current_balance) >
						parseFloat(data.data.initial_balance),
					percent:
						(
							((parseFloat(data.data.current_balance) -
								parseFloat(data.data.initial_balance)) /
								parseFloat(data.data.initial_balance)) *
							100
						).toFixed(2) + '%',
					gain: (
						parseFloat(data.data.current_balance) -
						parseFloat(data.data.initial_balance)
					).toFixed(2),
				});
			})
			.catch((error) => {
				console.log(error);
			});
	}, []);

	return (
		<div className='hero min-h-screen'>
			<div className='hero-content text-center'>
				<div className=''>
					<h1 className='text-5xl font-bold text-primary'>
						Bot Performance
					</h1>

					<p className='py-6'></p>
					<div className=''>
						<table className='table w-full custom-table'>
							<thead>
								<tr className='text-primary'>
									<th>ID</th>
									<th>Initial Investment(PKR)</th>
									<th>Current Value(PKR)</th>
									<th>In Profit ?</th>
									<th>
										{botPerformance?.profit
											? 'Gain (PKR)'
											: 'Loss(PKR)'}{' '}
									</th>
									<th>
										{botPerformance?.profit
											? '% Gain'
											: '% Loss'}{' '}
									</th>
								</tr>
							</thead>
							<tbody>
								<tr>
									<td>{botPerformance?.id}</td>
									<td>{botPerformance?.initialInvestment}</td>
									<td>{botPerformance?.currentValue}</td>
									<td>
										{botPerformance?.profit ? 'Yes' : 'No'}
									</td>
									<td>{botPerformance?.gain}</td>
									<td>{botPerformance?.percent}</td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>
			</div>
		</div>
	);
};

const Home: NextPage = () => {
	const router = useRouter();

	return (
		<InvestorLayout>
			<TradeTable />
		</InvestorLayout>
	);
};

export default Home;
