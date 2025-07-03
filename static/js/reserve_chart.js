document.addEventListener("DOMContentLoaded", () => {
  const chartDiv = document.getElementById("reservesBarChart");

  // Fetch oil reserves data and render as stacked area chart
  async function fetchAndRenderStackedChart() {
    try {
      const response = await fetch("/reserves_by_year/");
      const data = await response.json();      
      
      if (data.error) { 
        chartDiv.innerHTML = `<p class="text-danger">${data.error}</p>`;
        return;
      }

      // Prepare traces for each country (stacked by year)
      const traces = data.countries.map(country => ({
        x: data.years,
        y: data.series[country],
        mode: 'lines',
        name: country,
        stackgroup: 'one', 
        type: 'scatter'
      }));

      // Configure chart layout
      const layout = {
        title: {
          text: "Top 5 Countries by Oil Reserves (1995–2021)",
          x: 0.02,
          xanchor: "left"    
        },
        xaxis: { title: "Year" },
        yaxis: { title: "Oil Reserves (Billion Barrels)" },
        hovermode: "x unified"
      };

      Plotly.newPlot(chartDiv, traces, layout, { responsive: true });
    } catch (error) {      
      chartDiv.innerHTML = `<p class="text-danger">Error loading data</p>`;
      console.error(error);
    }
  }

  fetchAndRenderStackedChart();
});
