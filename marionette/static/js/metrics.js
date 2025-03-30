document.addEventListener("DOMContentLoaded", function () {
    function initializeGraphs() {
        if (typeof Plotly === "undefined") {
            console.error("Plotly.js is not loaded yet. Retrying...");
            setTimeout(initializeGraphs, 1000);
            return;
        }


        let cpuData = [{ x: [], y: [], mode: "lines", line: { color: "#003049" }, fill: "tozeroy", fillcolor: "#669BBC1F", hoverinfo: "none"}];
        let ramData = [{ x: [], y: [], mode: "lines", line: { color: "#003049" }, fill: "tozeroy", fillcolor: "#669BBC1F", hoverinfo: "none"}];
        let netData = [{ x: [], y: [], mode: "lines", line: { color: "#003049" }, fill: "tozeroy", fillcolor: "#669BBC1F", hoverinfo: "none"}];


        let layout = {
            xaxis: {
                showgrid: false,
                showticklabels: false,
            },
            yaxis: {
                range: [0, 100]
            },
            dragmode: false,
            showlegend: false,
            displayModeBar: false,
            margin: {
                l: 30,
                r: 20,
                t: 20,
                b: 20
            }
        };


        Plotly.newPlot("cpuGraph", cpuData, { ...layout, title: "" });
        Plotly.newPlot("ramGraph", ramData, { ...layout, title: "" });
        Plotly.newPlot("networkGraph", netData, { ...layout, title: "" });

        function updateGraphs() {
            fetch("/metrics")
                .then((response) => response.json())
                .then((data) => {
                    let time = new Date().toLocaleTimeString();


                    Plotly.extendTraces("cpuGraph", { x: [[time]], y: [[data.cpu]] }, [0]);
                    Plotly.extendTraces("ramGraph", { x: [[time]], y: [[data.ram]] }, [0]);
                    Plotly.extendTraces("networkGraph", { x: [[time]], y: [[data.network]] }, [0]);


                    [cpuData, ramData, netData].forEach((dataSet) => {
                        if (dataSet[0].x.length > 50) {
                            dataSet[0].x.shift();
                            dataSet[0].y.shift();
                        }
                    });
                });
        }
        setInterval(updateGraphs, 1500);
    }
    initializeGraphs();
});