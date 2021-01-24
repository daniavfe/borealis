import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

//Modules
import { AppRoutingModule } from './modules/app-routing.module'

//Components
import { AppComponent } from './app-component/app.component';


//Services
import { DensityService } from './services/density.service';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [DensityService],
  bootstrap: [AppComponent]
})
export class AppModule { }
