# Iris Species Explorer

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.20+-3F4F75?style=flat&logo=plotly&logoColor=white)
![Azure](https://img.shields.io/badge/Deployed-Azure-0078D4?style=flat&logo=microsoftazure&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

An interactive Streamlit dashboard for exploring the classic Iris dataset. Filter by species and sepal length in the sidebar and watch every chart update instantly.

---

## Features

- **Sidebar filters** — multi-select species and sepal length range slider
- **Scatter plot** — sepal length vs sepal width, coloured by species
- **Histograms** — frequency and cumulative sepal length distributions side by side
- **Pie charts** — species share by record count, petal length, and petal width
- **Descriptive statistics** table — transposed `describe()` output formatted to 2 decimal places
- **Data caching** — `@st.cache_data` keeps the CSV in memory for fast re-renders
- **Deployed on Azure** via Azure Pipelines CI/CD

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Python 3.10 · Streamlit 1.32+ |
| Visualisation | Plotly Express 5.20+ |
| Data | pandas 2.0+ · Iris CSV |
| CI / CD | Azure Pipelines |
| Hosting | Azure App Service |

---

## Project Structure

```
Streamlit-Dashboard/
├── app.py                  # Streamlit application — all charts and sidebar logic
├── iris.csv                # Iris dataset (150 rows, 5 columns)
├── requirements.txt        # Python dependencies with version pins
├── Pipfile                 # Pipenv dependency file
├── azure-pipelines.yml     # Azure Pipelines CI/CD configuration
└── .github/workflows/      # GitHub Actions workflows
```

---

## Getting Started

### Prerequisites

- Python 3.10 or newer

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Ochanji/Streamlit-Dashboard.git
cd Streamlit-Dashboard

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the dashboard
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Dataset

The [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) contains 150 samples across three species (*Iris setosa*, *Iris versicolor*, *Iris virginica*) with four numeric measurements each: sepal length, sepal width, petal length, and petal width.

---

## License

Distributed under the MIT License.
