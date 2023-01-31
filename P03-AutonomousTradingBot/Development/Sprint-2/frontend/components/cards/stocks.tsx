

interface Dictionary {
  [key: string]: any;
}


const Stocks = ({items} : Dictionary ) => {

  return (
    <div>
      <h1>Hello</h1>
      <div>{items.results.cik}</div>

      <div className="card w-96 bg-base-100 shadow-xl">
  <figure><img src="/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg" alt="Shoes" /></figure>
      <div className="card-body">
    <h2 className="card-title">
      {items.results.name}
      <div className="badge badge-secondary">{items.results.ticker}</div>
    </h2>
    <p> Visit website to learn more. 
    <a href={items.results.homepage_url} target="_blank">
          Here
        </a>
        
      </p>
    <div className="card-actions justify-end">
      <div className="badge badge-outline">{items.results.sic_description}</div> 
    </div>
  </div>
  </div>
</div>

      
    
      
    
  )
  
}

export default Stocks