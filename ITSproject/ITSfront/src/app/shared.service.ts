import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import {Observable}  from 'rxjs';
import { tap, map } from 'rxjs/operators';


const httpOptions = {
  headers: new HttpHeaders({
    'Content-type': 'application/json'
  })
};


@Injectable({
  providedIn: 'root'
})
export class SharedService {

  readonly APIUrl = "http://127.0.0.1:8000";
  
  constructor(private http: HttpClient) { }

  getGeoMap():Observable<{}>{
    return this.http.get<any[]>(this.APIUrl + '/geomap/');
  }

  getTable(value: any):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl +`/table/t/${value}`);
  }

  login(username:string,password:string) {
    return this.http.post<any>(this.APIUrl+'/auth/login',
    {username, password}, httpOptions).pipe(
      map(user=>{
      if (user && user.token) {
        localStorage.setItem("currentUser", JSON.stringify(user));
      }
      return user;
    })
    );
  };

  reg(username:string,email:string,password:string) {
    return this.http.post<any>(this.APIUrl+'/auth/reg',
    {username, email ,password}, httpOptions).pipe(
      map(user=>{
      if (user && user.token) {
        localStorage.setItem("currentUser", JSON.stringify(user));
      }
      return user;
    })
    );
  };


  logout() {
    localStorage.removeItem('currentUser')
  };
}