import { TestBed, inject } from '@angular/core/testing';

import { DistanceCalcService } from './distance-calc.service';

describe('DistanceCalcService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [DistanceCalcService]
    });
  });

  it('should be created', inject([DistanceCalcService], (service: DistanceCalcService) => {
    expect(service).toBeTruthy();
  }));
});
