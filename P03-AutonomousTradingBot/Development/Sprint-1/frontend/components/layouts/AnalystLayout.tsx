import { useRouter } from 'next/router';
import { FC, ReactNode } from 'react';
import AnalystNavbar from '../navbars/AnalystNavbar';

export interface IAnalystLayout {
	children: ReactNode;
}

const AnalystLayout: FC<IAnalystLayout> = ({ children }) => {
	const router = useRouter();

	return (
		<div>
			<AnalystNavbar />

			{children}
		</div>
	);
};

export default AnalystLayout;
