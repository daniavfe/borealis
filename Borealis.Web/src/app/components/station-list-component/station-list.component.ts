import { Component, NgZone, OnInit } from '@angular/core';
import { StationService } from 'src/app/services/station.service';
import { Station } from 'src/app/types/station/station';

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
        this.stationService.getStations(1, 10, "id", false).subscribe(
            res => {
                this.zone.run(
                    () => {
                        this.stations = res.items;
                    }
                )
            }
        );
    }

}
