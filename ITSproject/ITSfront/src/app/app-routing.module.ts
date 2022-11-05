import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutUsComponent } from './about-us/about-us.component';
import { CountriesComponent } from './countries/countries.component';
import { MainPageComponent } from './main-page/main-page.component';
import { ResearchComponent } from './research/research.component';


const routes: Routes = [
  {path: '', component: MainPageComponent},
  {path: 'about', component: AboutUsComponent},
  {path: 'research', component: ResearchComponent},
  {path: 'countries', component: CountriesComponent},
  { path: '**', redirectTo: '/'},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
