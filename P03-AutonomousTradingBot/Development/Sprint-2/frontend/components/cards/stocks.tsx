

interface Dictionary {
  [key: string]: any;
}


const Stocks = ({items} : Dictionary ) => {

  return (
    <div>
      

      <div className="carousel carousel-center rounded-box">
      <div className="card w-96 bg-base-100 shadow-xl ">
  <figure><img src={items.results.logo_url} alt="Shoes" /></figure>
      <div className="card-body">
    <h2 className="card-title">
      {items.results.name}
      <div className="badge badge-secondary">{items.results.ticker}</div>
    </h2>
    <p> Visit website to learn more. 
    <a href={items.results.homepage_url} target="_blank">
          <h2>Here</h2>
        </a>
        
      </p>
    <div className="card-actions justify-end ">
      <div className="badge badge-outline ">{items.results.sic_description}</div> 
    </div>
  </div>
  </div>
  </div>
</div>

      
    
      
    
  )
  
}

export default Stocks