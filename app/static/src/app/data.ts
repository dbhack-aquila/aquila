import { Poi } from './poi'


export class Data {
    public trainLatitude: number;
    public trainLongitude: number;
    public pois: [Poi];

    constructor(trainLatitude: number, trainLongitude: number, pois: [Poi]) {
        this.trainLatitude = trainLatitude;
        this.trainLongitude = trainLongitude;
        this.pois = pois;
    }
}
