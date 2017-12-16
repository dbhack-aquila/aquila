import { Component } from '@angular/core';
import {MatToolbarModule} from '@angular/material/toolbar';
import { Subscription } from 'rxjs/Subscription';

import { DataService } from './data.service';
import { Data } from './data';

import { MessageService } from './message.service';

import { StartComponent } from './start/start.component';
import { MapComponent } from './map/map.component';
import { ListComponent } from './list/list.component';
import { DetailsComponent } from './details/details.component';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  data: Data;
  view: 'start'|'map'|'list'|'details';

  subscription: Subscription;

  constructor(private dataService: DataService, private messageService: MessageService) {
    this.subscription = this.messageService
      .getMessage()
      .subscribe(message => {
        switch(message.sender) {
          case 'start_submit':
            // never gonna happen :()
            break;
        }
      });

    this.view = 'start';
    this.title = 'Welcome';
  }

  ngOnInit() {
      this.data = this.dataService.get(17);
      this.title = 'ICE 1337';
      this.view = 'map';
  }

  gotoMap() {
    this.view = 'map';
  }

  gotoList() {
    this.view = 'list';
  }
}
