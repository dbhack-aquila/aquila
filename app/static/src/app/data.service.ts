import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';
import "rxjs/add/observable/of";

import { Data } from './data';
import { Poi } from './poi';


@Injectable()
export class DataService {

  constructor(private http: HttpClient) { }

  get(no: number): Observable<Data> {
        return this.http.get<Data>('/gps/40117905/' + no);
    }
}
