import Link from 'next/link';

const InvestorNavbar = () => {
	const handleLogout = () => {
		return;
	};

	return (
		<div className='navbar bg-base-100'>
			<div className='flex-1'>
				<div className='btn btn-ghost normal-case text-xl'>
					<Link href='/investor'>Investor Dashboard</Link>
				</div>
			</div>
			<div className='flex-none'>
				<ul className='menu menu-horizontal px-1'>
					{/* <li>
						<a>Item 1</a>
					</li> */}
					<li tabIndex={0}>
						<a>
							Profile
							<svg
								className='fill-current'
								xmlns='http://www.w3.org/2000/svg'
								width='20'
								height='20'
								viewBox='0 0 24 24'
							>
								<path d='M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z' />
							</svg>
						</a>
						<ul className='p-2 bg-base-100'>

							<li>
								<Link href='/login'>Logout</Link>
							</li>
						</ul>
					</li>
				</ul>
			</div>
		</div>
	);
};

export default InvestorNavbar;
