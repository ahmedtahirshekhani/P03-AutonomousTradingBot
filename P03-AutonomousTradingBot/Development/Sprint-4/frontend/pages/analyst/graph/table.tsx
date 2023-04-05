import { NextPage } from 'next';
import React, { useEffect, useState } from 'react';
import AnalystLayout from '../../../components/layouts/AnalystLayout';
import Link from 'next/link';
import axios from 'axios';
import { useRouter } from 'next/router';

interface Trade {
	id: string;
	amount: string;
	start_price: string;
	started_at: string;
	trade_type: string;
	ended_at: string;
	end_price: string;
	is_profit: boolean;
}

interface TradeTableProps {}

const TradeTable: React.FC<TradeTableProps> = () => {
	const router = useRouter();

	const [trades, setTrades] = useState<
		Array<{
			id: string;
			amount: number;
			start_price: number;
			started_at: number;
			trade_type: string;
			ended_at: number;
			end_price: number;
			is_profit: string;
		}>
	>();

	const [APIdata, setAPIdata] = useState();

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
				setTrades(data.data.trades);
				setAPIdata(data);
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
						Trade History
					</h1>

					<p className='py-6'></p>
					<div className=''>
						{trades?.length ? (
							<>
								<table className='table w-full custom-table'>
									<thead>
										<tr className='text-primary'>
											<th>ID</th>
											<th>Amount</th>
											<th>Start Price</th>
											<th>Started At</th>
											<th>Trade Type</th>
											<th>Ended At</th>
											<th>End Price</th>
											<th>Profit ?</th>
										</tr>
									</thead>
									<tbody>
										{trades.map((trade) => (
											<tr key={trade.id}>
												<td>{trade.id}</td>
												<td>{trade.amount}</td>
												<td>{trade.start_price}</td>
												<td>{trade.started_at}</td>
												<td>
													{trade.trade_type == '1'
														? 'Put'
														: 'Call'}
												</td>
												<td>{trade.ended_at}</td>
												<td>{trade.end_price}</td>
												<td>
													{trade.is_profit
														? 'Yes'
														: 'No'}
												</td>
											</tr>
										))}
									</tbody>
								</table>
								<div className='text-center text-xl py-8'>
									<Link href='../graph'>
										<button
											className='btn btn-wide btn-primary'
											style={{ marginRight: '10px' }}
										>
											<h1>View Graph</h1>
										</button>
									</Link>
									<Link
										href={{
											pathname: '../graph/performance',
											query: {
												bot_id: router.query.bot_id,
											},
										}}
									>
										<button className='btn btn-wide btn-primary'>
											<h1>View Current Performance</h1>
										</button>
									</Link>
								</div>
							</>
						) : (
							<p>No trades found.</p>
						)}
					</div>
				</div>
			</div>
		</div>
	);
};

const Home: NextPage = () => {
	return (
		<AnalystLayout>
			<TradeTable />
		</AnalystLayout>
	);
};

export default Home;
