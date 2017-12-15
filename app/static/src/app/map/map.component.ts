import { Component, OnInit, Input } from '@angular/core';

import { Data } from './../data';


@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {

    @Input() data: Data;

  constructor() { }

  ngOnInit() {
  }

}
