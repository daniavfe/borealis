import { Component, NgZone, OnInit } from '@angular/core';
import { StationService } from 'src/app/services/station.service';
import { StationDto } from 'src/app/dtos/station/stationDto';
import { Status } from 'src/app/types/status';
import { PFOCollectionDto } from 'src/app/dtos/pfoCollectionDto';
import { Pagination } from 'src/app/types/pagination';
import { MatDialog } from '@angular/material/dialog';
import { StationFormDialog } from 'src/app/components/station-form-dialog/station-form';
import { icon, latLng, Layer, Marker, marker, MarkerClusterGroup, MarkerClusterGroupOptions, tileLayer } from 'leaflet';

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

    options:any = {
        layers: [
            tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 18})
        ],
        zoom: 11,
        center: latLng(40.4240, -3.6900)
    };

    map:any;

    index:number = 0;

    markers: Layer[] = [];

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
                        this.markers = this.stations.filter(x=>!!x.latitude && !!x.longitude).map(x=> marker([x.latitude, x.longitude]).bindPopup('<p>asdfasdf</p>'));
                    }
                )
                this.status = Status.loaded;
                
            }
        );
    }

    onMapReady(map){
        this.map = map;
    }


    openEditionDialog(station) {
        const dialog = this.dialog.open(StationFormDialog, { data: Object.assign({}, station) });

        dialog.afterClosed().subscribe(
            (data:StationDto) => { 
                this.loadStations();
            }
        );
    }

    ngAfterViewInit() {
        this.map.invalidateSize();
    }


}
