/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { TableProvasComponent } from './table-provas.component';

describe('TableProvasComponent', () => {
  let component: TableProvasComponent;
  let fixture: ComponentFixture<TableProvasComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TableProvasComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TableProvasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
