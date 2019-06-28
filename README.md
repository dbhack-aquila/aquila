# Aquila - Sightseeing in the Train

This Project was built at [8th DB Hackathon](https://dbmindbox.com/en/db-opendata-hackathons/hackathons/hackathon-8-db-open-data/) in Berlin at the 15th and 16th December 2017 by the team "SightTraining".

## Team
- Mauricio Abrigada
- Paul Bauriegel
- Kilian Kluge
- Florian Proske
- Jan-Philipp Schröder
- Joshua Töpfer ([\@joshuatoepfer](https://twitter.com/joshuatoepfer))
- Luca Vazzano ([\@lvgermany](https://twitter.com/lvgermany))

## Use Case
Train trips aren't always that fun, because of that we want to give you the opportunity to explore your surroundings and learn about them.

## Technologies
This Project was made with a [Python](https://www.python.org/) backend, which is an REST API made with [Flask](http://flask.pocoo.org/) and a frontend which was made with [Angular2+](https://angular.io/) and [Bluma](https://bulma.io/).

## Data
For our Project we used different kind of data. Because we hadn't had access to live positioning data of trains we used [historical data collected by the "Wifi on ICE" system](http://data.deutschebahn.com/dataset/wifi-on-ice) which is build into every ICE.
For the point of interests we used different approaches. First we tried the wikipedia geosearch. But this wasn't a good choice because it also marked call-houses near the train tracks. So we tried the [wikunia-sights API](http://api.wikunia.de/sights/index.php) next. There we found a lot of streets and also villages as point of interests. That isn't such a good solution too. So our last attempt was to use the [wikidata API](https://www.wikidata.org/wiki/Wikidata:Main_Page) which did a pretty good job, but marked some memorial tablets on a cemetery. So we had to improve out filtering. For that we hadn't enough time. So the point of interests in our presentation are from the [wikunia-sights API](http://api.wikunia.de/sights/index.php). Since the hackathon, the idea of using Wikidata and filtering is in development as [ionicsolutions/pomi](https://github.com/ionicsolutions/pomi), which one day might or might not serve as a more advanced backend to this project.

## Prospect
In the future you could implement our solution into the ICE portal of Deutsche Bahn, where it could use the positioning system of the Train. You could also build a augmented reality version of our solution or also a augmented window solution like shown in [this article](https://www.golem.de/news/innovation-train-deutsche-bahn-kooperiert-mit-hyperloop-1607-122408.html).

## Run the project
```bash
cd aquila
wget http://download-data.deutschebahn.com/static/datasets/wifi/20171212_wifionice.zip
unzip 20171212_wifionice.zip && rm 20171212_wifionice.zip
mv surveyor_hackathon_data_20171212.csv app/default/surveyor_hackathon_data_20171212.csv

cd app/static
npm install
npm run build

cd ../../..
python3 run.py
```