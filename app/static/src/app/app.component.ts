import { Component } from '@angular/core';
import {MatToolbarModule} from '@angular/material/toolbar';
import { Subscription } from 'rxjs/Subscription';

import { DataService } from './data.service';
import { Data } from './data';
import { Poi } from './poi';

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
  view: 'start'|'map'|'list';
  overlayDetails = false;
  oldView: string;
  number = 1;

  data: Data;
  selectedPoi: Poi;

  subscription: Subscription;

  constructor(private dataService: DataService, private messageService: MessageService) {
    this.subscription = this.messageService
      .getMessage()
      .subscribe(message => {
        switch(message.sender) {
          case 'start_submit':
            // never gonna (give you up) happen :()
            break;
          case 'poi_selected':
            this.selectedPoi = message.data;
            this.title = message.data.name;
            this.overlayDetails = true
            break;
        }
      });

    this.view = 'start';
    this.title = 'Welcome';
  }

  ngOnInit() {
    setInterval(this.sendText(), 20000);
  }

  sendText() {

      this.dataService.get(this.number)
        .subscribe(data => {
            this.data = data
            console.log(data)
                
            this.title = 'ICE 1337';
            this.view = 'map';
        }
        , err => {
          console.log(err);
          window.alert('Sorry, something went wrong.\n\nPlease try again later :/');
        }
      );
        this.number++;
  }

  gotoMap() {
    this.view = 'map';
  }

  gotoList() {
    this.view = 'list';
  }

  closeDetails() {
    this.title = 'ICE 1337';
    this.overlayDetails = false;
  }
}
