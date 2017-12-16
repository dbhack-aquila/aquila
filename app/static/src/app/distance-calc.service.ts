import { Injectable } from '@angular/core';


@Injectable()
export class DistanceCalcService {

    constructor() { }

    /**
    * Calculates the distance in meters in x- and y-direction separately.
    */
    measureVectors(trainlat, trainlon, lat2, lon2): object {
        let latMid = (trainlat + lat2 ) / 2.0;
        let m_per_deg_lat = 110600;
        let m_per_deg_lon = 111412.84 * Math.cos(latMid) - 93.5 * Math.cos(3*latMid) + 0.118*Math.cos(5*latMid);

        let deltaLat = lat2 - trainlat;
        let deltaLon = lon2 - trainlon;
        return {'lat': deltaLat * m_per_deg_lat, 'lon': deltaLon * m_per_deg_lon};
    }

    /**
     * Calculates the total linear distance between two coordiantes.
     */
    measureDistance(lat1, lon1, lat2, lon2): number {
        var R = 6378.137; // Radius of earth in KM
        var dLat = lat2 * Math.PI / 180 - lat1 * Math.PI / 180;
        var dLon = lon2 * Math.PI / 180 - lon1 * Math.PI / 180;
        var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
        Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
        Math.sin(dLon/2) * Math.sin(dLon/2);
        var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
        var d = R * c;
        return d * 1000; // meters
    }
}
