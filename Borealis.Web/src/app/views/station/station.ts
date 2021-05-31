import { Component, NgZone, OnInit } from '@angular/core';
import { StationService } from 'src/app/services/station.service';
import { StationDto } from 'src/app/dtos/station/stationDto';
import { StationUpdateDto } from 'src/app/dtos/station/stationUpdateDto';
import { Status } from 'src/app/types/status';
import { PFOCollectionDto } from 'src/app/dtos/pfoCollectionDto';
import { Pagination } from 'src/app/types/pagination';
import { MatDialog } from '@angular/material/dialog';
import { StationFormDialog } from 'src/app/components/station-form-dialog/station-form';

@Component({
    selector: 'station',
    templateUrl: './station.html',
    styleUrls: ['./station.scss']
})
export class StationView implements OnInit {

    public stations: StationDto[] = [];
    paginatedItems: PFOCollectionDto<StationDto>;
    status: Status;
    statusEnum: any = Status;

    page: number = 1;
    itemsPerPage: number = 20;

    constructor(
        private zone: NgZone,
        private stationService: StationService,
        private dialog: MatDialog) { }

    ngOnInit(): void {
        this.status = Status.idle;
        this.loadStations();
    }

    reload(pagination: Pagination) {
        this.page = pagination.page;
        this.itemsPerPage = pagination.perPage;
        this.loadStations();
    }

    loadStations(): void {
        this.status = Status.loading;
        this.stationService.getStations(this.page, this.itemsPerPage, "id", false).subscribe(
            res => {
                this.zone.run(
                    () => {
                        this.paginatedItems = res;
                        this.stations = res.items;
                    }
                )
                this.status = Status.loaded;
            }
        );
    }

    openEditionDialog(station) {
        const dialog = this.dialog.open(StationFormDialog, { data: Object.assign({}, station) });

        dialog.afterClosed().subscribe(
            (data:StationDto) => { 
                this.loadStations();
            }
        );
    }


}
