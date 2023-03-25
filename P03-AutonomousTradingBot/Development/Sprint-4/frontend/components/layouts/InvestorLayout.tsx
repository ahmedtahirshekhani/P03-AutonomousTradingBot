import { useRouter } from 'next/router';
import { FC, ReactNode } from 'react';
import InvestorNavbar from '../navbars/InvestorNavbar';

export interface IInvestorLayout {
	children: ReactNode;
}

const InvestorLayout: FC<IInvestorLayout> = ({ children }) => {
	const router = useRouter();

	return (
		<div>
			<InvestorNavbar />

			{children}
		</div>
	);
};

export default InvestorLayout;
