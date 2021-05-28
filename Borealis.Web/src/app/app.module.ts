import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

//Modules
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MaterialModule } from './modules/material.module'
import { RoutingModule } from './modules/routing.module'

//Views
import { DensityView } from './views/density/density';
import { MagnitudeView } from './views/magnitude/magnitude';
import { StationView } from './views/station/station';
import { HolidayView } from './views/holiday/holiday';
import { ReportView } from './views/report/report';
import { TimelineView } from './views/timeline/timeline';
import { MeasurementView } from './views/measurement/measurement';
import { MainView } from './views/main/main';

//Components
import { MagnitudeFormComponent } from './components/magnitude-form-component/magnitude-form.component';
import { StationFormComponent } from './components/station-form-component/station-form.component';
import { EventListComponent } from './components/event-list-component/event-list.component';


//Services
import { DensityService } from './services/density.service';
import { MagnitudeService } from './services/magnitude.service';
import { StationService } from './services/station.service';
import { HolidayService } from './services/holiday.service';
import { EventService } from './services/event.service';
import { ReportService } from './services/report.service';
import { TimelineService } from './services/timeline.service';
import { MeasurementService } from './services/measurement.service';
import { HeaderComponent } from './components/header/header.component';
import { PaginatorComponent } from './components/paginator/paginator.component';


@NgModule({
    declarations: [
        MainView,
        DensityView,
        MagnitudeView,
        MagnitudeFormComponent,
        StationView,
        StationFormComponent,
        EventListComponent,
        HolidayView,
        ReportView,
        TimelineView,
        MeasurementView,
        HeaderComponent,
        PaginatorComponent
    ],
    imports: [
        BrowserModule,
        BrowserAnimationsModule,
        HttpClientModule,
        FormsModule,
        NgxChartsModule,
        FlexLayoutModule,
        RoutingModule,
        MaterialModule
    ],
    providers: [
        DensityService, 
        MagnitudeService, 
        StationService, 
        HolidayService, 
        EventService,
        ReportService,
        TimelineService,
        MeasurementService
    ],
    bootstrap: [MainView]
})
export class AppModule { }
