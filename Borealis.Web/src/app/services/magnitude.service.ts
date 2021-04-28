import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Magnitude } from '../types/magnitude';
import { PFOCollection } from '../types/pfoCollection';

@Injectable({
    providedIn: 'root'
})
export class MagnitudeService {

    constructor(private http: HttpClient) { }

    //Dame datos del año X, mes X, distrito X, y barrio X

    public createMagnitudeFromParams(id: number, name: string, formula: string, measurementUnit: string): Observable<number> {
        return this.http.post<number>(`api/pollution/magnitude/`, { id: id, name: name, formula: formula, measurementUnit: measurementUnit });
    }
    public createMagnitude(magnitude: Magnitude): Observable<number> {
        return this.http.post<number>(`api/pollution/magnitude/`, magnitude);
    }

    public getMagnitudes(page: number, perPage: number, orderBy: string, orderByDescending: boolean): Observable<PFOCollection<Magnitude>> {
        let orderByDescendingText = orderByDescending ? '&orderByDescending' : ''
        return this.http.get<PFOCollection<Magnitude>>(`api/pollution/magnitude/?page=${page}&perPage=${perPage}&orderBy=${orderBy}${orderByDescendingText}`);
    }
}
