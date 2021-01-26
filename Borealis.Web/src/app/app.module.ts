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


//Services
import { DensityService } from './services/density.service';

@NgModule({
  declarations: [
    AppComponent,
    DensityComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    NgxChartsModule,
    AppRoutingModule
  ],
  providers: [DensityService],
  bootstrap: [AppComponent]
})
export class AppModule { }
