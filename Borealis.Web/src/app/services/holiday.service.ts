import { HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { PFOCollection } from '../types/pfoCollection';
import { HttpHelper } from '../helpers/httpHelper';
import { HolidayDto } from '../types/holiday/holidayDto';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
    providedIn: 'root'
})
export class HolidayService {

    constructor(private http: HttpClient) { }

    public getHolidays(page: number, perPage: number, orderBy: string, orderByDescending: boolean): Observable<PFOCollection<HolidayDto>> {
        const params = HttpHelper.createQueryParams({page:page,perPage:perPage,orderBy:orderBy, orderByDescending:orderByDescending}); 
        return this.http.get<PFOCollection<HolidayDto>>('api/holiday', {params});
    }

    public getHolidaysByYear(year:number): Observable<HolidayDto[]> {
        const params = HttpHelper.createQueryParams({year:year}); 
        return this.http.get<HolidayDto[]>('api/holiday/year', {params}).pipe(
            map(data => {
                data.map(el => el.date = new Date(el.date))
                return data;
            }));
    }
}
