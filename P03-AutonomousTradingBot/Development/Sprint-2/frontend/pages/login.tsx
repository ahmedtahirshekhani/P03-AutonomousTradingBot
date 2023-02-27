import type { NextPage } from 'next';
import { useRouter } from 'next/router';
import { useState } from 'react';
import ErrorMessageAlert from '../components/cards/ErrorMessageAlert';
import { login } from '../services/auth';

const Login: NextPage = () => {
	const router = useRouter();

	// Forcing a redoply of vercel

	const [email, setEmail] = useState<String>('');
	const [password, setPassword] = useState<String>('');
	const [showErrorMessage, setShowErrorMessage] = useState('');

	const handleLogin = () => {
		setShowErrorMessage('');

		login(email, password)
			.then(res => {
				router.push(`/${res.data.role}`);
			})
			.catch(e => {
				setShowErrorMessage(e.response.data.message);
			});
	};

	return (
		<div className='hero min-h-screen bg-base-200'>
			<div className='hero-content flex-col lg:flex-row-reverse'>
				<div className='text-center lg:text-left lg:ml-8'>
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
						</div>
						<div className='form-control mt-6'>
							<button
								className='btn btn-primary'
								onClick={handleLogin}
							>
								Login
							</button>
						</div>

						{/* Error prompt */}
						<ErrorMessageAlert
							showErrorMessage={showErrorMessage}
						/>
					</div>
				</div>
			</div>
		</div>
	);
};

export default Login;
