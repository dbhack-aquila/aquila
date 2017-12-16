import { Component } from '@angular/core';
import {MatToolbarModule} from '@angular/material/toolbar';

import { DataService } from './data.service';
import { Data } from './data';

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

  constructor(private dataService: DataService) {}

  ngOnInit() {
      this.data = this.dataService.get("ICE1337", 17);
      this.view = 'details';
  }
}
