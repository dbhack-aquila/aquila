import { Component, OnInit, Input } from '@angular/core';

import { Data } from './../data';


@Component({
  selector: 'app-start',
  templateUrl: './start.component.html',
  styleUrls: ['./start.component.css']
})
export class StartComponent implements OnInit {

  @Input() data: Data;

  constructor() { }

  ngOnInit() {
  }

}
