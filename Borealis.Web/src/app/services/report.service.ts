import { HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ReportDto } from '../types/report/report';
import { TimelineDate } from '../types/timeline/timelineDate';


@Injectable({
    providedIn: 'root'
})
export class ReportService {

    constructor(private http: HttpClient) { }

    public getReport():Observable<ReportDto> {
        return this.http.get<ReportDto>('api/report');
    }

    public getTimelineDates():Observable<TimelineDate>{
        return this.http.get<TimelineDate>('api/report/dates');
    }
}
