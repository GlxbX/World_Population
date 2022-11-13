import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { CountriesComponent } from './countries/countries.component';
import { MainPageComponent } from './main-page/main-page.component';



const routes: Routes = [
  {path: '', component: MainPageComponent},
  
 
  {path: 'countries', component: CountriesComponent},
  { path: '**', redirectTo: '/'},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
