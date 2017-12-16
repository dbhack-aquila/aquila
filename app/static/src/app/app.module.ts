import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import 'hammerjs';
import { RouterModule, Routes } from '@angular/router';
import { StartComponent } from './start/start.component';
import { DetailsComponent } from './details/details.component';
import { MapComponent } from './map/map.component';
import { ListComponent } from './list/list.component';

import { DataService } from "./data.service";
import { MessageService } from "./message.service";
import { DistanceCalcService } from "./distance-calc.service";


const appRoutes: Routes = [
    {
        path      : '**',
    },

];

@NgModule({
  declarations: [
    AppComponent,
    StartComponent,
    DetailsComponent,
    MapComponent,
    ListComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,

  ],
  providers: [
    DataService,
    MessageService,
    DistanceCalcService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
