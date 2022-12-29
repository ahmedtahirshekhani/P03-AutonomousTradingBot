import Link from "next/link";

const BotCard = ({ img, label }: { img: string; label: string }) => {
  return (
    <div className="card w-96 bg-base-100 shadow-xl">
      <figure>
        <img src={img} />
      </figure>
      <div className="card-body">
        <h2 className="card-title">{label}</h2>
        <div className="card-actions justify-end">
          <label htmlFor="my-modal-3" className="btn btn-primary">
            Add Trading Instance
          </label>

          {/* Put this part before </body> tag */}
          <input type="checkbox" id="my-modal-3" className="modal-toggle" />
          <div className="modal">
            <div className="modal-box relative">
              <label
                htmlFor="my-modal-3"
                className="btn btn-sm btn-circle absolute right-2 top-2"
              >
                ✕
              </label>
              <div className="form-control w-full max-w-xs">
                <label className="label">
                  <span className="label-text">Amount ?</span>
                </label>
                <input
                  type="text"
                  placeholder="amount"
                  className="input input-bordered w-full max-w-xs"
                />
                <label className="label"></label>
              </div>
              <div className="form-control w-full max-w-xs">
                <label className="label">
                  <span className="label-text">Risk Threshold ? (%)</span>
                </label>
                <input
                  type="percentage"
                  placeholder="risk %"
                  className="input input-bordered w-full max-w-xs"
                />
                <label className="label"></label>
              </div>
              <div className="form-control w-full max-w-xs">
                <label className="label">
                  <span className="label-text">Minimum Target Return ? (%)</span>
                </label>
                <input
                  type="text"
                  placeholder="return %"
                  className="input input-bordered w-full max-w-xs"
                />
                <label className="label"></label>
              </div>
              <p className="py-4">
              </p>
              <button className="btn btn-primary">Submit</button>

            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BotCard;
