import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router'; // CLI imports router

import { DensityComponent } from '../components/density-component/density.component';
import { EventListComponent } from '../components/event-list-component/event-list.component';
import { MagnitudeListComponent } from '../components/magnitude-list-component/magnitude-list.component';
import { StationListComponent } from '../components/station-list-component/station-list.component';

const routes: Routes = [
    { path: 'magnitude/list', component: MagnitudeListComponent },
    { path: 'station/list', component: StationListComponent },
    { path: 'event/list', component: EventListComponent },
    { path: 'density', component: DensityComponent },
    { path: '', redirectTo: '/magnitude/list', pathMatch: 'full' },
];

// configures NgModule imports and exports
@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }