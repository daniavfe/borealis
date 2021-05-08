import { Component, NgZone, OnInit } from '@angular/core';
import { TimelineService } from 'src/app/services/timeline.service';
import { TimelineDto } from 'src/app/types/timeline/timeline';

@Component({
    selector: 'timeline-list',
    templateUrl: './timeline-list.component.html',
    styleUrls: ['./timeline-list.component.scss']
})
export class TimelineListComponent implements OnInit {

    public timelines: TimelineDto[] = [];

    constructor(
        private zone: NgZone,
        private timelineService: TimelineService) { }

    ngOnInit(): void {
        this.loadTimelines();
    }

    loadTimelines(): void {
        this.timelineService.getTimelines(1, 100, "id", false).subscribe(
            res => {
                this.zone.run(
                    () => {
                        this.timelines = res.items;
                    }
                );
            }
        );
    }


}
