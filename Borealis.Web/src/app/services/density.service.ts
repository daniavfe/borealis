import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class DensityService {

  apiUrl = environment.apiUrl;
  
  constructor(private http : HttpClient) { }

  //Dame datos del año X, mes X, distrito X, y barrio X
  
  public GetDensityAvailableData(): Observable<DensityAvailableData>{
    return this.http.get(`${this.apiUrl}/density/availableData`);
  } 

  public GetDensityData(year: number[], month: number[], district:number[], barrio: number[]){

  }

}
