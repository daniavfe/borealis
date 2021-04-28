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
  
  public getdensityData(years: number[], districts:number[], neighborhoods:number[], months:number[]): Observable<DensityData[]>{
    let year_list = years.length > 1? '?years='+years.join('&years=') : '';
    let district_list = districts.length > 1? '&districts='+districts.join('&districts='):'';
    return this.http.get<DensityData[]>(`${this.apiUrl}/density${year_list}${district_list}`);
  } 
}
