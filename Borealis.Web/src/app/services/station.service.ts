import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { StationDto } from '../dtos/station/stationDto';
import { PFOCollectionDto } from '../dtos/pfoCollectionDto';
import { HttpHelper } from '../helpers/httpHelper';
import { StationCreationDto } from '../dtos/station/stationCreationDto';
import { StationUpdateDto } from '../dtos/station/stationUpdateDto';

@Injectable({
    providedIn: 'root'
})
export class StationService {

    constructor(private http: HttpClient) { }

    public createStation(stationCreation:StationCreationDto, id:number){
        return this.http.post<PFOCollectionDto<StationDto>>('api/station', stationCreation);
    }

    public updateStation(station:StationUpdateDto, id:number){
        const params = HttpHelper.createQueryParams({id:id});  
        return this.http.put<number>('api/station/', station, {params:params});
    }

    public getStations(page: number, perPage: number, orderBy: string, orderByDescending: boolean): Observable<PFOCollectionDto<StationDto>> {
        const params = HttpHelper.createQueryParams({page:page,perPage:perPage,orderBy:orderBy, orderByDescending:orderByDescending}); 
        return this.http.get<PFOCollectionDto<StationDto>>('api/station', {params});
    }
}
