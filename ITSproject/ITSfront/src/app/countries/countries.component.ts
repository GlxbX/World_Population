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

  selected:any = 2021;

  /*geomap*/
  row_data_geomap:any=[];
  mid_data_geomap: any=[];

  /*world linechart */
  row_data_wlc:any=[];
  mid_data_wlc: any=[];



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
    this.refreshWorldLineChart()
    this.refreshTable(this.selected);
    this.totalLenght = this.table_data.lenght;
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
      
      this.row_data_geomap = data;
      this.mid_data_geomap = JSON.parse(this.row_data_geomap);
  
      
    });
  }
  refreshWorldLineChart(){
    this.service.getWorldLineChart().subscribe(data=>{
      
      this.row_data_wlc = data;
      this.mid_data_wlc = JSON.parse(this.row_data_wlc);
  
      
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
