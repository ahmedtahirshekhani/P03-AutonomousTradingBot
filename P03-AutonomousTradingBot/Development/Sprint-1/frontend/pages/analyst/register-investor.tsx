import type { NextPage } from 'next';
import Link from 'next/link';
import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import Swal from 'sweetalert2';
import { registerInvestor } from '../../services/auth';
import AnalystLayout from '../../components/layouts/AnalystLayout';

const RegisterInvestor: NextPage = () => {
	const [NTN, setNTN] = useState('');
	const [name, setName] = useState('');
	const [email, setEmail] = useState('');
	const [phone, setPhone] = useState('');
	const [address, setAddress] = useState('');
	const [analyst_email, setAnalystEmail] = useState('');
	const router = useRouter();

	const regInvestor = () => {
		registerInvestor(NTN, email, analyst_email, name, phone, address)
			.then(res => {
				Swal.fire({
					title: 'Investor successfully registered',
					text:
						'Email: ' +
						res.investor.email +
						' Password: ' +
						res.plain_text_password,
					icon: 'success',
					confirmButtonText: 'Return to Dashboard',
				}).then(result => {
					if (result.isConfirmed) {
						router.push('/primary/dashboard');
					}
				});
				console.log(res);
			})
			.catch(err => {
				console.log(err);
			});
	};

	useEffect(() => {
		const email = localStorage.getItem('email')!;
		setAnalystEmail(email);
	}, []);

	return (
		<AnalystLayout>
			<div className='hero min-h-screen'>
				<div className='hero-content text-center'>
					<div className='max-w-xl'>
						<h1 className='mb-6 text-5xl font-bold'>
							Register Investor
						</h1>

						<div className='flex flex-col'>
							<div className='midnight text-tahiti'>
								<div className='card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100'>
									<div className='card-body'>
										<div className='form-control'>
											<label className='label'>
												<span className='label-text'>
													NTN
												</span>
											</label>
											<input
												type='text'
												placeholder='231351651'
												className='input input-bordered'
												onChange={e =>
													setNTN(e.target.value)
												}
											/>
										</div>

										<div className='form-control'>
											<label className='label'>
												<span className='label-text'>
													Name
												</span>
											</label>
											<input
												type='text'
												placeholder='John Doe'
												className='input input-bordered'
												onChange={e =>
													setName(e.target.value)
												}
											/>
										</div>

										<div className='form-control'>
											<label className='label'>
												<span className='label-text'>
													Email
												</span>
											</label>
											<input
												type='text'
												placeholder='someone@investor.com'
												className='input input-bordered'
												onChange={e =>
													setEmail(e.target.value)
												}
											/>
										</div>

										<div className='form-control'>
											<label className='label'>
												<span className='label-text'>
													Phone Number
												</span>
											</label>
											<input
												type='text'
												placeholder='+92 333 3333777'
												className='input input-bordered'
												onChange={e =>
													setPhone(e.target.value)
												}
											/>
										</div>

										<div className='form-control'>
											<label className='label'>
												<span className='label-text'>
													Residential Address
												</span>
											</label>
											<input
												type='text'
												placeholder='Street, Block Number, City, Country'
												className='input input-bordered'
												onChange={e =>
													setAddress(e.target.value)
												}
											/>
										</div>

										<div className='form-control mt-6'>
											<button
												className='btn btn-primary'
												onClick={regInvestor}
											>
												Register
											</button>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</AnalystLayout>
	);
};

export default RegisterInvestor;
