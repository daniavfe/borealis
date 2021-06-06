import { Component, Inject, NgZone, OnInit } from '@angular/core';
import { StationService } from 'src/app/services/station.service';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { DensityService } from 'src/app/services/density.service';
import { NeighborhoodDto } from 'src/app/dtos/density/neighborhoodDto';
import { StationUpdateDto } from 'src/app/dtos/station/stationUpdateDto';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { map, startWith } from 'rxjs/operators';

@Component({
    selector: 'station-form',
    templateUrl: './station-form.html',
    styleUrls: ['./station-form.scss']
})
export class StationFormDialog implements OnInit {

    public neighborhoods: NeighborhoodDto[] = [];
    public station: StationUpdateDto;

    public autocompleteControl = new FormControl();
    public neighborhoodOptions: Observable<NeighborhoodDto[]>;

    public neighborhood: NeighborhoodDto;

    constructor(
        private zone: NgZone,
        private densityService: DensityService,
        private stationService: StationService,
        @Inject(MAT_DIALOG_DATA) public data: StationUpdateDto,
        public dialogRef: MatDialogRef<StationFormDialog>
    ) {
        console.log(data);
        this.station = data;
    }

    ngOnInit(): void {
        this.loadNeighborhoods();
        this.neighborhoodOptions = this.autocompleteControl.valueChanges
            .pipe(
                startWith(''),
                map(value => typeof value === 'string' ? value : value.name),
                map(name => name ? this.filter(name) : this.neighborhoods.slice())
            );
    }

    updateStation(): void {
        this.station.neighborhoodId = this.autocompleteControl.value.id;
        this.stationService.updateStation(this.station, this.station.id).subscribe(
            res => {
                this.closeDialog();
            }
        );
    }

    displayFunction(neighborhood: NeighborhoodDto): string {
        if (!!neighborhood)
            return neighborhood.name;
    }

    loadNeighborhoods() {
        this.densityService.getNeighborhoods(1, 1000, 'id', true).subscribe(
            res => {
                this.zone.run(() => {
                    this.neighborhoods = res.items;

                });
            }
        );


    }

    filter(name: string): NeighborhoodDto[] {
        const filterValue = name.toLowerCase();
        return this.neighborhoods.filter(option => option.name.toLowerCase().indexOf(filterValue) === 0);
    }

    closeDialog(): void {
        this.dialogRef.close(this.station);
    }
}
