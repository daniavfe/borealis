import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpHelper } from '../helpers/httpHelper';
import { MeasurementDto } from '../dtos/measurement/measurementDto';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
    providedIn: 'root'
})
export class MeasurementService {

    constructor(private http: HttpClient) { }

    public getMeasurementForCharts(year: number, month:number, granularity: string, magnitudeIds: number[]): Observable<MeasurementDto[]> {
        const params = HttpHelper.createQueryParams({ year: year, month:month, granularity: granularity, magnitudeIds: magnitudeIds });
        return this.http.get<MeasurementDto[]>('api/measurement/chart', { params }).pipe(
            map(data => {
                data.map(el => el.datetime = new Date(el.datetime))
                return data;
            }));
    }
}
