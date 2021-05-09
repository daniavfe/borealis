import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
    selector: 'selector',
    templateUrl: './selector.component.html',
    styleUrls: ['./selector.component.scss']
})
export class SelectorComponent implements OnInit {

    @Input() content: any[];
    @Output() getSearchStatusChange = new EventEmitter<number[]>();

    constructor() { }

    ngOnInit(): void {
    }

}
