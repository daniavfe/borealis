import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpHelper } from '../helpers/httpHelper';
import { Event } from '../types/event/event';
import { PFOCollection } from '../types/pfoCollection';

@Injectable({
    providedIn: 'root'
})
export class EventService {

    constructor(private http: HttpClient) { }

    public getEvents(page: number, perPage: number, orderBy: string, orderByDescending: boolean): Observable<PFOCollection<Event>> {
        const params = HttpHelper.createQueryParams({page:page,perPage:perPage,orderBy:orderBy, orderByDescending:orderByDescending});
        return this.http.get<PFOCollection<Event>>('api/event/', {params});
    }
}
