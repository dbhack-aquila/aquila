import { Injectable } from '@angular/core';

import { Data } from './data';
import { Poi } from './poi';


@Injectable()
export class DataService {

  constructor() { }

  get(trainNumber: string, no: number) {
      return new Data(
          52.514436,
          13.418947,
          [
              new Poi("Mindbox", "Wir sind Teil der Digitalisierungsaktivitäten der DB unter DB digital. Die DB mindbox ist ein zentraler Ort, an dem wir uns mit Startups austauschen und zusammenarbeiten.", "https://inside.bahn.de/wordpress/uploads/2016/02/Mindbox2-Kopie-800x534.jpg", 52.514136, 13.419848, ["http://dbmindbox.com/dbaccelerator/", "https://www.facebook.com/dbmindbox/"], ["https://inside.bahn.de/wordpress/uploads/2016/02/Mindbox2-Kopie-800x534.jpg"]),
              new Poi("Jannowitzbrücke", "Coole Brücke, much Fluss, very bogig", "https://s3.amazonaws.com/gs-geo-images/6db8dbfb-2bc6-42f0-a1ea-25acb8a2ded8_l.jpg", 52.514240, 13.417788, ["https://de.wikipedia.org/wiki/Jannowitzbr%C3%BCcke", "https://www.berlin.de/tourismus/dampferfahrten/anlegestellen/2488866-2486252-jannowitzbruecke.html", "http://www.s-bahn-berlin.de/fahrplanundnetz/bahnhof/jannowitzbruecke/84"], [""])
          ]
      )
  }

}
