import Image from 'next/image';

interface Dictionary {
	[key: string]: any;
}

const Stocks = ({ items }: Dictionary) => {
	return (
		<div>
			<div className='card w-96 bg-base-100 shadow-xl'>
				<figure>
					<Image
						src={`${items.results.branding.logo_url}?apiKey=YFTHviueJWslQBln4lPLiSlAch9byi2z`}
						alt="Sorry, we're working on it!"
						width={250}
						height={250}
					/>
					<img />
				</figure>
				<div className='card-body'>
					<h2 className='card-title'>
						{items.results.name}
						<div className='badge badge-secondary'>
							{items.results.ticker}
						</div>
					</h2>
					<p>
						{' '}
						Works in {items.results.sic_description} Visit website
						to learn more.
						<a href={items.results.homepage_url} target='_blank'>
							Here
						</a>
					</p>
					<div className='card-actions justify-end'></div>
				</div>
			</div>
		</div>
	);
};

export default Stocks;
