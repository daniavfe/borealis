import { Component, Inject, OnInit } from '@angular/core';
import { MagnitudeService } from 'src/app/services/magnitude.service';
import { MagnitudeDto } from 'src/app/dtos/magnitude/magnitudeDto';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
    selector: 'magnitude-form',
    templateUrl: './magnitude-form.html',
    styleUrls: ['./magnitude-form.scss']
})
export class MagnitudeFormDialog implements OnInit {

    public magnitude: MagnitudeDto;

    constructor(
        private magnitudeService: MagnitudeService,
        @Inject(MAT_DIALOG_DATA) public data: MagnitudeDto,
        public dialogRef: MatDialogRef<MagnitudeFormDialog>){
        this.magnitude = data;
    }

    ngOnInit(): void {
    }

    updateMagnitude(): void {
        this.magnitudeService.updateMagnitude(this.magnitude, this.magnitude.id).subscribe(
            res => {
                this.closeDialog();
            }
        );
    }

    closeDialog():void{
        this.dialogRef.close();
    }

}
