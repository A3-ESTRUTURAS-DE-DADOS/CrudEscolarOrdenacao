/* tslint:disable:no-unused-variable */

import { TestBed, inject } from '@angular/core/testing';
import { ServiceService } from './aluno.service';

describe('Service: Service', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ServiceService]
    });
  });

  it('should ...', inject([ServiceService], (service: ServiceService) => {
    expect(service).toBeTruthy();
  }));
});
