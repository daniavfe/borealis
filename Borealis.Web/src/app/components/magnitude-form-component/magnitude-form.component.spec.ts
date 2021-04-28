import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MagnitudeFormComponent } from './magnitude-form.component';

describe('MagnitudeFormComponent', () => {
    let component: MagnitudeFormComponent;
    let fixture: ComponentFixture<MagnitudeFormComponent>;

    beforeEach(async () => {
        await TestBed.configureTestingModule({
            declarations: [MagnitudeFormComponent]
        })
            .compileComponents();
    });

    beforeEach(() => {
        fixture = TestBed.createComponent(MagnitudeFormComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
