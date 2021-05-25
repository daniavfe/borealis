import { Component, NgZone, OnInit } from '@angular/core';
import { StationService } from 'src/app/services/station.service';
import { StationDto } from 'src/app/dtos/station/stationDto';
import { StationUpdateDto } from 'src/app/dtos/station/stationUpdateDto';

@Component({
    selector: 'station',
    templateUrl: './station.html',
    styleUrls: ['./station.scss']
})
export class StationView implements OnInit {

    public stations: StationDto[] = [];

    constructor(
        private zone: NgZone,
        private stationService: StationService) { }

    ngOnInit(): void {
        this.loadStations();
    }

    loadStations(): void {
        this.stationService.getStations(1, 50, "id", false).subscribe(
            res => {
                this.zone.run(
                    () => {
                        this.stations = res.items;
                    }
                )
            }
        );
    }

    updateStation(station):void{
        const uploadStation = new StationUpdateDto(station?.name, station?.address, station?.startDate, station?.endDate, station?.latitude, station?.longitude, station?.altitude);
        this.stationService.updateStation(station.id, uploadStation).subscribe(res =>{
            console.log("updated");
        });
    }

}
