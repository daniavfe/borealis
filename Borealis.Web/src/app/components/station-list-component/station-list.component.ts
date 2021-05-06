import { Component, NgZone, OnInit } from '@angular/core';
import { StationService } from 'src/app/services/station.service';
import { Station } from 'src/app/types/station/station';
import { StationUpdate } from 'src/app/types/station/stationUpdate';

@Component({
    selector: 'station-list',
    templateUrl: './station-list.component.html',
    styleUrls: ['./station-list.component.scss']
})
export class StationListComponent implements OnInit {

    public stations: Station[] = [];

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
        const uploadStation = new StationUpdate(station?.name, station?.address, station?.startDate, station?.endDate, station?.latitude, station?.longitude, station?.altitude);
        this.stationService.updateStation(station.id, uploadStation).subscribe(res =>{
            console.log("updated");
        });
    }

}
