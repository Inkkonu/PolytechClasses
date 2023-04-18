<!-- Killian BLAIN -->

var margin = {
    top: 30, right: 10, bottom: 10, left: 0
};

var width = 1500 - margin.left - margin.right;
var height = 800 - margin.top - margin.bottom;

let selectedClass = null;
let rainbow = d3.scaleOrdinal(d3.schemeCategory10);

const bannedCol = ['day', 'year', 'month']

let dimensions = Object.keys(data[0]).filter(d => !bannedCol.find(key => key === d));

let y = {}
for (let i in dimensions) {
    const name = dimensions[i]
    y[name] = d3.scaleLinear().domain(d3.extent(data, function (d) {
        return +d[name];
    })).range([height, 0])
}

let x = d3.scalePoint()
    .range([0, width])
    .padding(1)
    .domain(dimensions);

function color(n) {
    if (selectedClass === null || selectedClass === n) return rainbow(n); else return "lightgrey";
}

function opacity(n) {
    if (selectedClass === null) return 0.5; else if (selectedClass === n) return 0.8; else return 0.2;
}

function updateColors() {
    d3.selectAll(".line")
        .style("stroke", function (d) {
            return color(d["make"]);
        })
        .style("opacity", function (d) {
            return opacity(d["make"]);
        });

    d3.selectAll("circle")
        .style("fill", function (d) {
            return color(d['make']);
        })
        .style("opacity", function (d) {
            return opacity(d["make"]) + 0.2;
        });
}

function path(d) {
    return d3.line()(dimensions.map(function (p) {
        return [x(p), y[p](d[p])];
    }));
}

let highlight = function (event, d) {
    let selectedClass = d["make"];
    updateColors();
}

let doNotHighlight = function (event, d) {
    selectedClass = null;
    updateColors();
}

var svg = d3.select("#parallel")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

svg
    .selectAll("myPath")
    .data(data)
    .enter().append("path")
    .attr("class", function (d) {
        return "line g" + d['Class (Species)']
    })
    .attr("d", path)
    .style("fill", "none")
    .style("stroke", function (d) {
        return color(d['Class (Species)']);
    })
    .style("opacity", 0.5)
    .on("mouseover", highlight)
    .on("mouseleave", doNotHighlight)

svg.selectAll("myAxis")
    .data(dimensions).enter()
    .append("g")
    .attr("transform", function (d) {
        return "translate(" + x(d) + ")";
    })
    .each(function (d) {
        d3.select(this).call(d3.axisLeft().scale(y[d]));
    })
    .append("text")
    .style("text-anchor", "middle")
    .attr("y", function (d, i) {
        return -12 - 8 * (-1) ** i;
    })
    .text(function (d) {
        return d;
    })
    .style("fill", "black")