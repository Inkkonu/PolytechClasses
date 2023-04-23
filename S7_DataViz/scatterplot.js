<!-- Killian BLAIN -->

const sizeScatter = 100;
const paddingScatter = 20;

let xScatter = d3
    .scaleLinear()
    .range([paddingScatter / 2, sizeScatter - paddingScatter / 2]);

let yScatter = d3
    .scaleLinear()
    .range([sizeScatter - paddingScatter / 2, paddingScatter / 2]);

let xAxisScatter = d3.axisBottom()
    .scale(xScatter)
    .ticks(6);

let yAxisScatter = d3.axisLeft()
    .scale(yScatter)
    .ticks(6);

let colorScatter = d3.scaleOrdinal(d3.schemeCategory10);

const banned = ['day', 'year', 'month']

let domainByTrait = {}, traits = Object.keys(data[0]).filter(d => !banned.find(key => key === d))
n = traits.length;

traits.forEach(function (trait) {
    domainByTrait[trait] = d3.extent(data, function (d) {
        return d[trait];
    });
});

xAxisScatter.tickSize(sizeScatter * n);
yAxisScatter.tickSize(-sizeScatter * n);

const brushScatter = d3.brush()
    .on("start", brushStart)
    .on("brush", brushMove)
    .on("end", brushEnd)
    .extent([[0, 0], [sizeScatter, sizeScatter]]);

const svgScatter = d3.select("#scatterplot")
    .append("svg")
    .attr("width", sizeScatter * n + paddingScatter)
    .attr("height", sizeScatter * n + paddingScatter)
    .append("g")
    .attr("transform", "translate(" + paddingScatter + "," + paddingScatter / 2 + ")");

svgScatter.selectAll(".x.axis")
    .data(traits)
    .enter().append("g")
    .attr("class", "x axis")
    .attr("transform", function (d, i) {
        return "translate(" + (n - i - 1) * sizeScatter + ",0)";
    })
    .each(function (d) {
        xScatter.domain(domainByTrait[d]);
        d3.select(this).call(xAxisScatter);
    });

svgScatter.selectAll(".y.axis")
    .data(traits)
    .enter().append("g")
    .attr("class", "y axis")
    .attr("transform", function (d, i) {
        return "translate(0," + i * sizeScatter + ")";
    })
    .each(function (d) {
        yScatter.domain(domainByTrait[d]);
        d3.select(this).call(yAxisScatter);
    });

let cellScatter = svgScatter.selectAll(".cell")
    .data(cross(traits, traits))
    .enter()
    .append("g")
    .attr("class", "cell")
    .attr("transform", function (d) {
        return "translate(" + (n - d.i - 1) * sizeScatter + "," + d.j * sizeScatter + ")";
    })
    .each(plot);

cellScatter.filter(function (d) {
    return d.i === d.j;
}).append("text")
    .attr("x", paddingScatter)
    .attr("y", paddingScatter)
    .attr("dy", ".71em")
    .text(function (d) {
        return d.x;
    });

cellScatter.call(brushScatter);

function plot(p) {
    let cell = d3.select(this);

    xScatter.domain(domainByTrait[p.x]);
    yScatter.domain(domainByTrait[p.y]);

    cell.append("rect")
        .attr("class", "frame")
        .attr("x", paddingScatter / 2)
        .attr("y", paddingScatter / 2)
        .attr("width", sizeScatter - paddingScatter)
        .attr("height", sizeScatter - paddingScatter);

    cell.selectAll("circle")
        .data(data)
        .enter().append("circle")
        .attr("cx", function (d) {
            return xScatter(d[p.x]);
        })
        .attr("cy", function (d) {
            return yScatter(d[p.y]);
        })
        .attr("r", 4)
        .style("fill", function (d) {
            return colorScatter(d['make']);
        });
}

let brushCellScatter;

function brushStart(plot) {
    if (brushCellScatter !== this) {
        d3.select(brushCellScatter).call(brushScatter.move, null);
        brushCellScatter = this;
        console.log(plot)
        console.log(domainByTrait)
        xScatter.domain(domainByTrait[plot.x]);
        yScatter.domain(domainByTrait[plot.y]);
    }
}

function brushMove(plot) {
    let e = d3.brushSelection(this);
    svgScatter.selectAll("circle").classed("hidden", function (d) {
        return !e ? false : (e[0][0] > xScatter(+d[plot.x]) || xScatter(+d[plot.x]) > e[1][0] || e[0][1] > yScatter(+d[plot.y]) || yScatter(+d[plot.y]) > e[1][1]);
    });
}

function brushEnd() {
    let e = d3.brushSelection(this);
    if (e === null) svgScatter.selectAll(".hidden").classed("hidden", false);

}

function cross(a, b) {
    let c = [], n = a.length, m = b.length, i, j;
    for (i = -1; ++i < n;) for (j = -1; ++j < m;) c.push({x: a[i], i: i, y: b[j], j: j});
    return c;
}