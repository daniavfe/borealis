import { Component, NgZone, OnInit } from '@angular/core';
import { DensityService } from 'src/app/services/density.service';
import { DensityDataDto } from 'src/app/dtos/density/densityDataDto';

@Component({
    selector: 'density',
    templateUrl: './density.html',
    styleUrls: ['./density.scss']
})
export class DensityView implements OnInit {
    single2020: any[];
    single2019: any[];
    densityData: DensityDataDto[];

    view: any[] = [2000, 500];

    // options
    showXAxis = true;
    showYAxis = true;
    gradient = false;
    showLegend = true;
    showXAxisLabel = true;
    xAxisLabel = 'Country';
    showYAxisLabel = true;
    yAxisLabel = 'Population';

    colorScheme = {
        domain: ['#5AA454', '#A10A28', '#C7B42C', '#AAAAAA']
    };

    constructor(
        private densityService: DensityService) {

    }

    onSelect(event) {
        console.log(event);
    }

    ngOnInit(): void {
        this.getDensityData();
    }


    getDensityData(): void {

        let years = [2020, 2019];

        // this.densityService.getdensityData(years, [], [], []).subscribe(
        //     res => {
        //         this.densityData = res;
        //         this.single2020 = this.densityData[0].districts.map(
        //             el => el.neighborhoods.map(
        //                 (sel) => {
        //                     return {
        //                         name: sel.name,
        //                         value: Object.values(sel.values).reduce((a, b) => a + b, 0) / 12
        //                     }
        //                 }
        //             )
        //         ).flat();



        //         this.single2019 = this.densityData[1].districts.map(
        //             el => el.neighborhoods.map(
        //                 (sel) => {
        //                     return {
        //                         name: sel.name,
        //                         value: Object.values(sel.values).reduce((a, b) => a + b, 0) / 12
        //                     }
        //                 }
        //             )
        //         ).flat();
        //         var x = this.single2020.reduce((a, b) => a + b.value, 0);
        //         var y = this.single2019.reduce((a, b) => a + b.value, 0);
        //         console.log(x);
        //         console.log(y);

        //         // this.single = this.densityData[0].districts[0].neighborhoods.map((el)=>{
        //         //   return {'name':el.name, 'value':el.values[10]}
        //         // }); 
        //     },
        //     err => {

        //     }


        // )
    }

}
