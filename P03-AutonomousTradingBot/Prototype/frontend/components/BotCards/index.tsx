import Link from "next/link";
import {useState} from 'react';


const BotCard = ({ desc, label }: { desc: string, label: string }) => {
  return (
    <div className="card w-96 bg-base-100 shadow-xl h-48">
      <div className="card-body">
        <h2 className="card-title"></h2>
        <div className="card-actions justify-end">
            <p>{desc}</p>
            <Link href="../bot/instanceParams">
          <div className="btn btn-primary place-content-center">
            {label}
          </div>
          </Link>

         
          
        </div>
      </div>
    </div>
  );
};

export default BotCard;
