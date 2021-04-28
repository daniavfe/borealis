import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

//Modules
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { AppRoutingModule } from './modules/app-routing.module'


//Components
import { AppComponent } from './components/app-component/app.component';
import { DensityComponent } from './components/density-component/density.component';
import { MagnitudeListComponent } from './components/magnitude-list-component/magnitude-list.component';
import { MagnitudeFormComponent } from './components/magnitude-form-component/magnitude-form.component';
import { StationListComponent } from './components/station-list-component/station-list.component';
import { StationFormComponent } from './components/station-form-component/station-form.component';


//Services
import { DensityService } from './services/density.service';
import { MagnitudeService } from './services/magnitude.service';
import { FormsModule } from '@angular/forms';


@NgModule({
    declarations: [
        AppComponent,
        DensityComponent,
        MagnitudeListComponent,
        MagnitudeFormComponent,
        StationListComponent,
        StationFormComponent,
    ],
    imports: [
        BrowserModule,
        BrowserAnimationsModule,
        HttpClientModule,
        FormsModule,
        NgxChartsModule,
        AppRoutingModule
    ],
    providers: [DensityService, MagnitudeService],
    bootstrap: [AppComponent]
})
export class AppModule { }
