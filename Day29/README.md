# Create README file for Day 29

readme_content = f"""# Day 29 - Customer Segmentation with K-Means

## Objective

The goal of Day 29 was to understand customer types using
K-Means clustering and identify different customer segments
based on their purchasing behavior.

## Dataset

The cleaned sales dataset was used to create customer-level
behavior data.

Instead of treating every order as a separate customer,
orders were grouped by customer name.

## Customer Features

The following numerical features were used:

- Total Sales
- Total Quantity
- Total Profit
- Average Discount
- Average Shipping Days
- Number of Orders

## Methodology

1. Loaded the cleaned sales dataset.
2. Aggregated order-level data into customer-level data.
3. Selected relevant numerical customer behavior features.
4. Standardized the features using StandardScaler.
5. Tested different K-Means cluster counts from 2 to 6.
6. Compared clusters using Inertia and Silhouette Score.
7. Selected the cluster count with the highest Silhouette Score.
8. Applied the final K-Means model.
9. Used PCA to visualize customer segments.
10. Created cluster profiles and business insights.

## Selected Number of Clusters

The analysis selected **{best_k} clusters** based on the highest
Silhouette Score among the tested cluster counts.

## Output Files

- `day29.ipynb` - Customer segmentation notebook
- `cluster_evaluation.csv` - Evaluation of different cluster counts
- `customer_cluster_profile.csv` - Average behavior of each cluster
- `final_customer_segment_summary.csv` - Final segment summary
- `customer_segments.png` - Customer segment visualization
- `business_insights.md` - Business insight report

## Key Learning

K-Means clustering can identify groups of customers with similar
behavior without requiring predefined customer labels.

Customer segmentation can help businesses understand purchasing
patterns and support more targeted business strategies.

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- K-Means Clustering
- PCA
"""

with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme_content)

print("README created successfully!")