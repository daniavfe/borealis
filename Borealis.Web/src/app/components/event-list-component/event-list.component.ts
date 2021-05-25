import { Component, NgZone, OnInit } from '@angular/core';
import { EventService } from 'src/app/services/event.service';
import { Event } from 'src/app/dtos/event/event';

@Component({
	selector: 'event-list',
	templateUrl: './event-list.component.html',
	styleUrls: ['./event-list.component.scss']
})
export class EventListComponent implements OnInit {

	public events: Event[];

	constructor(private zone: NgZone, private eventService: EventService) { }

	ngOnInit(): void {
		this.loadEvents();
	}

	loadEvents(): void {
		this.eventService.getEvents(1, 10, 'id', true).subscribe(
			res => {
				this.zone.run(() => {
					this.events = res.items;
				}
				);
			}
		);
	}

}
