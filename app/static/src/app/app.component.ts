import { Component } from '@angular/core';
import { MatToolbarModule } from '@angular/material/toolbar';
import { Observable, Subscription } from 'rxjs';

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
    liveViewPaused = false;
    oldView: string;
    number = 2000;

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
        this.title = 'Welcome to Aquila';
    }

    ngOnInit() {
        Observable.timer(0, 6000)
        //               ^ delay (ms) before first call
        //                   ^ delay (ms) between each subsequent call
            .exhaustMap((value, index) => {
                return this.dataService.get(this.number)
            })
            .scan((acc, value, index) => {
                if ( !(this.liveViewPaused) ) {
                    this.data = value;
                    console.log(this.data);
                }

                if (this.view == 'start') {
                    this.title = 'ICE 1337';
                    this.view = 'map';
                }

                this.number += 250;

                return {};
            })
            .subscribe(_ => {
            }, err => {
                console.log(err);
                window.alert('Sorry, something went wrong.\n\nPlease try again later :/');
            })
        ;
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

    toggleLiveView() {
        this.liveViewPaused = !this.liveViewPaused;
    }
}
