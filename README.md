# Manthan: Election Data Analysis (2019 vs 2024)

## Overview

_Manthan_ is a comprehensive data analytics project aimed at analyzing the electoral landscape of India, comparing the 2019 and 2024 general elections. The goal is to identify key factors behind the shift in election results, specifically why the BJP secured fewer seats in 2024. The project explores multiple dimensions including candidate demographics, voter turnout, socio-economic indicators, and voting patterns.

## Key Objectives

- **Data Acquisition**: Scrape, clean, and organize data from various reliable sources.
- **Data Analysis**: Uncover insights related to voter behavior, candidate characteristics, and socio-economic factors influencing election outcomes.
- **Visualization**: Present findings through an interactive Streamlit dashboard using advanced visualizations.

## Data Sources

The data was extracted from the following key sources:

1. [Election Commission of India](https://www.eci.gov.in) – Official results and candidate data for the 2019 and 2024 elections.
2. [Voter Turnout](https://www.indiavotes.com/) – Voter turnout statistics for different constituencies.
3. [Candidate Background](https://myneta.info/) – Information on candidates' education, assets, and legal cases.
4. [Socio-Demographic Data](https://www.census2011.co.in/) – Census data providing insights into social and economic demographics across constituencies.
5. [World Bank Open Data](https://data.worldbank.org/indicator) - Provides free and open access to global development data

## Tools and Technologies

- **Web Scraping**:
  - `BeautifulSoup`, `Selenium`, and `lxml` were used to extract dynamic HTML content from the above websites.
- **Data Wrangling**:
  - `Pandas` was extensively used for cleaning, merging, and transforming large datasets.
  - `FuzzyWuzzy` was utilized for fuzzy string matching to resolve inconsistencies in candidate names across different datasets.
  - `Numpy` assisted with numerical operations during data cleaning and transformation.
- **Visualization** (Planned):
  - The cleaned and structured data will be analyzed and visualized using `Matplotlib` and `Plotly`.
- **Dashboard** (Planned):
  - Final insights will be presented on a user-friendly `Streamlit` dashboard, offering interactive visualizations.

## Methodology

1. **Data Extraction**: Leveraged web scraping tools to extract dynamic data from online resources, ensuring accuracy and completeness of election and socio-demographic data.
2. **Data Cleaning**: Rigorous data wrangling techniques were applied to handle inconsistencies, missing values, and redundancies, ensuring data integrity across all sources.
3. **Data Analysis** (Ongoing):
   - Comparative analysis of BJP’s performance across two election cycles.
   - Exploration of voter turnout, candidate demographics, and socio-economic trends.
   - Correlation between candidates’ background and election results.

## Next Steps

- Perform in-depth analysis on:
  - Vote margins and their relationship to socio-economic indicators.
  - Voter turnout patterns based on demographic data (age, gender, literacy, etc.).
- Build an interactive dashboard using `Streamlit` to visualize these findings and make them accessible for public and academic use.

## Project Status

- **Data Scraping**: Completed
- **Data Wrangling**: Completed
- **Data Analysis**: Ongoing
- **Dashboard Development**: Upcoming

## Conclusion

_Manthan_ provides a unique data-driven perspective on Indian elections by leveraging both political and socio-economic data. The project aims to contribute to understanding the evolving political landscape of India and offer insights into how various factors shape election outcomes.

---

Let me know if you'd like to add or modify any part!
