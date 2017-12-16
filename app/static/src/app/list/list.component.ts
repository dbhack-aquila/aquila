import { Component, OnInit, Input } from '@angular/core';

import { Data } from './../data';
import { Poi } from './../poi';

import { DistanceCalcService } from './../distance-calc.service';
import { MessageService } from './../message.service';


class ListData {
    public distance: number;
    public oldData: Poi;

    constructor(oldData: Poi, distance: number) {
        this.oldData = oldData;
        this.distance = distance;
    }
}

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {

    @Input() data: Data;
    listData: ListData[];

    constructor(private distanceCalcService: DistanceCalcService, private messageService: MessageService) { }

    ngOnInit() {
        this.listData = [];

        for (let i = 0; i < this.data.pois.length; i++) {
            let poi = this.data.pois[i];
            this.listData.push(new ListData(
                poi, this.distanceCalcService.measureDistance(
                        this.data.trainLatitude, this.data.trainLongitude,
                        poi.latitude, poi.longitude
                    )
            ))
        }

        this.listData.sort((d1, d2) => {
            if (d1.distance < d2.distance) { return -1; }
            if (d2.distance < d1.distance) { return 1;  }
            return 0;
        });
    }

    submit(i) {
        this.messageService.sendMessage('poi_selected', this.listData[i].oldData);
    }

}
