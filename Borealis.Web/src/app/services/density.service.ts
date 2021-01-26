import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { DensityData } from '../types/densityData';

@Injectable({
  providedIn: 'root'
})
export class DensityService {

  apiUrl = environment.apiUrl;
  
  constructor(private http : HttpClient) { }

  //Dame datos del año X, mes X, distrito X, y barrio X
  
  public getdensityData(): Observable<DensityData[]>{
    return this.http.get<DensityData[]>(`${this.apiUrl}/density`);
  } 


}
