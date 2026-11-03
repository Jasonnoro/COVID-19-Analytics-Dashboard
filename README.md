# Pandemic Trends Explorer

An interactive, full-stack analytics dashboard for exploring COVID-19 trends across countries, transforming raw pandemic data into dynamic visualizations and meaningful insights.

## Overview

Developed a web-based analytics application that enables users to investigate the progression of COVID-19 through country-specific comparisons of new cases, deaths, and vaccinations.

Built with a Flask backend and an interactive HTML, CSS, and JavaScript frontend, the dashboard retrieves filtered datasets through API requests and dynamically updates Plotly visualizations without requiring page reloads.

## Key Features

- **Interactive Country Filtering:** Compare pandemic trends across countries using dynamic dropdown selections.
- **Multi-Metric Analysis:** Explore new cases, reported deaths, and vaccination trends over time.
- **Dynamic Visualizations:** Generate interactive Plotly time-series charts based on user-selected countries and metrics.
- **Flask API Integration:** Implemented a `/data` endpoint to serve filtered COVID-19 data in JSON format.
- **Asynchronous Updates:** Integrated JavaScript API requests to refresh visualizations without reloading the dashboard.
- **Trend Interpretation:** Generate contextual insights to highlight fluctuations, emerging patterns, and changes in pandemic metrics.

## Data Processing & Analysis

Used Pandas to transform raw COVID-19 records into structured time-series data suitable for interactive analysis.

- Handled missing values in `new_vaccinations` by replacing them with zero to maintain dataset continuity.
- Sorted records chronologically to ensure accurate time-series analysis.
- Calculated 7-day rolling averages to smooth daily fluctuations and identify underlying trends.
- Generated monthly aggregations to examine longer-term changes in pandemic metrics.

## Insights & Analytical Considerations

The dashboard supports exploration of several pandemic-related patterns:

- **Infection trends:** Identify periods of increased cases and changes in reported infection rates.
- **Mortality patterns:** Examine changes in reported deaths and potential delays relative to case surges.
- **Vaccination progress:** Explore vaccination rollout patterns and differences across countries.
- **Temporal relationships:** Compare case, death, and vaccination trends over time.

Interpretation considers potential reporting delays, changes in testing practices, public health policies, and batch reporting. Observed correlations should not be interpreted as evidence of causation.

## Technology Stack

| Technology | Application |
|---|---|
| Python | Core application logic |
| Flask | Backend framework and API development |
| Pandas | Data cleaning, preprocessing, and aggregation |
| Plotly | Interactive time-series visualizations |
| HTML5 | Dashboard structure |
| CSS3 | Styling and interface design |
| JavaScript | API requests and dynamic frontend updates |

## Application Architecture

The application connects data processing, backend services, and frontend visualization into a single workflow.

1. **Data Layer:** Pandas processes and prepares the COVID-19 dataset.
2. **Backend:** Flask handles user requests and filters records through the `/data` API endpoint.
3. **Frontend:** HTML and CSS structure and style the dashboard.
4. **Visualization:** JavaScript retrieves filtered JSON data and updates Plotly charts asynchronously.

## Getting Started

### Prerequisites

- Python 3.14
- pip

### 1. Clone the repository

```bash
git clone https://github.com/Jasonnoro/Pandemic-Trends-Explorer.git
```

### 2. Navigate to the project directory

```bash
cd Pandemic-Trends-Explorer
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the application

```bash
python app.py
```

### 5. Access the dashboard

Open your browser and navigate to:

http://127.0.0.1:5000/

## API Endpoint

The dashboard uses a Flask endpoint to retrieve country-specific metrics.

**Example request:**

```text
/data?country=Canada&metric=new_cases
```

The endpoint returns filtered observations in JSON format, which the frontend uses to update the corresponding visualization.

## Project Structure


Pandemic-Trends-Explorer/
│
├── src/
|   ├── app.py
│   └── DataCleaning.py
│
├── data/
│   ├── cleaned_covid_data.csv
│   └── COVID_Country_Sample.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── styles.css
│
├── requirements.txt
└── README.md


## Key Learning Outcomes

- Integrated data analytics with full-stack web application development.
- Processed and aggregated real-world time-series datasets using Pandas.
- Developed backend API routes and data filtering logic using Flask.
- Implemented asynchronous JavaScript requests for dynamic content updates.
- Built interactive visualizations to communicate temporal and geographic trends.
- Translated data patterns into contextual insights while accounting for limitations in real-world reporting.

---

*Built with Python, Flask, Pandas, Plotly, HTML, CSS, and JavaScript.*
