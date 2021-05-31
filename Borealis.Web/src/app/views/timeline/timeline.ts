import { Component, NgZone, OnInit } from '@angular/core';
import { TimelineService } from 'src/app/services/timeline.service';
import { TimelineDto } from 'src/app/dtos/timeline/timelineDto';
import { PFOCollectionDto } from 'src/app/dtos/pfoCollectionDto';
import { Status } from 'src/app/types/status';
import { Pagination } from 'src/app/types/pagination';

@Component({
    selector: 'timeline',
    templateUrl: './timeline.html',
    styleUrls: ['./timeline.scss']
})
export class TimelineView implements OnInit {

    timelines: TimelineDto[] = [];
    paginatedTimelines: PFOCollectionDto<TimelineDto>;
    status:Status;
    statusEnum:any = Status;

    page:number = 1;
    itemsPerPage:number = 20;

    timelineTypes: string[] = ['Pollution', 'CommunityPollution', 'Meteorology', 'CommunityMeteorology', 'Holiday', 'CommunityHoliday', 'Density','CommunityDensity'];
    selectedTimelineType:string;

    constructor(
        private zone: NgZone,
        private timelineService: TimelineService) { }

    ngOnInit(): void {
        this.status = Status.idle;
        this.loadTimelines();
    }

    reload(pagination:Pagination){
        this.page = pagination.page;
        this.itemsPerPage = pagination.perPage;
        this.loadTimelines();
    }

    loadTimelines(): void {
        this.status = Status.loading;
        this.timelineService.getTimelines(this.page, this.itemsPerPage, "id", false).subscribe(
            res => {
                
                this.zone.run(
                    () => {
                        this.paginatedTimelines = res;
                        this.timelines = res.items;
                    }
                );
                this.status = Status.loaded;
            }
        );
    }


}
