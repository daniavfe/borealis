import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { HttpHelper } from '../helpers/httpHelper';
import { MagnitudeDto } from '../types/magnitude/magnitudeDto';
import { PFOCollection } from '../types/pfoCollection';

@Injectable({
    providedIn: 'root'
})
export class MagnitudeService {

    constructor(private http: HttpClient) { }

    public createMagnitudeFromParams(id: number, name: string, formula: string, measurementUnit: string): Observable<number> {
        return this.http.post<number>('api/magnitude/', { id: id, name: name, formula: formula, measurementUnit: measurementUnit });
    }
    public createMagnitude(magnitude: MagnitudeDto): Observable<number> {
        return this.http.post<number>('api/magnitude/', magnitude);
    }

    public getMagnitudes(page: number, perPage: number, orderBy: string, orderByDescending: boolean): Observable<PFOCollection<MagnitudeDto>> {
        const params = HttpHelper.createQueryParams({page:page,perPage:perPage,orderBy:orderBy, orderByDescending:orderByDescending});  
        return this.http.get<PFOCollection<MagnitudeDto>>('api/magnitude',{params});
    }
}
