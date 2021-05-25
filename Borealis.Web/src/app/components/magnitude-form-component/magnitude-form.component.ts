import { Component, OnInit } from '@angular/core';
import { MagnitudeService } from 'src/app/services/magnitude.service';
import { MagnitudeDto } from 'src/app/dtos/magnitude/magnitudeDto';

@Component({
    selector: 'magnitude-form',
    templateUrl: './magnitude-form.component.html',
    styleUrls: ['./magnitude-form.component.scss']
})
export class MagnitudeFormComponent implements OnInit {

    public magnitude: MagnitudeDto;

    constructor(private magnitudeService: MagnitudeService) {

        this.magnitude = new MagnitudeDto();
    }

    ngOnInit(): void {
    }

    createMagnitude(): void {
        this.magnitudeService.createMagnitude(this.magnitude).subscribe(
            res => {
                alert(res);
            }
        );
    }

}
