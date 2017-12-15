import { Component, OnInit, Input } from '@angular/core';

import { Poi } from './../poi';


@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css']
})
export class DetailsComponent implements OnInit {

    @Input() poi: Poi;

  constructor() { }

  ngOnInit() {
  }

}
