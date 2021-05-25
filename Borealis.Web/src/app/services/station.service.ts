import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { StationDto } from '../types/station/stationDto';
import { PFOCollection } from '../types/pfoCollection';
import { HttpHelper } from '../helpers/httpHelper';
import { StationCreation } from '../types/station/stationCreation';
import { StationUpdate } from '../types/station/stationUpdate';

@Injectable({
    providedIn: 'root'
})
export class StationService {

    constructor(private http: HttpClient) { }

    public createStation(stationCreation:StationCreation){
        return this.http.post<PFOCollection<StationDto>>('api/station', stationCreation);
    }

    public updateStation(stationId:number, stationUpdate:StationUpdate){
        return this.http.put<PFOCollection<StationDto>>(`api/station?id=${stationId}`, stationUpdate);
    }

    public getStations(page: number, perPage: number, orderBy: string, orderByDescending: boolean): Observable<PFOCollection<StationDto>> {
        const params = HttpHelper.createQueryParams({page:page,perPage:perPage,orderBy:orderBy, orderByDescending:orderByDescending}); 
        return this.http.get<PFOCollection<StationDto>>('api/station', {params});
    }
}
