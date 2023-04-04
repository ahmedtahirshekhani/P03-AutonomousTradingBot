import type { NextPage } from 'next';
import { useState, useEffect } from 'react';
import Stocks from '../../components/cards/stocks';
import Link from 'next/link';
import AnalystLayout from '../../components/layouts/AnalystLayout';

const ShowStocks: NextPage = () => {
	const [stocks, setStocks] = useState([]);
	const [tickers, setTickers] = useState([]);

	useEffect(() => {
		fetch('/api/v1/get-stock-tickers')
			.then((response) => response.json())
			.then((data) => {
				setStocks(data.data.names);
				setTickers(data.data.stock_tickers);
			})
			.catch((error) => {
				console.error('Error fetching stock data:', error);
			});
	}, []);

	const returnStockList = (stocks: any) => {
		const numberOfRows = Math.ceil(stocks.length / 5);

		return (
			<div>
				{Array.from({ length: numberOfRows }).map((_, rowIndex) => (
					<div
						key={rowIndex}
						className='flex flex-row justify-center mb-4'
					>
						{stocks
							.slice(rowIndex * 4, rowIndex * 4 + 4)
							.map((stock: string, index: number) => (
								<Stocks
									key={index}
									items={{
										title: stock,
										ticker: tickers.slice(
											rowIndex * 4,
											rowIndex * 4 + 4
										)[index],
									}}
								/>
							))}
					</div>
				))}
			</div>
		);
	};

	return (
		<AnalystLayout>
			<div className='hero min-h-screen bg-base-200'>
				<div className='hero-content text-center'>
					<div className='max-w-md'>
						<h1 className='text-5xl font-bold text-primary'>
							Available Stocks
						</h1>
						<div className='flex flex-wrap justify-center'>
							{returnStockList(stocks)}
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
