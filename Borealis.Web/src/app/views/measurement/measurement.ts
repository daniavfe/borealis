import { NgZone } from '@angular/core';
import { Component, OnInit } from '@angular/core';
import { MagnitudeService } from 'src/app/services/magnitude.service';
import { MeasurementService } from 'src/app/services/measurement.service';
import { StationService } from 'src/app/services/station.service';
import { TimelineService } from 'src/app/services/timeline.service';
import { MagnitudeDto } from 'src/app/dtos/magnitude/magnitudeDto';
import { MeasurementDto } from 'src/app/dtos/measurement/measurementDto';
import { StationDto } from 'src/app/dtos/station/stationDto';
import { Status } from 'src/app/types/status';


@Component({
    selector: 'measurement',
    templateUrl: './measurement.html',
    styleUrls: ['./measurement.scss']
})
export class MeasurementView implements OnInit {

    public granularity: string = 'monthly';
    public granularityOptions: string[] = ['hourly', 'daily', 'monthly']
    public measurementYears: number[];
    public stations: StationDto[];
    public magnitudes: MagnitudeDto[];
    public measurements: MeasurementDto[];

    public selectedYear: number;
    public selectedMonth: number;
    public selectedMagnitudes: number[] = [];



    public status: Status;
    public statusEnum = Status;

    public showData: boolean = false;


    multi: any[];
    view: any[] = [0, 500];


    // options
    legend: boolean = true;
    showLabels: boolean = true;
    animations: boolean = false;
    xAxis: boolean = true;
    yAxis: boolean = true;
    showYAxisLabel: boolean = false;
    showXAxisLabel: boolean = true;
    xAxisLabel: string = 'Date';
    yAxisLabel: string = 'Measurement';
    timeline: boolean = true;

    colorScheme = {
        domain: ['#5AA454', '#E44D25', '#CFC0BB', '#7aa3e5', '#a8385d', '#aae3f5']
    };

    constructor(
        private zone: NgZone,
        private timelineService: TimelineService,
        private measurementService: MeasurementService,
        private stationService: StationService,
        private magnitudeService: MagnitudeService) { }

    ngOnInit(): void {
        this.status = Status.idle;
        this.loadMeasurementTypeYears();
        this.loadStations();
        this.loadMagnitudes();
    }

    public loadMeasurementTypeYears(): void {
        this.timelineService.getTimelineInterval('Meteorology').subscribe(res => {
            this.zone.run(() => {
                const firstYear = res.lifeStart.getFullYear();
                const lastYear = res.lifeEnd.getFullYear();
                this.measurementYears = Array.from({ length: lastYear - firstYear + 1 }, (_, index) => index + firstYear);
            });
        });
    }

    public loadStations(): void {
        this.stationService.getStations(1, 1000, '', true).subscribe(res => {
            this.zone.run(() => {
                this.stations = res.items;
            });
        })
    }

    public loadMagnitudes(): void {
        this.magnitudeService.getMagnitudes(1, 1000, '', true).subscribe(res => {
            this.zone.run(() => {
                this.magnitudes = res.items;
            });
        })
    }

    public getMeasurements(): void {
        this.status = Status.loading;
        this.measurementService.getMeasurementForCharts(this.selectedYear, this.selectedMonth, this.granularity, this.selectedMagnitudes).subscribe(res => {
            this.zone.run(() => {
                this.measurements = res;
                const reducedMeasurements = this.reduceMeasurements(res);

                this.multi = Object.entries(reducedMeasurements).map(el => {
                    return {
                        name: el[0],
                        series: el[1].map(el => {
                            let x: any = { name: el.datetime, value: el.data };
                            return x;
                        })

                    }
                });
                this.status = Status.loaded;
            });
        });
    };

    public reduceMeasurements(measurements: MeasurementDto[]): any[] {
        const reduced = measurements.reduce((accumulator: any = {}, currentElement: MeasurementDto) => {
            if (!accumulator[currentElement.magnitudeId])
                accumulator[currentElement.magnitudeId] = []

            accumulator[currentElement.magnitudeId].push(currentElement)
            return accumulator;
        }, {});
        return reduced;
    }

    public mustYearBeSelected() {
        return this.granularity != 'monthly';
    }

    public mustMonthBeSelected() {
        return (this.granularity == 'hourly');
    }

    public granularityChanged() {
        switch (this.granularity) {
            case 'monthly':
                this.selectedYear = null;
            case 'daily':
                this.selectedMonth = null;
                break;
        }
    }

    public canLoadChart():boolean{
        switch (this.granularity) {
            case 'hourly':
                return !!this.selectedMonth && !!this.selectedYear;
            case 'daily':
                return !!this.selectedYear;
        }

        return true;
    }
}

