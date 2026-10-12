const spec = {
  "$schema": "https://vega.github.io/schema/vega-lite/v6.json",
  "data": {
    "values": [
      { "model": "A", "latency": 1.2 },
      { "model": "B", "latency": 0.8 },
      { "model": "C", "latency": 1.5 }
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": { "field": "model", "type": "nominal" },
    "y": { "field": "latency", "type": "quantitative" }
  }
};
 
vegaEmbed("#chart", spec, { actions: true })
  .catch(err => {
    document.getElementById("error").textContent = "Chart render error: " + err.message;
    console.error(err);
  });
 