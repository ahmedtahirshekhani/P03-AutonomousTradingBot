import Image from "next/image";

interface StocksProps {
  items: {
    title: string;
  };
}

const Stocks: React.FC<StocksProps> = ({ items }) => {
  return (
    <div className="card shadow-md w-60 h-40 p-4 m-2">
      <div className="card-body">
        <div className="flex flex-row justify-between items-center">
          <h2 className="card-title">{items.title}</h2>
        </div>
      </div>
    </div>
  );
};

export default Stocks;
