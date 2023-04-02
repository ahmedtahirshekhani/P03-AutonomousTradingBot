import type { NextPage } from 'next';
import { useEffect, useState } from 'react';
import AssignBot from '../../components/cards/AssignBot';
import AnalystLayout from '../../components/layouts/AnalystLayout';
import { getAllInvestors } from '../../services/auth';

interface Investor {
	id: string;
	name: string;
	email: string;
	phone_number: string;
}

const ViewInvestors: NextPage = () => {
	const [investors, setInvestors] = useState<Array<Investor>>([]);

	useEffect(() => {
		getAllInvestors().then(res => {
			setInvestors(res.investors);
		});
	}, []);

	return (
		<AnalystLayout>
			<div className='hero min-h-screen'>
				<div className='hero-content text-center'>
					<div className='max-w-xl'>
						<h1 className='text-5xl font-bold text-primary'>Investors</h1>

						<p className='py-6'></p>
						<div className=''>
						{investors.length ? (
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
									{investors.map(i => (
										<AssignBot
											key={i.id}
											id={i.id}
											name={i.name}
											email={i.email}
											phone={i.phone_number}
										/>
									))}
								</tbody>
							</table>
							) : (
                <p className="text-2xl text-gray-500">No investors found.</p>
              )}
						</div>
					</div>
				</div>
			</div>
		</AnalystLayout>
	);
};

export default ViewInvestors;
