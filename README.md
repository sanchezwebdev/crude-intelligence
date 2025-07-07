# Crude Intelligence

**Crude Intelligence** is a Django-based web application for analyzing and visualizing oil and gas pipeline data in the United States. It delivers interactive, browser-based data visualizations to help users explore pipeline incidents, spillage volumes, and infrastructure metrics across the country.

---

## Deployment

- **Backend**: PostgreSQL database deployed on **[Supabase](https://supabase.com)**  
- **Frontend**: Django app hosted on **[Heroku](https://www.heroku.com/)**

---

## Features

- Interactive **choropleth maps** of oil spillage per pipeline mile by U.S. state
- **Data visualizations** built with Plotly and Pandas
- Clean, modular **Django app structure**
- Custom PostgreSQL queries for efficient data aggregation
- Simple setup and extensibility for new views or visualizations
---

## Project Structure

- `manage.py`: Django management script
- `crude_intelligence`: Django project configuration (settings, URLs, WSGI/ASGI)
- `app/`: Main Django app containing models, views, utilities, and templates
- `static/`: Static files (CSS, JS)

## Example Visualization

The main dashboard provides an overview of global oil data, including crude oil price trends, production breakdown by source, consumption patterns by country over time, and global trade flows illustrated with a Sankey diagram.
![Alt text](https://res.cloudinary.com/dyivstfjt/image/upload/v1751635361/pic_ci1_tkuzwq.png)

## Getting Started

### Prerequisites

- Python 3.8+
- Django
- Pandas
- Plotly

### Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd crude_intelligence
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up your database and environment variables in `.env`.

4. Run migrations:
    ```sh
    python manage.py migrate
    ```

5. Start the development server:
    ```sh
    python manage.py runserver
    ```

6. Access the app at `http://127.0.0.1:8000/`.

## Usage

- Explore interactive maps and data visualizations via the web interface.
- Extend the app by adding new views to app/views/.

## License

This project is licensed under the MIT License.

---

For more details, see the source code in `crude_intelligence/app/views/spills_choropleth.py` and other modules.

# Crude Intelligence

**Crude Intelligence** is a data analytics dashboard for exploring trends, incidents, and economics within the global oil industry. Built with Django, PostgreSQL, and Plotly, it showcases full-stack development and data visualization techniques by combining real-world datasets with interactive, responsive charting.

## 🌍 Features

- Global oil trade flows visualized with Sankey diagrams
- Line, area, pie, bar, and choropleth maps using Plotly
- Interactive chart zooming, tooltips, and image downloads
- Spill event analysis tools with map, timeline, and cost calculators
- Stacked area charts for historical oil reserves and production
- Fully responsive layout with Bootstrap and custom CSS
- AJAX-enhanced dropdowns and filterable data tables

## 📁 Datasets

Sourced from Kaggle, the dashboard integrates data from:
- Global oil reserves, consumption, and production (1965–2023)
- Pipeline mileage and oil spills in the U.S.
- Brent and crude oil prices
- Country-level oil consumption and trade flows
- Pipeline incident reports with cost, fatalities, and release data

## 📊 Chart Types

- Sankey diagrams (oil trade flows)
- Choropleths (pipeline spill maps)
- Line & area charts (oil prices, reserves over time)
- Pie charts (fuel composition, reserve breakdowns)
- Stacked bar charts (spills over time)
- Globe visualizations (international flows)
- Filterable and exportable tables

## 🚀 Tech Stack

- Python · Django · PostgreSQL
- Plotly · pandas · numpy
- AJAX · Bootstrap · Custom CSS
- Hosted on Heroku

## 📦 Getting Started

```bash
git clone https://github.com/YOUR_USERNAME/crude-intelligence.git
cd crude-intelligence
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
