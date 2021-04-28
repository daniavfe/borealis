import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MagnitudeListComponent } from './magnitude-list.component';

describe('MagnitudeListComponent', () => {
    let component: MagnitudeListComponent;
    let fixture: ComponentFixture<MagnitudeListComponent>;

    beforeEach(async () => {
        await TestBed.configureTestingModule({
            declarations: [MagnitudeListComponent]
        })
            .compileComponents();
    });

    beforeEach(() => {
        fixture = TestBed.createComponent(MagnitudeListComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
