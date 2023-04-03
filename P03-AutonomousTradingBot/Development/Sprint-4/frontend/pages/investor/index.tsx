import type { NextPage } from 'next';
import Link from 'next/link';
import { useRouter } from 'next/router';
import AnalystLayout from '../../components/layouts/AnalystLayout';


const AnalystDashboard: NextPage = () => {
  const router = useRouter();
  const isAnalyst = router.pathname.includes('/analyst');




  return (
    <AnalystLayout>
      <div className='hero min-h-screen bg-base-200'>
        <div className='hero-content text-center'>
          <div className='max-w-md flex flex-col'>
            {isAnalyst ? (
              <>
                <Link href='/analyst/view-investors'>
                  <button className='btn btn-primary'>
                    View Investors
                  </button>
                </Link>

                <div className='h-4'></div>

                <Link href='/analyst/register-investor'>
                  <button className='btn btn-primary'>
                    Register Investor
                  </button>
                </Link>

                <div className='h-4'></div>

                <Link href='/analyst/show-stocks'>
                  <button className='btn btn-primary'>
                    Show Stocks
                  </button>
                </Link>

                <div className='h-4'></div>

                <Link href='/analyst/show-trained-stocks'>
                  <button className='btn btn-primary'>
                    Show Trained Stocks
                  </button>
                </Link>
              </>
            ) : (
				<div>
					<div className='h-4'></div>
					<Link href='/analyst/view-investors'>
                <button className='btn btn-primary btn-wide'>
                  View Stocks
                </button>
              </Link>
			  <div className='h-4'></div>

			  <Link href='/analyst/show-trained-stocks'>
				<button className='btn btn-primary  btn-wide'>
				  Show Trained Stocks
				</button>
			  </Link>
			  </div>
            )}
          </div>
        </div>
      </div>
    </AnalystLayout>
  );
};

export default AnalystDashboard;
