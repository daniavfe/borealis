import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpHelper } from '../helpers/httpHelper';
import { ReportDto } from '../dtos/report/reportDto';
import { TimelineDateDto } from '../dtos/timeline/timelineDateDto';


@Injectable({
    providedIn: 'root'
})
export class ReportService {

    constructor(private http: HttpClient) { }

    public getReport(): Observable<ReportDto> {
        return this.http.get<ReportDto>('api/report');
    }

    public getTownReport(year: number, granularity: string, towns: number[], months: number[], stationIds: number[], magnitudeIds: number[]): Observable<ReportDto> {
        const params = HttpHelper.createQueryParams({ year: year, granularity: granularity, towns:towns, months: months,  stationIds: stationIds, magnitudeIds: magnitudeIds });
        return this.http.get<ReportDto>('api/report/town', { params });
    }

    public getTimelineDates(): Observable<TimelineDateDto> {
        return this.http.get<TimelineDateDto>('api/report/dates');
    }
}
