import { Component, OnInit } from '@angular/core';
import { StationService } from 'src/app/services/station.service';
import { StationCreation } from 'src/app/types/station/stationCreation';

@Component({
    selector: 'station-form',
    templateUrl: './station-form.component.html',
    styleUrls: ['./station-form.component.scss']
})
export class StationFormComponent implements OnInit {

    public station:StationCreation;

    constructor(private stationService:StationService) { }

    ngOnInit(): void {
        this.station = new StationCreation();
    }

    createStation():void{
        this.stationService.createStation(this.station).subscribe(
            res=>{
                console.log(res);
            }
        );
    }
}
