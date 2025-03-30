document.addEventListener("DOMContentLoaded", function () {
    function initializeGraphs() {
        if (typeof Plotly === "undefined") {
            console.error("Plotly.js is not loaded yet. Retrying...");
            setTimeout(initializeGraphs, 1000); // Try again after 1000ms
            return;
        }

        // Define graph data
        let cpuData = [{ x: [], y: [], mode: "lines", name: "CPU Usage" }];
        let ramData = [{ x: [], y: [], mode: "lines", name: "RAM Usage" }];
        let networkData = [{ x: [], y: [], mode: "lines", name: "Network Traffic" }];

        // Define layout (x-axis labels and controls disabled)
        let layout = {
            xaxis: {
                showgrid: false,
                showticklabels: false, // Hide x-axis labels
            },
            yaxis: {
                title: "%",
            },
            dragmode: false,          // Disable zoom and pan interactions
            showlegend: false,        // Hide the legend
            displayModeBar: false     // Disable graph controls
        };

        // Ensure each graph is inside its respective div inside .graph
        Plotly.newPlot("cpuGraph", cpuData, { ...layout, title: "CPU Usage (%)" });
        Plotly.newPlot("ramGraph", ramData, { ...layout, title: "RAM Usage (%)" });
        Plotly.newPlot("networkGraph", networkData, { ...layout, title: "Network Traffic (Bytes)" });

        function updateGraphs() {
            fetch("/metrics")
                .then((response) => response.json())
                .then((data) => {
                    let time = new Date().toLocaleTimeString();

                    // Update each graph correctly
                    Plotly.extendTraces("cpuGraph", { x: [[time]], y: [[data.cpu]] }, [0]);
                    Plotly.extendTraces("ramGraph", { x: [[time]], y: [[data.ram]] }, [0]);
                    Plotly.extendTraces("networkGraph", { x: [[time]], y: [[data.network]] }, [0]);

                    // Keep max 20 data points for smooth visualization
                    [cpuData, ramData, networkData].forEach((dataSet) => {
                        if (dataSet[0].x.length > 20) {
                            dataSet[0].x.shift();
                            dataSet[0].y.shift();
                        }
                    });
                });
        }

        // Fetch updates every second
        setInterval(updateGraphs, 1000);
    }

    initializeGraphs();
});