import { Component, NgZone, OnInit } from '@angular/core';
import { HolidayService } from 'src/app/services/holiday.service';
import { Holiday } from 'src/app/types/holiday/holiday';

@Component({
	selector: 'holiday-list',
	templateUrl: './holiday-list.component.html',
	styleUrls: ['./holiday-list.component.scss']
})
export class HolidayListComponent implements OnInit {

	public holidays:Holiday[];

	constructor(private zone:NgZone, private holidayService:HolidayService) { }

	ngOnInit(): void {
		this.loadHolidays();
	}

	loadHolidays():void{
		this.holidayService.getHolidays(1, 10, 'id', true).subscribe(
			res=>{
				this.zone.run(()=>{
					this.holidays = res.items;
				});
			}
		);
	}

}
