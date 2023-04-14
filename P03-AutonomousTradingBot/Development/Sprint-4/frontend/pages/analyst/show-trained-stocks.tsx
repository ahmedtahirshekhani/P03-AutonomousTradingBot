import type { NextPage } from 'next';
import { useState, useEffect } from 'react';
import Stocks from '../../components/cards/stocks';
import Link from 'next/link';
import AnalystLayout from '../../components/layouts/AnalystLayout';
import axios from 'axios';

const ShowStocks: NextPage = () => {
	const [stocks, setStocks] = useState([]);

	useEffect(() => {
		const getStocks = async () => {
			let data = '';

			let config = {
				method: 'get',
				maxBodyLength: Infinity,
				url: '/api/v1/get-trained-stock-tickers',
				headers: {},
				data: data,
			};

			try {
				const response = await axios.request(config);
				setStocks(response.data.data.trained_stock_tickers);
			} catch (error) {
				console.error('Error fetching stock data:', error);
			}
		};

		getStocks();
	}, []);

	return (
		<AnalystLayout>
			<div className='hero min-h-screen bg-base-200'>
				<div className='hero-content text-center'>
					<div className='max-w-lg'>
						<h1 className='text-5xl font-bold text-primary'>
							Trained Stock Tickers
						</h1>
						<div className='flex flex-wrap justify-center'>
							{stocks?.map((s, k) => (
								<div key={k} className='my-2 card w-96 bg-neutral text-neutral-content'>
									<div className='card-body items-center text-center'>
										<h2 className='card-title'>{s}</h2>
									</div>
								</div>
							))}
						</div>
						<Link href='/analyst'>
							<button className='btn btn-wide btn-primary'>
								<h1>Back to Main Page</h1>
							</button>
						</Link>
					</div>
				</div>
			</div>
		</AnalystLayout>
	);
};

export default ShowStocks;
