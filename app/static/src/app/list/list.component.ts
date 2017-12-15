import { Component, OnInit, Input } from '@angular/core';

import { Data } from './../data';


@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {

    @Input() data: Data;

  constructor() { }

  ngOnInit() {
  }

}
