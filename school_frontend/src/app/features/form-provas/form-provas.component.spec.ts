/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { FormProvasComponent } from './form-provas.component';

describe('FormProvasComponent', () => {
  let component: FormProvasComponent;
  let fixture: ComponentFixture<FormProvasComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FormProvasComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FormProvasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
