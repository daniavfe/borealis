import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
import { PFOCollectionDto } from '../dtos/pfoCollectionDto';
import { HttpHelper } from '../helpers/httpHelper';
import { TimelineDto } from '../dtos/timeline/timelineDto';
import { TimelineIntervalDto } from '../dtos/timeline/timelineIntervalDto';


@Injectable({
    providedIn: 'root'
})
export class TimelineService {

    constructor(private http: HttpClient) { }

    public getTimelines(page: number, perPage: number, orderBy: string, orderByDescending: boolean): Observable<PFOCollectionDto<TimelineDto>> {
        const params = HttpHelper.createQueryParams({ page: page, perPage: perPage, orderBy: orderBy, orderByDescending: orderByDescending });
        return this.http.get<PFOCollectionDto<TimelineDto>>('api/timeline', { params });
    }

    public getTimelineInterval(type: string): Observable<TimelineIntervalDto> {
        const params = HttpHelper.createQueryParams({ type: type });
        return this.http.get<TimelineIntervalDto>('api/timeline/interval', { params }).pipe(
            map(data => {
                data.lifeEnd = new Date(data.lifeEnd);
                data.lifeStart = new Date(data.lifeStart);
                return data;
            })
        );
    }
}
