import { Component, NgZone, OnInit } from '@angular/core';
import { MagnitudeService } from 'src/app/services/magnitude.service';
import { MagnitudeDto } from 'src/app/dtos/magnitude/magnitudeDto';
import { Status } from 'src/app/types/status';
import { PFOCollectionDto } from 'src/app/dtos/pfoCollectionDto';
import { Pagination } from 'src/app/types/pagination';
import { MatDialog } from '@angular/material/dialog';
import { MagnitudeFormDialog } from 'src/app/components/magnitude-form-dialog/magnitude-form';


@Component({
    selector: 'magnitude',
    templateUrl: './magnitude.html',
    styleUrls: ['./magnitude.scss']
})
export class MagnitudeView implements OnInit {
    magnitudes: MagnitudeDto[] = [];
    paginatedItems: PFOCollectionDto<MagnitudeDto>;
    status: Status;
    statusEnum: any = Status;

    page: number = 1;
    itemsPerPage: number = 20;

    constructor(
        private zone: NgZone,
        private magnitudeService: MagnitudeService,
        private dialog: MatDialog) { }

    ngOnInit(): void {
        this.status = Status.idle;
        this.loadMagnitudes();
    }

    reload(pagination: Pagination) {
        this.page = pagination.page;
        this.itemsPerPage = pagination.perPage;
        this.loadMagnitudes();
    }

    openEditionDialog(magnitude) {
        this.dialog.open(MagnitudeFormDialog,{data:Object.assign({}, magnitude)});
    }

    loadMagnitudes(): void {
        this.status = Status.loading;
        this.magnitudeService.getMagnitudes(this.page, this.itemsPerPage, 'name', false).subscribe(
            res => {
                this.zone.run(() => {
                    this.paginatedItems = res;
                    this.magnitudes = res.items;
                })
                this.status = Status.loaded;
            }
        );
    }


}
