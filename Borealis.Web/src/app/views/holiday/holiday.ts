import { Component, NgZone, OnInit } from '@angular/core';
import { HolidayService } from 'src/app/services/holiday.service';
import { HolidayDto } from 'src/app/types/holiday/holidayDto';

@Component({
	selector: 'holiday',
	templateUrl: './holiday.html',
	styleUrls: ['./holiday.scss']
})
export class HolidayView implements OnInit {

    public year:number = 2020;
    public scope:string[] = ['local', 'national','community'];
    public daysInMonths:number[]; 
	public holidays:HolidayDto[];

	constructor(private zone:NgZone, private holidayService:HolidayService) { }

	ngOnInit(): void {
		this.loadHolidays();
	}

    getMonthDisplacement(month):number{
        let date = new Date(this.year, month, 1);
        return date.getDay()-1;
    }

    setUpCalendar():void{
        this.daysInMonths = [31, this.getFebDays(), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    }

    getFebDays():number{
        if (((this.year % 4 == 0) && (this.year % 100 != 0)) || (this.year % 400 == 0)){
            return 29;
        }
        return 28;
    }

	loadHolidays():void{
		this.holidayService.getHolidaysByYear(this.year).subscribe(
			res=>{
				this.zone.run(()=>{
					this.holidays = res;
                    this.setUpCalendar();
				});
			}
		);
	}

    changeYear(year:number):void{
        this.year = year;
        this.loadHolidays();
    }

    isFestiveDay(month, day):boolean{
        var date = new Date(this.year, month+1, day+1);
        return this.holidays.some(el=>el.date.getTime() == date.getTime());
    }

    getRange(amount:number):number[]{
        if(amount <= 0)
            return [];
        return [...Array(amount).keys()];
    }

}
