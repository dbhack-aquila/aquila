import { Component, OnInit, OnChanges, Input, ViewChild } from '@angular/core';

import * as d3 from 'd3/index';

import { Data } from './../data';

import { MessageService } from './../message.service';


@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {

    @Input() data: Data;

    @ViewChild('train') svgElement;

    zoomStep = 0.1;
    zoomLevel = 0;
    viewportSizeStr: string;

  constructor(private messageService: MessageService) { }

  ngOnInit() {}

  ngOnChanges() {
      this.draw(this.data);

      this.resizeViewport();
  }

  resizeViewport() {
    let baseWidth = parseInt(this.svgElement.nativeElement.width.baseVal.value);
    let baseHeight = parseInt(this.svgElement.nativeElement.height.baseVal.value);
    let deltaW = this.zoomStep * this.zoomLevel * baseWidth;
    let deltaH = this.zoomStep * this.zoomLevel * baseHeight;

    let x = baseWidth - (deltaW * 2);
    let y = baseHeight - (deltaH * 2);
    if (x <= 0 || y <= 0) {
      this.zoomLevel--;
      return;
    }

    this.viewportSizeStr = `${deltaW} ${deltaH} ${x} ${y}`;

    this.draw(this.data);
  }

  zoomIn() {
    this.zoomLevel++;
    this.resizeViewport();
  }

  zoomOut() {
    this.zoomLevel--;
    this.resizeViewport();
  }


  draw(data) {
    d3.select("#train").selectAll('*').remove();
    let h = window.innerHeight - 75;
    let w = window.innerWidth;
    let originX = w / 2;
    let originY = h / 2;

    let dataset = [150, 300, 450, 600];

    let svgContainer = d3.select("#train")
      .attr("width", w - 30)
      .attr("height", h - 30);

    svgContainer.selectAll("circle")
      .data(dataset)
      .enter()
      .append("circle")
      .attr("class","circ")
      .style("fill", "none")
      .style("stroke", "black")
      .style("stroke-dasharray", "5,5")
      .style("stroke-width", "2.5")
      .attr("stroke-opacity", function (d) {
      return 1 - (((d/150 - 1)/10)*3);
    })
      .attr("r", function (d) {
        return d;
      })
      .attr("cx", originX)
      .attr("cy", originY);

    let chairWidth = 50;
    svgContainer.selectAll("rect")
      .data(dataset)
      .enter()
      .append("rect")
      .attr("x", function (d) {
        return originX + ((d) * Math.sin(0)) - (chairWidth / 2);
      })
      .attr("y", function (d) {
        return originY - ((d) * Math.cos(0))- (chairWidth / 2) + 20;
      })
      .attr("height", 20)
      .attr("width", chairWidth)
      .style("fill", "white");

    svgContainer.selectAll("text")
      .data(dataset)
      .enter()
      .append("text")
      .attr("x", function (d) {
        return originX + ((d) * Math.sin(0)) - (chairWidth / 2) + 3;
      })
      .attr("y", function (d) {
        return originY - ((d) * Math.cos(0))- (chairWidth / 2) + 30;
      })
      .text(function (d) {
        return d.toString() + " m"
      });

    function measure(trainlat, trainlon, lat2, lon2) {  // generally used geo measurement function
      let latMid = (trainlat + lat2 ) / 2.0;
      let m_per_deg_lat = 111132.954 - 559.822 * Math.cos(2.0 * latMid) + 1.175 * Math.cos(4.0 * latMid);
      let m_per_deg_lon = (3.14159265359 / 180 ) * 6367449 * Math.cos(latMid);

      let deltaLat = lat2 - trainlat;
      let deltaLon = lon2 - trainlon;
      return {['lat']: deltaLat * m_per_deg_lat, ['lon']: deltaLon * m_per_deg_lon}; // meters
    }

    data.pois.forEach((currentValue, index, array) => {
      let diff = measure(data.trainLatitude, data.trainLongitude, data.pois[index].latitude, data.pois[index].longitude);
        let circ = svgContainer.append("circle")
        .attr("cx", (this.zoomLevel * -2.5) + originX + (diff.lon / 2))
        .attr("cy", (this.zoomLevel * -2.5) + originY + (diff.lat / 2))
        .attr("r", (this.zoomLevel * -2.5) + 20)
          .attr("class", "cirir")
          .style("fill", "black")
          .style("pointer-events","visible");
        circ.on("click", () => {
          this.messageService.sendMessage('poi_selected', currentValue);
        });


      let imgCirc = svgContainer.append("image")
        .attr("xlink:href", "https://storage.googleapis.com/material-icons/external-assets/v4/icons/svg/ic_star_white_24px.svg")
        .attr("x", (this.zoomLevel * 0.1) + originX + (diff.lon / 2)-10)
        .attr("y", (this.zoomLevel * 0.1) + originY + (diff.lat / 2)-10)
        .attr("height", (this.zoomLevel * -5) + 24)
        .attr("width", (this.zoomLevel * -5) + 24)
        .attr("class","material-icons")
        .text("star")
        .style("pointer-events","visible");
      imgCirc.on("click", () => {
        this.messageService.sendMessage('poi_selected', currentValue);
      });
       let tex = svgContainer.append("text")
        .attr("x", originX + (diff.lon / 2))
        .attr("y", (this.zoomLevel * -10) + originY + (diff.lat / 2))
        .attr("text-anchor","middle")
        .attr("height",(this.zoomLevel * -2) + 24)
        .text(data.pois[index].name)
        .style("font-size", (this.zoomLevel * -3) + "pt" );
      let bbox = (tex.node() as any).getBBox();
      let padding = 2;
      let rect = svgContainer.insert("rect", "text")
        .attr("x", bbox.x - padding)
        .attr("y", bbox.y - padding)
        .attr("width", bbox.width + (padding*2))
        .attr("height", bbox.height + (padding*2))
        .style("fill", "white");
    });

    svgContainer.append("circle")
      .attr("cx", originX)
      .attr("cy", originY)
      .attr("r", 20)
      .style("fill", "black");

    svgContainer.append("svg:image")
      .attr("xlink:href", "/assets/DerKleineICE.png")
      .attr("x", originX - 25 + (this.zoomLevel * 5))
      .attr("y", originY - 75 + (this.zoomLevel * 5))
      .attr("height", (this.zoomLevel * -10) + 152.5)
      .attr("width", (this.zoomLevel * -10) + 57.75);
  }

  submitter(i) {
        this.messageService.sendMessage('poi_selected', this.data.pois[i]);
        console.log(this.data.pois[i]);
    }

}
