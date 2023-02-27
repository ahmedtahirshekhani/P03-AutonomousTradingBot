import Link from 'next/link';

const BotCard = ({
	desc,
	label,
	pathname,
	investor_id,
}: {
	desc: string;
	label: string;
	pathname: string;
	investor_id: string;
}) => {
	return (
		<div className='card w-96 bg-base-100 shadow-xl h-48 border-slate-50'>
			<div className='card-body'>
				<h2 className='card-title'></h2>

				<div className='card-actions justify-end'>
					<p>{desc}</p>

					<Link
						href={{
							pathname: pathname,
							query: { investor_id: investor_id },
						}}
					>
						<button className='btn btn-primary place-content-center'>
							{label}
						</button>
					</Link>
				</div>
			</div>
		</div>
	);
};

export default BotCard;
