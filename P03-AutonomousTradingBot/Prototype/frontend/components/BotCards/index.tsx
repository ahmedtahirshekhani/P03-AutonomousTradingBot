import Link from "next/link";
import { useState } from "react";
import AssignBot from "../assign_bot";

const BotCard = ({ desc, label }: { desc: string; label: string }) => {
  
  return (
    <div className="card w-96 bg-base-100 shadow-xl h-48 border-slate-50">
      <div className="card-body">
        <h2 className="card-title"></h2>

        {label === "Add Trading Instance" ? (
          <div className="card-actions justify-end">
            <p>{desc}</p>

            <Link href="/bot/instanceParams">
              <button className="btn btn-primary place-content-center">
                {label}
              </button>
            </Link>
          </div>
        ) : null}




{label === "View Instances" ? (
          <div className="card-actions justify-end">
            <p>{desc}</p>

            <Link href="/bot/viewInstances">
              <button className="btn btn-primary place-content-center">
                {label}
              </button>
            </Link>
          </div>
        ) : null}





      </div>
    </div>
  );
};

export default BotCard;
