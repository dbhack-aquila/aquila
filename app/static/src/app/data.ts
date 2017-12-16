import { Poi } from './poi'


export class Data {
    public trainLatitude: number;
    public trainLongitude: number;
    public sid: number;
    public pois: [Poi];

    constructor(pois:[Poi], sid: number, trainLatitude: number, trainLongitude: number) {
        this.trainLatitude = trainLatitude;
        this.trainLongitude = trainLongitude;
        this.sid = sid;
        this.pois = pois;
    }
}
