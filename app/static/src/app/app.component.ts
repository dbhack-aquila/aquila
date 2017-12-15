import { Component } from '@angular/core';
import {MatToolbarModule} from '@angular/material/toolbar';

import { DataService } from './data.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';

  constructor(private dataService: DataService) {}

  ngOnInit() {
      console.log(this.dataService.get("ICE1337", 17));
  }
}
