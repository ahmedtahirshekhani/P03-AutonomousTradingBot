import { useState } from 'react';
import axios from 'axios';

interface StocksProps {
	items: {
		title: string;
		ticker: string;
	};
}

const Stocks: React.FC<StocksProps> = ({ items }) => {
	const [isLoading, setIsLoading] = useState(false);

	const trainModel = async () => {
		setIsLoading(true);

		const config = {
			method: 'get',
			url: '/api/v1/train-model',
			headers: {
				'Content-Type': 'application/json',
			},
			params: {
				ticker: items.ticker,
			},
		};

		try {
			await axios(config);

			console.log('Training successful!');
		} catch (error) {
			console.error(error);
		} finally {
			setIsLoading(false);
		}
	};

	return (
		<div className='card shadow-md w-70 h-60 p-4 m-2'>
			<div className='card-body'>
				<h2 className='card-title'>{items.title}</h2>
				<div className='flex flex-row justify-between items-center mt-4'>
					<button
						className='btn btn-wide btn-primary'
						onClick={trainModel}
						disabled={isLoading}
					>
						{isLoading ? 'Loading...' : 'Train Stock'}
					</button>
				</div>
			</div>
		</div>
	);
};

export default Stocks;
