# Day 45: Deployment Architecture

## 1. Overview

The Customer Intelligence Platform is a Streamlit dashboard deployed using Streamlit Community Cloud.

## 2. Architecture

GitHub Repository → Streamlit Community Cloud → Python and Streamlit Application → CSV Datasets → Interactive Dashboard

## 3. Technology Stack

* Python
* Streamlit
* Pandas
* NumPy
* Matplotlib
* GitHub
* Streamlit Community Cloud

## 4. Data Sources

* `cleaned_dataset.csv` — cleaned customer and sales data
* `Day30/customer_segments_final.csv` — customer segmentation results
* `Day41/customer_risk_ranking.csv` — customer risk rankings

## 5. Deployment Process

1. Store the application code and datasets in GitHub.
2. Connect the GitHub repository to Streamlit Community Cloud.
3. Select `Day44/app.py` as the main application file.
4. Configure the required Python packages.
5. Deploy the dashboard and test the live application.

## 6. Challenge and Solution

**Challenge:** The application initially could not locate some CSV files after deployment.

**Solution:** Updated the paths using Python's `pathlib` to locate the files relative to the project directory.

## 7. Live Application

https://60-days-data-science-k2oxkhpttsfnganorfhgx9.streamlit.app/

## 8. Conclusion

The dashboard is available online, demonstrating the process of deploying a Python data analytics application to the cloud.
