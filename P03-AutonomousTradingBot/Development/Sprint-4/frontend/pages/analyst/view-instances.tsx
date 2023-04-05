import type { NextPage } from 'next';
import Link from 'next/link';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';
import Swal from 'sweetalert2';
import AnalystLayout from '../../components/layouts/AnalystLayout';
import {
	getAllBots,
	initiateBotExecution,
	terminateBot,
} from '../../services/auth';

interface Bot {
	id: string;
	state: string;
	risk_appetite: string;
	target_return: string;
	stocks_ticker: string;
	initial_balance: string;
}

const Home: NextPage = () => {
	const router = useRouter();
	const investor_id = router.query.investor_id;

	const [bots, setBots] = useState<Array<Bot>>([]);

	useEffect(() => {
		if (!investor_id) return;

		getAllBots(investor_id).then((res) => {
			setBots(res.bots);
		});
	}, [investor_id]);

	const handleStartClick = async (bot_id: string) => {
		const response = await initiateBotExecution(bot_id);
		console.log(response);
		Swal.fire(response.message);
		setBots((prevBots) =>
			prevBots.map((bot) =>
				bot.id === bot_id ? { ...bot, state: 'Started' } : bot
			)
		);
	};

	const handleTerminateClick = async (bot_id: string) => {
		const response = await terminateBot(bot_id);
		Swal.fire(response.message);
		setBots((prevBots) =>
			prevBots.map((bot) =>
				bot.id === bot_id ? { ...bot, state: 'Terminated' } : bot
			)
		);
	};

	return (
		<AnalystLayout>
			<div className='hero min-h-screen bg-base-200'>
				<div className='hero-content text-center'>
					<div className='max-w-4xl mx-auto '>
						<h1 className='text-5xl font-bold mb-6 text-primary'>
							Current Instances
						</h1>

						{bots.length > 0 ? (
							<div className='grid gap-4 grid-cols-1 md:grid-cols-2 justify-items-start'>
								{bots.map((b, i) => (
									<div
										key={i}
										className='p-4 card w-96 bg-blue text-neutral-content border-primary'
									>
										<div className='card-body items-center text-center'>
											<h2 className='card-title font-bold text-primary'>
												Bot ID: {b.id}
											</h2>
											<p className='font-bold'>
												Configuration Parameters:
											</p>
											<ul>
												<li className='text-info'>
													State: {b.state}
												</li>
												<li>
													Amount Invested:{' '}
													{b.initial_balance}
												</li>
												<li>
													Risk Appetite:{' '}
													{b.risk_appetite}
												</li>
												<li>
													Target Return:{' '}
													{b.target_return}%
												</li>
												<li>
													Stock: {b.stocks_ticker}
												</li>
											</ul>
											<div className='card-actions justify-end'>
												<div className='btn-container'>
													<div className='flex justify-end'>
														<button
															onClick={() =>
																handleStartClick(
																	b.id
																)
															}
															className='btn btn-primary mr-2'
														>
															Start
														</button>
														<button
															onClick={() =>
																handleTerminateClick(
																	b.id
																)
															}
															className='btn btn-error mr-2'
														>
															Terminate
														</button>
														<Link
															href={{
																pathname:
																	'/analyst/graph/table',
																query: {
																	bot_id: b.id,
																},
															}}
														>
															<button className='btn btn-accent'>
																View Trades
															</button>
														</Link>
													</div>
												</div>
											</div>
										</div>
									</div>
								))}
							</div>
						) : (
							<p>
								No bot instances currently found for this
								investor.
							</p>
						)}
					</div>
				</div>
			</div>
		</AnalystLayout>
	);
};

export default Home;
