import { Component, OnInit } from '@angular/core';

@Component({
	selector: 'station-list',
	templateUrl: './station-list.component.html',
	styleUrls: ['./station-list.component.scss']
})
export class StationListComponent implements OnInit {

    public stations:Station[];

	constructor() { }

	ngOnInit(): void {
	}

}
