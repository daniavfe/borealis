import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { DensityDataDto } from '../dtos/density/densityDataDto';
import { NeighborhoodDto } from '../dtos/density/neighborhoodDto';
import { PFOCollectionDto } from '../dtos/pfoCollectionDto';
import { HttpHelper } from '../helpers/httpHelper';

@Injectable({
    providedIn: 'root'
})
export class DensityService {

    apiUrl = environment.apiUrl;

    constructor(private http: HttpClient) { }

    //Dame datos del año X, mes X, distrito X, y barrio X

    public getdensityData(years: number[], districts: number[], neighborhoods: number[], months: number[]): Observable<DensityDataDto[]> {
        let year_list = years.length > 1 ? '?years=' + years.join('&years=') : '';
        let district_list = districts.length > 1 ? '&districts=' + districts.join('&districts=') : '';
        return this.http.get<DensityDataDto[]>(`api/density${year_list}${district_list}`);
    }

    public getNeighborhoods(page: number, perPage: number, orderBy: string, orderByDescending: boolean): Observable<PFOCollectionDto<NeighborhoodDto>> {
        const params = HttpHelper.createQueryParams({ page: page, perPage: perPage, orderBy: orderBy, orderByDescending: orderByDescending });
        return this.http.get<PFOCollectionDto<NeighborhoodDto>>('api/density/neighborhood', {params});
    }
}
