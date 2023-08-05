const borders = true;
const WIDTH = $width;
const HEIGHT = $height;
const dataset = $data
const tooltipAttributes = $tooltip
const MAX_RADIUS = $radio;

const MARGIN = { TOP: 10, BOTTOM: 10, LEFT: 10, RIGHT: 10 };
const widthSVG = WIDTH - MARGIN.RIGHT - MARGIN.LEFT;
const heightSVG = HEIGHT - MARGIN.TOP - MARGIN.BOTTOM;

const SVG = d3.select('#pynetworkd3-chart')
    .append('svg')
    .attr('width', WIDTH)
    .attr('height', HEIGHT)


const container = SVG.append("g").attr(
    "transform",
    `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`
);

const tooltip = d3
    .select("body")
    .append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

const simulation = d3
    .forceSimulation()
    .force("center", d3.forceCenter(widthSVG / 2, heightSVG / 2))
    .force("collision", d3.forceCollide(30))
    .force("charge", d3.forceManyBody().strength(-50))
    .force("link", d3.forceLink().id(node => node.id));

const ticked = () => {
    if (borders) {
        container
            .selectAll(".node")
            .attr("cx", function (d) { return (d.x = Math.max(MAX_RADIUS, Math.min(widthSVG - MAX_RADIUS, d.x))); })
            .attr("cy", function (d) { return (d.y = Math.max(MAX_RADIUS, Math.min(heightSVG - MAX_RADIUS, d.y))); })
    }
    container
        .selectAll(".node")
        .attr("transform", node => `translate(${node.x}, ${node.y})`);

    container
        .selectAll("line")
        .attr("x1", link => link.source.x)
        .attr("y1", link => link.source.y)
        .attr("x2", link => link.target.x)
        .attr("y2", link => link.target.y);
};

simulation
    .nodes(dataset.nodes)
    .on("tick", ticked)
    .force("link")
    .links(dataset.links)
    .distance(80);

container
    .selectAll("line")
    .data(dataset.links)
    .enter()
    .append("line")
    .attr("x1", link => link.source.x)
    .attr("y1", link => link.source.y)
    .attr("x2", link => link.target.x)
    .attr("y2", link => link.target.y);

const dragstarted = (event, node) => {
    if (!event.active) {
        simulation.alphaTarget(0.3).restart();
    }
    node.fx = node.x;
    node.fy = node.y;
};

const dragged = (event, node) => {
    node.fx = event.x;
    node.fy = event.y;
};

const dragended = (event, node) => {
    if (!event.active) {
        simulation.alphaTarget(0.0);
    }
    node.fx = null;
    node.fy = null;
};

const nodes = container
    .selectAll(".node")
    .data(dataset.nodes)
    .enter()
    .append("g")
    .attr("class", "node")
    .call(
        d3
            .drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended)
    );

const mouseover = (event, node) => {
    if (tooltipAttributes) {
        let content = '<table style="margin-top: 2.5px;">'
        tooltipAttributes.forEach(d => {
            content += `<tr><td>${d}: </td><td style="text-align: right">${node[d]}</td></tr>`
        })
        content += '</table>'

        tooltip
            .transition()
            .duration(200)
            .style("opacity", 0.9);

        tooltip
            .html(content)
            .style("left", event.pageX + "px")
            .style("top", event.pageY - 28 + "px");
    }

};

const mouseout = _ => {
    tooltip
        .transition()
        .duration(200)
        .style("opacity", 0);
};

nodes
    .append("circle")
    .attr("r", MAX_RADIUS)
    .on("mouseover", mouseover)
    .on("mouseout", mouseout)