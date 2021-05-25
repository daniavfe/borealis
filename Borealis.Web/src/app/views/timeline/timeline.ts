import { Component, NgZone, OnInit } from '@angular/core';
import { TimelineService } from 'src/app/services/timeline.service';
import { TimelineDto } from 'src/app/types/timeline/timelineDto';

@Component({
    selector: 'timeline',
    templateUrl: './timeline.html',
    styleUrls: ['./timeline.scss']
})
export class TimelineView implements OnInit {

    public timelines: TimelineDto[] = [];

    constructor(
        private zone: NgZone,
        private timelineService: TimelineService) { }

    ngOnInit(): void {
        this.loadTimelines();
    }

    loadTimelines(): void {
        this.timelineService.getTimelines(1, 1000, "id", false).subscribe(
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
