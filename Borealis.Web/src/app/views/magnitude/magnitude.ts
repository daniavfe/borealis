import { Component, NgZone, OnInit } from '@angular/core';
import { MagnitudeService } from 'src/app/services/magnitude.service';
import { MagnitudeDto } from 'src/app/types/magnitude/magnitudeDto';


@Component({
    selector: 'magnitude',
    templateUrl: './magnitude.html',
    styleUrls: ['./magnitude.scss']
})
export class MagnitudeView implements OnInit {
    public magnitudes: MagnitudeDto[] = [];

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
