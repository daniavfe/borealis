import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router'; // CLI imports router

import { MagnitudeListComponent } from '../components/magnitude-list-component/magnitude-list.component';

const routes: Routes = [
  { path: 'magnitude/list', component: MagnitudeListComponent },
  { path: '',   redirectTo: '/magnitude/list', pathMatch: 'full' }, 
]; 

// configures NgModule imports and exports
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }