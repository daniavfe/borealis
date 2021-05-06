import { Component, NgZone, OnInit } from '@angular/core';
import { MagnitudeService } from 'src/app/services/magnitude.service';
import { Magnitude } from 'src/app/types/magnitude/magnitude';


@Component({
    selector: 'magnitude-list',
    templateUrl: './magnitude-list.component.html',
    styleUrls: ['./magnitude-list.component.scss']
})
export class MagnitudeListComponent implements OnInit {
    public magnitudes: Magnitude[] = [];

    constructor(
        private zone: NgZone,
        private magnitudeService: MagnitudeService,) { }

    ngOnInit(): void {
        this.loadMagnitudes();
    }

    loadMagnitudes(): void {
        this.magnitudeService.getMagnitudes(1, 50, 'name', false).subscribe(
            res => {
                this.zone.run(() => {
                    this.magnitudes = res.items;
                })
            }
        );
    }

    uploadMagnitude(magnitude):void{

    }

}
