import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

//Modules
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { AppRoutingModule } from './modules/app-routing.module'
import { FlexLayoutModule } from '@angular/flex-layout';


//Components
import { AppComponent } from './components/app-component/app.component';
import { DensityComponent } from './components/density-component/density.component';
import { MagnitudeListComponent } from './components/magnitude-list-component/magnitude-list.component';
import { MagnitudeFormComponent } from './components/magnitude-form-component/magnitude-form.component';
import { StationListComponent } from './components/station-list-component/station-list.component';
import { StationFormComponent } from './components/station-form-component/station-form.component';
import { EventListComponent } from './components/event-list-component/event-list.component';
import { HolidayListComponent } from './components/holiday-list-component/holiday-list.component';
import { ReportComponent } from './components/report-component/report.component';
import { TimelineListComponent } from './components/timeline-list-component/timeline-list.component';
import { SelectorComponent } from './components/selector-component/selector.component';
import { MeasurementComponent } from './components/measurement-component/measurement.component';

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


@NgModule({
    declarations: [
        AppComponent,
        DensityComponent,
        MagnitudeListComponent,
        MagnitudeFormComponent,
        StationListComponent,
        StationFormComponent,
        EventListComponent,
        HolidayListComponent,
        ReportComponent,
        TimelineListComponent,
        SelectorComponent,
        MeasurementComponent,
        HeaderComponent
    ],
    imports: [
        BrowserModule,
        BrowserAnimationsModule,
        HttpClientModule,
        FormsModule,
        NgxChartsModule,
        AppRoutingModule,
        FlexLayoutModule 
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
    bootstrap: [AppComponent]
})
export class AppModule { }
