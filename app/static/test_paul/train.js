d3.json('/gps/40117905/1', function (error, data) {
    "use strict";
    if (error) throw error;
    let svgContainer = d3.select("#train").append("svg")
        .attr("width", window.innerWidth - 20)
        .attr("height", window.innerHeight - 20);

    let circleSelection = svgContainer.append("circle")
        .attr("cx", 25)
        .attr("cy", 25)
        .attr("r", 25)
        .style("fill", "purple");

    /*
    newChart('/janreport/runs/', file, '/all_runs', [], colorMapping);
    function redrawPlot(){
        newChart('/janreport/runs/', file, '/all_runs', $("#chip-active").material_chip('data')
            .reduce((accumulator, currentValue) => {
            accumulator.push(currentValue.tag);
        return accumulator;
    }, []), colorMapping);
    }*/
});