d3.json('/gps/40117905/1', function (error, data) {
  if (error) throw error;
  $(window).resize(() => draw());
  draw();

  function draw() {
    d3.select("#train").selectAll('*').remove();
    let h = window.innerHeight;
    let w = window.innerWidth;
    let originX = w / 2;
    let originY = h / 2;

    let dataset = [150, 300, 450, 600];

    let svgContainer = d3.select("#train").append("svg")
      .attr("width", w - 30)
      .attr("height", h - 30);

    svgContainer.selectAll("circle")
      .data(dataset)
      .enter()
      .append("circle")
      .attr("class","circ")
      .style("fill", "none")
      .style("stroke", "black")
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
      svgContainer.append("circle")
        .attr("cx", originX + (diff.lon / 2))
        .attr("cy", originY + (diff.lat / 2))
        .attr("r", 20)
        .style("fill", "black")
        .append("i")
        .attr("class","material-icons")
        .text("star");//<i class="material-icons">star</i>
      svgContainer.append("image")
        .attr("xlink:href", "https://storage.googleapis.com/material-icons/external-assets/v4/icons/svg/ic_star_white_24px.svg")
        .attr("x", originX + (diff.lon / 2)-12)
        .attr("y", originY + (diff.lat / 2)-12)
        .attr("height",24)
        .attr("width",24)
        .attr("class","material-icons")
        .text("star");
       let tex = svgContainer.append("text")
        .attr("x", originX + (diff.lon / 2))
        .attr("y", originY + (diff.lat / 2) + 36)
        .attr("text-anchor","middle")
        .attr("height",24)
        .text(data.pois[index].name);
      let bbox = tex.node().getBBox();
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
      .attr("xlink:href", "DerKleineICE.png")
      .attr("x", originX - 25)
      .attr("y", originY - 75)
      .attr("height", 152.5)
      .attr("width", 57.75);
  }
});
