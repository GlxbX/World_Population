import { Component, OnInit } from '@angular/core';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-countries',
  templateUrl: './countries.component.html',
  styleUrls: ['../app.component.css']
})
export class CountriesComponent implements OnInit {

  constructor(private service: SharedService) { }

  CountryNameFilter:string="";

  totalLenght:any;
  page:number=1;

  selected:any = 2017;

  row_data:any=[];
  mid_data: any=[];
  parsed_data: any =[];
  
 

  value: any = 1800;
  options: any = {
    floor: 1800,
    ceil: 2021
  };



  table_data_withoutFilter:any=[];
  row_table_data:any=[];
  table_data:any=[];

  ngOnInit(): void {
    this.refreshGeomap();
    // this.refreshTable(this.selected);
    // this.totalLenght = this.table_data.lenght;
  }



  searchCountry(){
    var CountryNameFilter =this.CountryNameFilter;
    this.table_data = this.table_data_withoutFilter.filter(function (el:any){
      return el.country.toString().toLowerCase().includes(
        CountryNameFilter.toString().trim().toLowerCase()
      )
    });
  }
  

  refreshGeomap(){
    this.service.getGeoMap().subscribe(data=>{
      
      this.row_data = data;
      this.mid_data = JSON.parse(this.row_data);
      // this.parsed_data = JSON.parse(this.mid_data[this.value-1800]);
      
    });
  }

  


  refreshTable(year:number){
    
    this.service.getTable(year).subscribe(data=>{
      this.table_data = data;
      this.table_data_withoutFilter = data;
    });
  }

  sortResult(prop:any, asc:any){
    this.table_data = this.table_data_withoutFilter.sort(function(a:any,b:any){
      if(asc){
        return (a[prop]>b[prop])?1 : ((a[prop]<b[prop]) ?-1 :0);
      }else{
        return (b[prop]>a[prop])?1 : ((b[prop]<a[prop]) ?-1 :0);
      }
    })
  }
 
  
}
