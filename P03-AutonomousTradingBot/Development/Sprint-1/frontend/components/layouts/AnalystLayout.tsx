import { useRouter } from 'next/router';
import { FC, ReactNode, useEffect, useState } from 'react';
import AnalystNavbar from '../navbars/AnalystNavbar';

export interface IAnalystLayout {
	children: ReactNode;
}

const AnalystLayout: FC<IAnalystLayout> = ({ children }) => {
	const router = useRouter();

	const [showErrorMessage, setShowErrorMessage] = useState(false);
	const [errorMessage, setErrorMessage] = useState('');

	useEffect(() => {
		setTimeout(() => {
			setShowErrorMessage(false);
		}, 5000);
	}, [showErrorMessage]);

	return (
		<div>
			<AnalystNavbar />

			{children}

			{showErrorMessage ? (
				<div className='toast'>
					<div className='alert alert-error'>
						<div>
							<span>{errorMessage}</span>
						</div>
					</div>
				</div>
			) : null}
		</div>
	);
};

export default AnalystLayout;
