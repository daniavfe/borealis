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

    constructor(
        private zone: NgZone,
        private timelineService: TimelineService) { }

    ngOnInit(): void {
        this.status = Status.idle;
        this.loadTimelines(1, 20);
    }

    reload(pagination:Pagination){
        this.loadTimelines(pagination.page, pagination.perPage);
    }

    loadTimelines(page:number, itemsPerPage:number): void {
        this.status = Status.loading;
        this.timelineService.getTimelines(page, itemsPerPage, "id", false).subscribe(
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
