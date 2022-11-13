import { Component, OnInit } from '@angular/core';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['../app.component.css']
})
export class MainPageComponent implements OnInit {

  constructor(private service: SharedService) { }

  CountryNameFilter:string="";

  totalLenght:any;
  page:number=1;

  selected:any = 2021;

  table_data_withoutFilter:any=[];
  row_table_data:any=[];
  table_data:any=[];

  ngOnInit(): void {
   
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
  

  

  refreshTable(year:number){
    
    this.service.getTable(year).subscribe(data=>{
      this.table_data = data;
      this.table_data_withoutFilter = data;
      console.log(this.table_data);
    });
  }

  sortResult(prop:any, asc:any){
    this.table_data = this.table_data_withoutFilter.sort(function(a:any,b:any){
      if(asc){
        return (a[prop]>b[prop])?1 : ((a[prop]<b[prop]) ?-1 :0);
      }else{
        return (b[prop]>a[prop])?1 : ((b[prop]<a[prop]) ?-1 :0);
      }
    });
  }
}