import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpHelper } from '../helpers/httpHelper';
import { MagnitudeDto } from '../dtos/magnitude/magnitudeDto';
import { PFOCollectionDto } from '../dtos/pfoCollectionDto';

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

    public updateMagnitude(magnitude: MagnitudeDto, id:number): Observable<number> {
        const params = HttpHelper.createQueryParams({id:id});  
        return this.http.put<number>('api/magnitude/', magnitude, {params:params});
    }

    public getMagnitudes(page: number, perPage: number, orderBy: string, orderByDescending: boolean): Observable<PFOCollectionDto<MagnitudeDto>> {
        const params = HttpHelper.createQueryParams({page:page,perPage:perPage,orderBy:orderBy, orderByDescending:orderByDescending});  
        return this.http.get<PFOCollectionDto<MagnitudeDto>>('api/magnitude',{params});
    }
}
