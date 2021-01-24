import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { DensityData } from '../types/densityData';
import { PFOCollection } from '../types/pfoCollection';

@Injectable({
  providedIn: 'root'
})
export class DensityService {

  constructor(private http : HttpClient) { }

  public GetDensityData(page, perPage, orderBy, orderByDescending):Observable<PFOCollection<DensityData>>{
    return this.http.get<PFOCollection<DensityData>>("");
  }
}
