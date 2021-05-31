import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Pagination } from 'src/app/types/pagination';

@Component({
    selector: 'paginator',
    templateUrl: './paginator.component.html',
    styleUrls: ['./paginator.component.scss']
})
export class PaginatorComponent implements OnInit {

    @Input()
    page: number;
    @Input()
    pageCount: number;
    @Input()
    perPage: number;
    @Input()
    perPageOptions: any[];
    @Output()
    onLoadPage: EventEmitter<Pagination> = new EventEmitter();

    constructor() { }

    ngOnInit(): void {

    }

    loadNextPage() {
        if (this.page < this.pageCount) {
            this.onLoadPage.emit(new Pagination(this.page + 1, this.perPage));
        }
    }

    loadPreviousPage() {
        if (this.page > 0) {
            this.onLoadPage.emit(new Pagination(this.page -1, this.perPage));
        }
    }

    reloadPage() {
        this.onLoadPage.emit(new Pagination(this.page, this.perPage));
    }

}
