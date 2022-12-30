import type { NextPage } from 'next';
import AssignBot from '../../components/cards/AssignBot';

const ViewInvestors: NextPage = () => {
	return (
		<div className='hero min-h-screen'>
			<div className='hero-content text-center'>
				<div className='max-w-xl'>
					<h1 className='text-5xl font-bold'>
						Autonomous Trading Bot
					</h1>
					<h1 className='text-xl font-bold pt-6 '>Investors</h1>

					<p className='py-6'></p>
					<div className=''>
						<table className='table w-full'>
							<thead>
								<tr className='text-primary'>
									<th></th>
									<th>Name </th>
									<th>Email Address</th>
									<th>Phone Number</th>
									<th></th>
								</tr>
							</thead>
							<tbody>
								<AssignBot
									name='Ali'
									email='ali@gmail.com'
									phone='02135526879'
								/>
								<AssignBot
									name='Sheikhani'
									email='sheikhani@gmail.com'
									phone='02135526879'
								/>
								<AssignBot
									name='Suleiman'
									email='suleiman@gmail.com'
									phone='02135526879'
								/>
							</tbody>
						</table>
					</div>
				</div>
			</div>
		</div>
	);
};

export default ViewInvestors;
