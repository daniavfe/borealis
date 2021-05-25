import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router'; // CLI imports router

import { DensityView } from '../views/density/density';
import { EventListComponent } from '../components/event-list-component/event-list.component';
import { HolidayView } from '../views/holiday/holiday';
import { MagnitudeView } from '../views/magnitude/magnitude';
import { MeasurementView} from '../views/measurement/measurement';
import { ReportView } from '../views/report/report';
import { StationView} from '../views/station/station';
import { TimelineView } from '../views/timeline/timeline';

const routes: Routes = [
    { path: 'magnitude', component: MagnitudeView },
    { path: 'station', component: StationView },
    { path: 'event', component: EventListComponent },
    { path: 'holiday', component: HolidayView },
    { path: 'timeline', component: TimelineView },
    { path: 'density', component: DensityView },
    { path: 'report', component: ReportView },
    { path: 'measurement', component: MeasurementView },
    { path: '', redirectTo: '/measurement', pathMatch: 'full' },
];

// configures NgModule imports and exports
@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class RoutingModule { }