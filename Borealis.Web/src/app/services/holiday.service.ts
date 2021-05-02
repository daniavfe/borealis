import { HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { PFOCollection } from '../types/pfoCollection';
import { HttpHelper } from '../helpers/httpHelper';
import { Holiday } from '../types/holiday/holiday';

@Injectable({
    providedIn: 'root'
})
export class HolidayService {

    constructor(private http: HttpClient) { }

    public getHolidays(page: number, perPage: number, orderBy: string, orderByDescending: boolean): Observable<PFOCollection<Holiday>> {
        const params = HttpHelper.createQueryParams({page:page,perPage:perPage,orderBy:orderBy, orderByDescending:orderByDescending}); 
        return this.http.get<PFOCollection<Holiday>>('api/holiday', {params});
    }
}
