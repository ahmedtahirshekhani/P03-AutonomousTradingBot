import { useEffect, useState } from 'react';
import axios from 'axios';

interface StocksProps {
	items: {
		title: string;
		ticker: string;
	};
}

const Stocks: React.FC<StocksProps> = ({ items }) => {
	const [isLoading, setIsLoading] = useState(false);
	const [isTrained, setIsTrained] = useState(false);
	const [trainedStocks, setTrainedStocks] = useState<string[]>([]);

	useEffect(() => {
		const fetchTrainedStocks = async () => {
			try {
				const response = await axios.get('/api/v1/get-trained-stock-tickers');
				if (response.data && response.data.data && Array.isArray(response.data.data.trained_stock_tickers)) {
					setTrainedStocks(response.data.data.trained_stock_tickers);
				} else {
					setTrainedStocks([]);
				}
			} catch (error) {
				console.error(error);
				setTrainedStocks([]);
			}
		};
		

		
	
		fetchTrainedStocks();
	}, []);
	
	useEffect(() => {
		setIsTrained(trainedStocks.includes(items.ticker));
	}, [trainedStocks, items.ticker]);
	
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
			setIsTrained(true);
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
					{!isTrained ? (
						<button
							className='btn btn-wide btn-primary'
							onClick={trainModel}
							disabled={isLoading}
						>
							{isLoading ? 'Training...' : 'Train'}
						</button>
					) : (
						<span className='text-primary text-xl px-6'>Trained Successfully</span>
					)}
				</div>
			</div>
		</div>
	);
	
};

export default Stocks;
