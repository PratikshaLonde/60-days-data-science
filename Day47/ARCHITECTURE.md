\# Customer Intelligence Platform

\## System Architecture — Day 47/60



```mermaid

flowchart TD

&#x20;   A\[Sales Dataset: cleaned\_dataset.csv] --> B\[Data Loading]

&#x20;   B --> C\[Data Validation]

&#x20;   C --> D\[Data Cleaning and Preparation]

&#x20;   D --> E\[Analytics Engine]



&#x20;   E --> F\[Sales and Profitability Analytics]

&#x20;   E --> G\[Customer Segmentation]

&#x20;   E --> H\[Customer Risk and Retention Insights]

&#x20;   E --> I\[Sales Forecasting]



&#x20;   F --> J\[Results and KPIs]

&#x20;   G --> J

&#x20;   H --> J

&#x20;   I --> J



&#x20;   J --> K\[Interactive Streamlit Dashboard]

&#x20;   K --> L\[Business Insights and Reports]



&#x20;   C --> M\[Logging and Error Handling]

&#x20;   E --> M

&#x20;   K --> M

```



\### Architecture Explanation



1\. \*\*Sales Dataset:\*\* Provides the existing cleaned sales data.

2\. \*\*Data Loading:\*\* Reads the dataset into the application.

3\. \*\*Data Validation:\*\* Checks required columns and invalid values.

4\. \*\*Data Cleaning:\*\* Prepares the data for analysis.

5\. \*\*Analytics Engine:\*\* Runs the different customer intelligence modules.

6\. \*\*Results and KPIs:\*\* Organizes the analytical results into useful metrics.

7\. \*\*Streamlit Dashboard:\*\* Displays metrics, charts, and customer insights.

8\. \*\*Logging and Error Handling:\*\* Records important events and errors.



\### Design Principle



The system will use a modular architecture so each analytical module can be developed, tested, and improved independently.



\*Note: The diagram represents the proposed architecture. The modules will be implemented and connected during the upcoming capstone days.\*



