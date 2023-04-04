import type { NextPage } from 'next';
import Link from 'next/link';
import { useRouter } from 'next/router';
import AnalystLayout from '../../components/layouts/AnalystLayout';
import InvestorLayout from '../../components/layouts/InvestorLayout';


const InvestorDashboard: NextPage = () => {
  const router = useRouter();





  return (
	
    <InvestorLayout>
      <div className='hero min-h-screen bg-base-200'>

        <div className='hero-content text-center'>
          <div className='max-w-md flex flex-col'>
            
				<div>
					<div className='h-4'></div>
					<Link href='/investor/showbots'>
                <button className='btn btn-primary btn-wide'>
                  View Bots
                </button>
              </Link>
			  <div className='h-4'></div>

			  <Link href='/investor/show-trained-stocks'>
				<button className='btn btn-primary  btn-wide'>
				  Show Trained Stocks
				</button>
			  </Link>
			  </div>
          </div>
        </div>
      </div>
    </InvestorLayout>
  );
};

export default InvestorDashboard;
