interface Dictionary {
  [key: string]: any;
}

const Stocks = ({ items }: Dictionary) => {
  return (
    <div>
      <div className="card w-96 bg-base-100 shadow-xl">
        <figure>
          <img src={items.results.logo_url} alt="Sorry, we're working on it!" />
        </figure>
        <div className="card-body">
          <h2 className="card-title">
            {items.results.name}
            <div className="badge badge-secondary">{items.results.ticker}</div>
          </h2>
          <p>
            {" "}
            Works in {items.results.sic_description} Visit website to learn
            more.
            <a href={items.results.homepage_url} target="_blank">
              Here
            </a>
          </p>
          <div className="card-actions justify-end"></div>
        </div>
      </div>
    </div>
  );
};

export default Stocks;
