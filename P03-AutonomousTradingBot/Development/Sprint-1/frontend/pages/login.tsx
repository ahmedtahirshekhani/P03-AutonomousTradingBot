import type { NextPage } from 'next';
import { useState } from 'react';

const Login: NextPage = () => {
	const [email, setEmail] = useState<String>('');
	const [password, setPassword] = useState<String>('');

	const handleLogin = () => {};

	return (
		<div className='hero min-h-screen bg-base-200'>
			<div className='hero-content flex-col lg:flex-row-reverse'>
				<div className='text-center lg:text-left'>
					<h1 className='text-5xl font-bold'>Login now!</h1>
					<p className='py-6'>
						Start investing and enjoy autonomous trading benefits!
					</p>
				</div>
				<div className='card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100'>
					<div className='card-body'>
						<div className='form-control'>
							<label className='label'>
								<span className='label-text'>Email</span>
							</label>
							<input
								type='text'
								placeholder='email'
								className='input input-bordered'
								onChange={e => setEmail(e.target.value)}
							/>
						</div>
						<div className='form-control'>
							<label className='label'>
								<span className='label-text'>Password</span>
							</label>
							<input
								type='password'
								placeholder='password'
								className='input input-bordered'
								onChange={e => setPassword(e.target.value)}
							/>
							{/* <label className='label'>
								<a
									href='#'
									className='label-text-alt link link-hover'
								>
									Forgot password?
								</a>
							</label> */}
						</div>
						<div className='form-control mt-6'>
							<button
								className='btn btn-primary'
								onClick={handleLogin}
							>
								Login
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	);
};

export default Login;
