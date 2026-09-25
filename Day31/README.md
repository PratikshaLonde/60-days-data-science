# Create Day 31 README

readme = """# Day 31 - Building Customer Personas from Behavioral Data

## 📌 Objective

The goal of Day 31 was to transform customer clustering results into
meaningful customer personas using behavioral data.

## 🛠️ Analysis Performed

- Analyzed customer clusters in detail
- Calculated persona-level behavioral metrics
- Created business-friendly persona descriptions
- Created a customer persona summary table
- Visualized spending patterns
- Visualized customer engagement
- Visualized profit patterns
- Recommended business strategies for each persona

## 📊 Behavioral Metrics

The personas were analyzed using:

- Total Sales
- Total Quantity
- Total Profit
- Average Discount
- Average Shipping Days
- Average Number of Orders
- Customer Count

## 👥 Customer Personas

The customer clusters were converted into business-friendly personas
based on their behavioral characteristics.

Each persona includes:

- Behavioral profile
- Customer count
- Spending characteristics
- Engagement patterns
- Profit contribution
- Recommended business strategy

## 📈 Visualizations

The following visualizations were created:

- `persona_spending.png` - Average spending by persona
- `persona_engagement.png` - Customer engagement by persona
- `persona_profit.png` - Average profit by persona

## 📁 Files

- `day31.ipynb` - Complete persona analysis notebook
- `customer_persona_summary.csv` - Persona summary table
- `customer_persona_report.md` - Detailed persona report
- `persona_spending.png` - Spending visualization
- `persona_engagement.png` - Engagement visualization
- `persona_profit.png` - Profit visualization
- `README.md` - Project documentation

## 💡 Key Learning

Customer personas transform numerical clustering results into
easy-to-understand customer profiles that can support business
decision-making.

The analysis connects customer behavior with practical strategies
for retention, engagement, promotions, and personalization.

## 🚀 Conclusion

Day 31 demonstrated how behavioral data can be transformed into
meaningful customer personas and actionable business strategies.
"""

with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme)

print("Day 31 README created successfully!")
print("File: README.md")