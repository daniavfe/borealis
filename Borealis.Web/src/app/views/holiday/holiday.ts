import { Component, NgZone, OnInit } from '@angular/core';
import { HolidayService } from 'src/app/services/holiday.service';
import { HolidayDto } from 'src/app/dtos/holiday/holidayDto';
import { id } from '@swimlane/ngx-charts';

@Component({
    selector: 'holiday',
    templateUrl: './holiday.html',
    styleUrls: ['./holiday.scss']
})
export class HolidayView implements OnInit {

    public year: number = 2021;
    public scope: string[] = ['local', 'national', 'community'];
    public months: string[] = ['January', 'Febrary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December'];
    public daysInMonths: number[];
    public holidays: any = {};

    constructor(private zone: NgZone, private holidayService: HolidayService) { }

    ngOnInit(): void {
        this.loadHolidays();
    }

    getMonthDisplacement(month): number {
        const date = new Date(this.year, month, 1);
        let displacement = date.getDay();

        if (displacement == 0)
            return 7;

        return displacement;
    }

    setUpCalendar(): void {
        this.daysInMonths = [31, this.getFebDays(), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    }

    getFebDays(): number {
        if (((this.year % 4 == 0) && (this.year % 100 != 0)) || (this.year % 400 == 0)) {
            return 29;
        }
        return 28;
    }

    loadHolidays(): void {
        this.holidayService.getHolidaysByYear(this.year).subscribe(
            res => {
                this.zone.run(() => {
                    res.forEach(item => {
                        const index = `${item.date.getFullYear()}${item.date.getMonth()}${item.date.getDate()}`;
                        
                        if (!this.holidays[index]) {
                            this.holidays[index] = [];
                        }

                        this.holidays[index].push(item);
                    });
                    this.setUpCalendar();
                });

                
            }
        );
    }

    changeYear(year: number): void {
        this.year = year;
        this.loadHolidays();
    }

    getTypeOfFestive(month, day) {
        const index = `${this.year}${month}${day}`;
        const festives = this.holidays[index];
        if (!festives)
            return;
        let isLocal = false;
        let isCommunitary = false;
        let isNational = false;


        console.log(festives);
        //Local,Comunitario, Nacional y cualquier mezcla
        isLocal = festives.some(el => el.scope == 'LOCAL_FESTIVE');
        isCommunitary = festives.some(el => el.scope == 'COMMUNITY_FESTIVE');
        isNational = festives.some(el => el.scope == 'NATIONAL_FESTIVE');

        return `${isLocal ? 'local' : ''}${isCommunitary ? 'communitary' : ''}${isNational ? 'national' : ''}`;

    }


    getRange(amount: number): number[] {
        if (amount <= 0)
            return [];
        return [...Array(amount).keys()];
    }

}
