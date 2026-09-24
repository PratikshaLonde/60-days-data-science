# Create Day 30 README file

readme = f"""# Day 30 - Finding the Ideal Number of Customer Segments

## 📌 Objective

The goal of Day 30 was to determine the ideal number of customer segments
using clustering optimization techniques.

## 🛠️ Techniques Used

- K-Means Clustering
- Elbow Method
- Silhouette Score
- Customer Behavior Analysis
- Data Visualization

## 📊 K Values Tested

The clustering model was tested with K values from **2 to 10**.

The Elbow Method was used to analyze inertia, while the Silhouette Score
was used to evaluate the quality of the clusters.

## 🎯 Final Result

The final model uses **{final_k} customer segments**.

The segments were analyzed using:

- Total Sales
- Total Quantity
- Total Profit
- Average Discount
- Average Shipping Days
- Number of Orders

## 👥 Business Segmentation

### High-Value Customers

Customers belonging to the cluster with higher total sales.

**Strategy:**
- Customer retention
- Loyalty rewards
- Personalized offers
- Priority service

### Regular Customers

Customers in the other identified segment.

**Strategy:**
- Targeted promotions
- Product recommendations
- Increase purchase frequency
- Customer engagement

## 📁 Files

- `day30.ipynb` - Complete Day 30 notebook
- `cluster_optimization_results.csv` - K comparison results
- `customer_segment_profiles.csv` - Segment profiles
- `customer_segments_final.csv` - Final customer segmentation
- `elbow_method.png` - Elbow Method visualization
- `silhouette_scores.png` - Silhouette Score visualization
- `customer_segments_day30.png` - Customer segment visualization
- `segmentation_strategy.md` - Business segmentation strategy

## 💡 Key Learning

Day 30 demonstrated how clustering optimization can help identify
a suitable number of customer segments and convert clustering results
into practical business strategies.
"""

with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme)

print("Day 30 README created successfully!")
print("File: README.md")