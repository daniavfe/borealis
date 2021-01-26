import { Component, OnInit } from '@angular/core';
import { DensityService } from 'src/app/services/density.service';
import { DensityData } from 'src/app/types/densityData';
import { NeighborhoodData } from 'src/app/types/neighborhoodData';

@Component({
  selector: 'density-component',
  templateUrl: './density.component.html',
  styleUrls: ['./density.component.scss']
})
export class DensityComponent implements OnInit {
  
  single: any[];
  densityData: DensityData[];

  view: any[] = [700, 400];

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

  constructor(private densityService:DensityService) {

  }

  onSelect(event) {
    console.log(event);
  }

  ngOnInit(): void {
    this.getDensityData();
  }


  getDensityData():void{
    this.densityService.getdensityData().subscribe(
      res=>{
        this.densityData = res;

        let x = this.densityData[0].districts.map(el=>{
          return el.neighborhoods.map((sel)=>{
            return {'name':sel.name, 'value':sel.values[10]}
          })
        })

        console.log(x );

        // this.single = this.densityData[0].districts[0].neighborhoods.map((el)=>{
        //   return {'name':el.name, 'value':el.values[10]}
        // }); 
      },
      err=>{

      }
    )
  }

}
