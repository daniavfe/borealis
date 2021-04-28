import { Component, OnInit } from '@angular/core';
import { MagnitudeService } from 'src/app/services/magnitude.service';
import { Magnitude } from 'src/app/types/magnitude';

@Component({
    selector: 'magnitude-form',
    templateUrl: './magnitude-form.component.html',
    styleUrls: ['./magnitude-form.component.scss']
})
export class MagnitudeFormComponent implements OnInit {

    public magnitude: Magnitude;

    constructor(private magnitudeService: MagnitudeService) {

        this.magnitude = new Magnitude();
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
