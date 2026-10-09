# Day 45: Cloud Deployment

## Project

Customer Intelligence Platform

## Objective

Deploy the customer intelligence dashboard to the cloud and make it accessible through a live URL.

## Deployment Platform

Streamlit Community Cloud

## Live Dashboard

https://60-days-data-science-k2oxkhpttsfnganorfhgx9.streamlit.app/

## Features

* Customer analytics and KPI cards
* Customer segmentation
* Customer churn-risk analysis
* Monthly revenue visualization
* Profit analysis by category
* Customer filters and data table

## Deployment Challenge

The dashboard initially had problems finding CSV files in the cloud environment because of relative file paths.

## Solution

Updated the file paths using Python's `pathlib` so the application could locate the project datasets correctly.

## Result

The dashboard is deployed and accessible online.

## Skills Learned

* Cloud deployment
* Streamlit Community Cloud
* GitHub integration
* File-path management
* Live application testing
