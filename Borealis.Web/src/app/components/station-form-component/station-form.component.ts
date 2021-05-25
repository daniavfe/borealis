import { Component, OnInit } from '@angular/core';
import { StationService } from 'src/app/services/station.service';
import { StationCreationDto } from 'src/app/dtos/station/stationCreationDto';

@Component({
    selector: 'station-form',
    templateUrl: './station-form.component.html',
    styleUrls: ['./station-form.component.scss']
})
export class StationFormComponent implements OnInit {

    public station:StationCreationDto;

    constructor(private stationService:StationService) { }

    ngOnInit(): void {
        this.station = new StationCreationDto();
    }

    createStation():void{
        this.stationService.createStation(this.station).subscribe(
            res=>{
                console.log(res);
            }
        );
    }
}
