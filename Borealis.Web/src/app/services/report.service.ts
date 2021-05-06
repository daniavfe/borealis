import { HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ReportDto } from '../types/report/report';


@Injectable({
    providedIn: 'root'
})
export class ReportService {

    constructor(private http: HttpClient) { }

    public getCsv():Observable<ReportDto> {
        return this.http.get<ReportDto>('api/report');
    }
}
