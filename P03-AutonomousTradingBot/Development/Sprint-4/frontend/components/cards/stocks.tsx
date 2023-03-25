import Image from 'next/image';

interface Dictionary {
	[key: string]: any;
}


interface StocksProps {
	items: {
	  title: string;
	  imageUrl: string;
	  description: string;
	};
  }

// const Stocks = ({ items }: Dictionary) => {
// 	return (
// 		<div className="stock-container">
// 			<div className='card w-96 bg-base-100 shadow-xl'>
// 				<figure>
// 					<Image
// 						src={`${items.results.branding.logo_url}?apiKey=YFTHviueJWslQBln4lPLiSlAch9byi2z`}
// 						alt="Sorry, we're working on it!"
// 						width={250}
// 						height={250}
// 					/>
// 					<img />
// 				</figure>
// 				<div className='card-body'>
// 					<h2 className='card-title'>
// 						{items.results.name}
// 						<div className='badge badge-secondary'>
// 							{items.results.ticker}
// 						</div>
// 					</h2>
// 					<p>
// 						{' '}
// 						Works in {items.results.sic_description} Visit website
// 						to learn more.
// 						<a href={items.results.homepage_url} target='_blank'>
// 							Here
// 						</a>
// 					</p>
// 					<div className='card-actions justify-end'></div>
// 				</div>
// 			</div>
// 		</div>
// 	);
// };


const Stocks: React.FC<StocksProps> = ({ items }) => {
	return (
		
		<div className="card shadow-md w-80 h-80 p-4 m-4">
		<div className="card-body">
		  <div className="flex flex-row justify-between items-center">
			<h2 className="card-title">{items.title}</h2>
			<img className="w-30 h-20" src={items.imageUrl} alt={items.title} />
		  </div>
		  <p className="mt-2">{items.description}</p>
		</div>
	  </div>
	);
  };



export default Stocks;
