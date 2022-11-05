import { Component, OnInit } from '@angular/core';
import { SharedService } from '../shared.service';
import {  FormGroup, FormControl, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { ConfirmedValidator } from '../confirmed.validator';


declare var window:any;

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['../app.component.css']
})
export class HeaderComponent implements OnInit {

  loginform : any = FormGroup;
  regform : any = FormGroup;


  formModal1: any;
  formModal2: any;

  constructor(private service: SharedService) { }

  ngOnInit(): void {
    this.formModal1 = new window.bootstrap.Modal(
      document.getElementById("exampleModal")
    )
    this.formModal2 = new window.bootstrap.Modal(
      document.getElementById("exampleModal1")
    )

    this.regform =  new FormGroup({
      username: new FormControl(''),
      email: new FormControl(''),
      password: new FormControl('',Validators.required),
      confirm_password: new FormControl('',Validators.required)})

    this.loginform =  new FormGroup({
      username: new FormControl(''),
      password: new FormControl(''),
  })
  }
  get login() {
    return this.loginform.controls;
  };

  get reg() {
    return this.regform.controls;
  };



  OnLogin(){
    console.log()
    this.service.login(this.login.username.value , this.login.password.value).pipe(first()).subscribe(data=>{
      console.log(data);
    })
   };

  //  OnReg(){
  //   console.log()
  //   this.service.reg(this.reg.username.value, this.reg.email.value, this.reg.password.value).pipe(first()).subscribe(data=>{
  //     console.log(data);
  //   })
  //  };
  last_data :any =[];
  isSuccessful = false;
  isSignUpFailed = false;
  errorMessage = '';
   OnReg(): void {
    
    this.service.reg(this.reg.username.value, this.reg.email.value, this.reg.password.value).subscribe(
      data => {
        console.log(data);
        this.isSuccessful = true;
        this.isSignUpFailed = false;
        this.last_data =data;
      },
      err => {
        this.errorMessage = err.error.message;
        this.isSignUpFailed = true;
      }
    );
   };
  

  openLogin(){
    this.formModal1.show();
  }
  openRegister(){
    this.formModal2.show();
  }


}
