import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Station } from '../types/station/station';
import { PFOCollection } from '../types/pfoCollection';
import { HttpHelper } from '../helpers/httpHelper';
import { TimelineDto } from '../types/timeline/timeline';


@Injectable({
    providedIn: 'root'
})
export class TimelineService {

    constructor(private http: HttpClient) { }

    public getTimelines(page: number, perPage: number, orderBy: string, orderByDescending: boolean): Observable<PFOCollection<TimelineDto>> {
        const params = HttpHelper.createQueryParams({ page: page, perPage: perPage, orderBy: orderBy, orderByDescending: orderByDescending });
        return this.http.get<PFOCollection<TimelineDto>>('api/timeline', { params });
    }
}
