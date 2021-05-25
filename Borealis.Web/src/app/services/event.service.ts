import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpHelper } from '../helpers/httpHelper';
import { Event } from '../dtos/event/event';
import { PFOCollectionDto } from '../dtos/pfoCollectionDto';

@Injectable({
    providedIn: 'root'
})
export class EventService {

    constructor(private http: HttpClient) { }

    public getEvents(page: number, perPage: number, orderBy: string, orderByDescending: boolean): Observable<PFOCollectionDto<Event>> {
        const params = HttpHelper.createQueryParams({page:page,perPage:perPage,orderBy:orderBy, orderByDescending:orderByDescending});
        return this.http.get<PFOCollectionDto<Event>>('api/event/', {params});
    }
}
