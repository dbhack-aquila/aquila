import { Component, OnInit, Input } from '@angular/core';

import { Data } from './../data';

import { MessageService } from './../message.service';


class Train {
    public sid: string;
    public name: string;

    constructor(sid: string, name: string) {
        this.sid = sid;
        this.name = name;
    }
}

@Component({
  selector: 'app-start',
  templateUrl: './start.component.html',
  styleUrls: ['./start.component.css']
})
export class StartComponent implements OnInit {

  trains = [
      new Train('40117905', 'ICE 1337'),
      new Train('40117905', 'ICE 42')
  ];

  selectedId: number;
  ready: boolean;

  constructor(private messageService: MessageService) { }

  ngOnInit() {
    this.ready = false;
  }

  onChange(value) {
      this.selectedId = value;
      this.ready = true;
  }

  submit() {
    this.messageService.sendMessage('start_submit', this.trains[this.selectedId]);
  }

}
