// Fetch data for the choropleth map and render it using Plotly
async function fetchAndRenderChoropleth(metric, causeCategory = null) {
  let url = `/ajax/choropleth-data/?metric=${metric}`;
  if (metric === 'cause_category' && causeCategory) {
    url += `&cause_category=${encodeURIComponent(causeCategory)}`;
  }

  const res = await fetch(url);
  const json = await res.json();
  const data = json.data;

  const locations = data.map(d => d.state);
  const values = data.map(d => d.value);

  // Set colorbar title based on selected metric
  const colorbarTitle =
    metric === 'incidents_per_1000_miles'
      ? 'Incidents per 1,000 Miles'
      : metric === 'total_spilled'
      ? 'Total Spillage'
      : metric === 'cause_category'
      ? 'Cause % of Total Spills'
      : '';
  
  // Format tooltip text for each state
  const text = locations.map((state, i) => {
    const val = values[i];
    const displayVal = values[i];
    if (metric === 'cause_category') {
      return `${state}: ${displayVal} incidents`;
    } else if (metric === 'incidents_per_1000_miles') {
      return `${state}: ${val.toFixed(2)} incidents / 1,000 miles`;
    } else {
      return `${state}: ${val.toFixed(0)} barrels`;
    }
  });
  

  const zmin = Math.min(...values);
  const zmax = Math.max(...values);
  const tickformat =
    metric === 'cause_category'
      ? '.0f'
      : metric === 'incidents_per_1000_miles'
      ? '.2f'
      : '.0f'; 
      
  const colorbar =
    metric === 'cause_category'
      ? {
          title: colorbarTitle,            
          tickformat: tickformat,          
          tick0: 0,
          dtick: (zmax - zmin) / 3 || 1,
          tickmode: 'linear',          
        }
      : {
          title: colorbarTitle,
          tickformat: tickformat,          
        };
  // Define Plotly trace for the choropleth
  const dataTrace = [
    {
      type: 'choropleth',
      locationmode: 'USA-states',
      locations: locations,
      z: values,
      zmin: zmin,
      zmax: zmax,
      text: text,
      colorscale: [
        [0, '#fff5f0'],
        [0.05, '#fee0d2'],
        [0.15, '#fcbba1'],
        [0.25, '#fc9272'],
        [0.35, '#fb6a4a'],
        [0.5, '#ef3b2c'],
        [0.75, '#cb181d'],
        [1, '#a50f15']
      ],
      colorbar: colorbar,
      marker: {
        line: { color: 'rgb(255,255,255)', width: 2 }
      }
    }
  ];

  // Configure map layout
  const layout = {
      title: {
    text: `Pipeline Oil ${colorbarTitle} by U.S. State (2010)`,
    x: 0.02,               
    xanchor: 'left'     
  },
    geo: {
      scope: 'usa',
      projection: { type: 'albers usa' },
      showlakes: true,
      lakecolor: 'rgb(255,255,255)'
    },
    margin: { l: 5, r: 0, t: 100, b: 0 }
  };

  Plotly.newPlot('choroplethContainer', dataTrace, layout, { responsive: true });
}

// Fetch list of possible cause categories
async function fetchCauseCategories() {
  const res = await fetch('/ajax/cause-categories/');
  const json = await res.json();
  return json.causes || [];
}

// Wait for DOM to be ready before setting up event listeners and map
document.addEventListener('DOMContentLoaded', async function () {
  const metricSelector = document.getElementById('metricSelector');
  const causeCategoryContainer = document.getElementById('causeCategoryContainer');
  const causeCategorySelector = document.getElementById('causeCategorySelector');
  
  // Function to update the map based on current selectors
  async function updateMap() {
    const metric = metricSelector.value;
    console.log(metric)
    if (metric === 'cause_category') {
      const cause = causeCategorySelector.value;
      await fetchAndRenderChoropleth(metric, cause);
    } else {
      await fetchAndRenderChoropleth(metric);
    }
  }
  
  metricSelector.addEventListener('change', async () => {
    if (metricSelector.value === 'cause_category') {      
      causeCategoryContainer.style.display = 'block';

    // Populate cause category selector only once if empty
    if (causeCategorySelector.options.length === 0) {
      const causes = await fetchCauseCategories();
      causeCategorySelector.innerHTML = ''; 
      causes.forEach(cause => {
        const opt = document.createElement('option');
        opt.value = cause; 
        
        // Convert to title case and handle slashes
        opt.textContent = cause
          .toLowerCase()
          .split(/[\s/]+/)
          .map(word => word.charAt(0).toUpperCase() + word.slice(1))
          .join(' ')
          .replace(/\/([a-z])/g, (_, c) => '/' + c.toUpperCase());

        causeCategorySelector.appendChild(opt);
      });
    }

      await updateMap();
    } else {      
      causeCategoryContainer.style.display = 'none';
      await updateMap();
    }
  });
  
  causeCategorySelector.addEventListener('change', updateMap);
  
  // Initial setup: show/hide cause category selector depending on metric
  if (metricSelector.value === 'cause_category') {
    causeCategoryContainer.style.display = 'block';
    const causes = await fetchCauseCategories();
    causeCategorySelector.innerHTML = '';
    causes.forEach(cause => {
      const opt = document.createElement('option');
      opt.value = cause;
      opt.textContent = cause;
      causeCategorySelector.appendChild(opt);
    });
  } else {
    causeCategoryContainer.style.display = 'none';
  }
  await updateMap();
});
