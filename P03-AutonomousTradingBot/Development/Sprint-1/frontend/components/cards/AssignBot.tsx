import Link from 'next/link';

const AssignBot = ({
	id,
	name,
	email,
	phone,
}: {
	id: string;
	name: string;
	email: string;
	phone: string;
}) => {
	return (
		<tr className='hover'>
			<th className='text-primary'>*</th>
			<td>{name}</td>
			<td>{email}</td>
			<td>{phone}</td>
			<td>
				<div className='dropdown dropdown-right '>
					<label className=' bg-black text-primary'>
						<Link
							href={{
								pathname: '/analyst/add-instance',
								query: { investor_id: id },
							}}
						>
							<button className='btn btn-primary'>Select</button>
						</Link>
					</label>
				</div>
			</td>
		</tr>
	);
};

export default AssignBot;
