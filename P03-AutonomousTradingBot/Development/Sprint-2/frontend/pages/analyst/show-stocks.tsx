import type { NextPage } from "next";
import Stocks from "../../components/cards/stocks";
import stockdata from "../../components/cards/stockdetails.json"
import { error } from "console";



interface Stockdata {
  [key: string]: any;
}





const ShowStocks: NextPage = () => {

  // const result = Object.keys(stockdata).map((key) => {
  //   return { [key]: stockdata[key as keyof typeof stockdata] };
  // });

  // //console.log(result)
  // Object.entries(stockdata.data).forEach(
  //   ([key, value]) => console.log(key,value)
    
  // );


  const returnStockList = (stocks : any) =>{
      let temp: any[] = []
      let data = stocks['data']
      let keys = Object.keys(data);
      console.log("Data", data)
      keys.forEach((k: any, i: number) => {
      
        temp.push(<Stocks items = {data[k]} key= {i}/>)
      });

   
      return temp



    }

  return (
    <div>
      <div className="flex flex-row flex-wrap">
      {returnStockList(stockdata)}      
    </div>
    </div>
  );
};

export default ShowStocks;
